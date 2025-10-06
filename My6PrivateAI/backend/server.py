from fastapi import FastAPI, WebSocket
from executor import run_task
import asyncio

app = FastAPI()

logs = []

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/api/run_task")
async def run_task_endpoint(task: dict):
    task_id = await run_task(task)
    return {"task_id": task_id}

@app.websocket("/ws/logs")
async def websocket_logs(ws: WebSocket):
    await ws.accept()
    while True:
        if logs:
            await ws.send_text(logs.pop(0))
        await asyncio.sleep(0.1)