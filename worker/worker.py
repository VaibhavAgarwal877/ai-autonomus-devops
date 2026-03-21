import asyncio
from temporalio.client import Client
from temporalio.worker import Worker

from workflows.incident_workflow import IncidentWorkflow

from activities.kubernetes_fix import restart_pod
from activities.docker_fix import restart_container
from activities.cicd_fix import retry_pipeline
from activities.cpu_fix import scale_service
from activities.api_fix import restart_api
from activities.llm_activity import analyze_with_llm

async def main():

    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="incident-queue",
        workflows=[IncidentWorkflow],
        activities=[
            analyze_with_llm,
            restart_pod,
            restart_container,
            retry_pipeline,
            scale_service,
            restart_api
        ],
    )

    await worker.run()

asyncio.run(main())