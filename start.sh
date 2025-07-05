#!/bin/bash
echo "Starting FastAPI Bank Account Agent..."
echo "PORT environment variable: $PORT"
echo "Starting uvicorn with host 0.0.0.0 and port $PORT"
exec uvicorn main:app --host 0.0.0.0 --port $PORT --workers 1
