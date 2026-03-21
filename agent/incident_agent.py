import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:1b"


def analyze_incident(log: str) -> str:

    prompt = f"""
You are a DevOps AI.

Analyze logs and return ONLY ONE action:

restart_pod
restart_docker
retry_pipeline
scale_service
restart_api

Logs:
{log}

ONLY return one word.
"""

    try:
        print("🤖 Calling LLM for analysis...")

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )

        data = response.json()

        print("🧾 RAW RESPONSE:", data)

        result = data.get("response", "").strip().lower()

        if not result:
            print("⚠️ Empty response → fallback")
            return "restart_pod"

        allowed = [
            "restart_pod",
            "restart_docker",
            "retry_pipeline",
            "scale_service",
            "restart_api"
        ]

        for action in allowed:
            if action in result:
                print(f"✅ Final Decision: {action}")
                return action

        print("⚠️ Unknown output → fallback")
        return "restart_pod"

    except Exception as e:
        print(f"❌ LLM Error: {e}")
        return "restart_pod"