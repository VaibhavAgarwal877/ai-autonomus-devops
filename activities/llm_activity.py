from temporalio import activity
from agent.incident_agent import analyze_incident

@activity.defn
async def analyze_with_llm(log: str) -> str:
    print("Calling LLM for analysis...")

    decision = analyze_incident(log)

    print(f" LLM Decision: {decision}")

    return decision