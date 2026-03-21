import asyncio
import subprocess
import time
import hashlib
from temporalio.client import Client
from workflows.incident_workflow import IncidentWorkflow

COOLDOWN = 60
last_trigger_time = 0
last_hash = ""


def get_logs():
    result = subprocess.run(
        ["kubectl", "logs", "-l", "app=ai-devops"],
        capture_output=True,
        text=True
    )
    return result.stdout


def get_hash(data):
    return hashlib.md5(data.encode()).hexdigest()


async def trigger(log):

    global last_trigger_time

    # ⛔ cooldown check
    if time.time() - last_trigger_time < COOLDOWN:
        print("⏳ Cooldown active, skipping...")
        return

    print("🚀 Triggering workflow...")

    client = await Client.connect("localhost:7233")

    await client.start_workflow(
        IncidentWorkflow.run,
        log,
        id=f"incident-{int(time.time())}",
        task_queue="incident-queue"
    )

    last_trigger_time = time.time()


async def monitor():

    global last_hash

    print("🔍 Smart Monitoring started...")

    while True:

        logs = get_logs()

        # 🔥 limit logs (cost + stability)
        logs = logs[-2000:]

        current_hash = get_hash(logs)

        if current_hash != last_hash:

            print("📡 New logs detected")

            await trigger(logs)

            last_hash = current_hash

        else:
            print("😴 No change, skipping")

        await asyncio.sleep(30)


if __name__ == "__main__":
    asyncio.run(monitor())