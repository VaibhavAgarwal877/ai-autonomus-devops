from temporalio import activity

@activity.defn
async def retry_pipeline():
    print("Retrying Jenkins Pipeline")
    return "done"