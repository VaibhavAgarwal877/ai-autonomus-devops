from temporalio import activity
import subprocess

@activity.defn
async def restart_container():
    print("Restarting Docker Container")
    subprocess.run(["docker","restart","ai-devops-app"])
    return "done"