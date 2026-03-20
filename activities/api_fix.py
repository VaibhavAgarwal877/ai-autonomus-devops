from temporalio import activity
import subprocess

@activity.defn
async def restart_api(log):
    print("Restarting API")
    subprocess.run([
        "kubectl","rollout","restart","deployment/ai-devops-app"
    ])
    return "done"