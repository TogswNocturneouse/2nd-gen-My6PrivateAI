import asyncio
import uuid
from utils import log

async def run_task(task: dict):
    task_id = str(uuid.uuid4())
    log(f"Starting task {task_id}: {task}")
    await asyncio.sleep(2)
    log(f"Task {task_id} complete")
    return task_id