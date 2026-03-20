import asyncio
import requests
import time
from temporalio.client import Client
from workflows.incident_workflow import IncidentWorkflow

async def trigger(log):

    client = await Client.connect("localhost:7233")

    await client.start_workflow(
        IncidentWorkflow.run,
        log,
        id=f"id-{int(time.time())}",
        task_queue="incident-queue"
    )

async def monitor():

    while True:

        try:
            r = requests.get("http://localhost:30007/health")

            if r.json()["status"] != "ok":
                print("🚨 Incident")
                await trigger("API Down")

        except:
            print("🚨 Down")
            await trigger("API Down")

        await asyncio.sleep(10)

asyncio.run(monitor())