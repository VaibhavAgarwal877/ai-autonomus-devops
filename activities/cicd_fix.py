from temporalio import activity

@activity.defn
async def retry_pipeline(log):
    print("Retrying Jenkins Pipeline")
    return "done"