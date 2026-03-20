from strands import Agent
from strands.models import BedrockModel
from agent.log_reader import read_logs

model = BedrockModel(
    model_id="anthropic.claude-3-sonnet"
)

agent = Agent(model=model)

def analyze_incident():

    logs = read_logs()

    prompt = f"""
Analyze logs and return action:

restart_pod
restart_docker
retry_pipeline
scale_service
restart_api

Logs:
{logs}
"""

    return agent(prompt).strip()