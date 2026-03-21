from temporalio import activity
import subprocess
import time

@activity.defn
async def restart_pod():

    print("🔁 Restarting Kubernetes Deployment...")

    subprocess.run(
        ["kubectl", "rollout", "restart", "deployment/ai-devops-app"]
    )

    # 🔥 prevent rapid repeat
    time.sleep(5)

    return "pod restarted"