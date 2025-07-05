#!/usr/bin/env python3
"""
Render deployment startup script for FastAPI Bank Account Agent
"""
import os
import uvicorn
from main import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print(f"🚀 Starting FastAPI Bank Account Agent on 0.0.0.0:{port}")
    print(f"Environment PORT: {os.environ.get('PORT', 'Not set')}")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info",
        access_log=True
    )
