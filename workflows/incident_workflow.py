from temporalio import workflow

@workflow.defn
class IncidentWorkflow:

    @workflow.run
    async def run(self, log):

        from agent.incident_agent import analyze_incident

        from activities.kubernetes_fix import restart_pod
        from activities.docker_fix import restart_container
        from activities.cicd_fix import retry_pipeline
        from activities.cpu_fix import scale_service
        from activities.api_fix import restart_api

        print("Workflow Started")

        decision = analyze_incident()

        print("Decision:", decision)

        action_map = {
            "restart_pod": restart_pod,
            "restart_docker": restart_container,
            "retry_pipeline": retry_pipeline,
            "scale_service": scale_service,
            "restart_api": restart_api
        }

        activity = action_map.get(decision)

        return await workflow.execute_activity(
            activity,
            log,
            start_to_close_timeout=30
        )