#!/bin/bash
echo "Starting backend..."
cd backend
uvicorn server:app --reload &
echo "Backend started"

echo "Starting executor loop..."
python3 executor.py &
echo "Executor started"

echo "All systems nominal. Connect via iOS console."