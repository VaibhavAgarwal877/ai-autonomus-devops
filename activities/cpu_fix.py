from temporalio import activity
import subprocess

@activity.defn
async def scale_service():
    print("Scaling Deployment")
    subprocess.run([
        "kubectl","scale","deployment","ai-devops-app","--replicas=4"
    ])
    return "done"