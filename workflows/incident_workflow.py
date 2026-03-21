from temporalio import workflow
from datetime import timedelta

with workflow.unsafe.imports_passed_through():
    from activities.llm_activity import analyze_with_llm
from activities.kubernetes_fix import restart_pod
from activities.docker_fix import restart_container
from activities.cicd_fix import retry_pipeline
from activities.cpu_fix import scale_service
from activities.api_fix import restart_api


@workflow.defn
class IncidentWorkflow:

    @workflow.run
    async def run(self, log: str):

        print(f"🚨 Incident received:\n{log}")

        # 🔥 STEP 1: LLM decision
        decision = await workflow.execute_activity(
            analyze_with_llm,
            log,
            start_to_close_timeout=timedelta(seconds=60)
        )

        print(f"🧠 Decision: {decision}")

        # 🔥 STEP 2: Dynamic mapping (NO IF)
        action_map = {
            "restart_pod": restart_pod,
            "restart_docker": restart_container,
            "retry_pipeline": retry_pipeline,
            "scale_service": scale_service,
            "restart_api": restart_api,
        }

        activity_fn = action_map.get(decision)

        # 🔥 STEP 3: Execute action (fallback safe)
        if activity_fn:
            return await workflow.execute_activity(
                activity_fn,
                start_to_close_timeout=timedelta(seconds=60)
            )

        print("⚠️ Unknown decision, no action taken")
        return "no_action"

