from temporalio import activity
import subprocess

@activity.defn
async def restart_pod(log):
    print("Restarting Kubernetes Deployment")
    subprocess.run([
        "kubectl","rollout","restart","deployment/ai-devops-app"
    ])
    return "done"