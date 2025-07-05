#!/bin/bash
export HOST=0.0.0.0
export PORT=${PORT:-10000}
echo "Starting on $HOST:$PORT"
exec uvicorn main:app --host $HOST --port $PORT
