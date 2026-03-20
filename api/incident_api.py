from fastapi import FastAPI
from temporalio.client import Client
from workflows.incident_workflow import IncidentWorkflow

app = FastAPI()

@app.post("/incident")
async def create(log: str):

    client = await Client.connect("localhost:7233")

    await client.start_workflow(
        IncidentWorkflow.run,
        log,
        id="manual",
        task_queue="incident-queue"
    )

    return {"status": "triggered"}