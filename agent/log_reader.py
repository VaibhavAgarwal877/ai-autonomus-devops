import subprocess

def read_logs():
    result = subprocess.run(
        ["kubectl","logs","-l","app=ai-devops"],
        capture_output=True,
        text=True
    )
    return result.stdout