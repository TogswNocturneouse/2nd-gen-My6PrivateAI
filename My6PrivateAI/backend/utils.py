logs = []

def log(message: str):
    from datetime import datetime
    logs.append(f"[{datetime.now().isoformat()}] {message}")