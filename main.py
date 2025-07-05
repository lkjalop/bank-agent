from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import uvicorn
import os

app = FastAPI(
    title="Bank Account Agent",
    description="A simple FastAPI application for bank account operations",
    version="1.0.0"
)

# Add CORS middleware for web frontend compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock database - in production, you'd use a real database
mock_account_data = {
    "account_number": "123456789",
    "account_holder": "John Doe",
    "balance": 1250.75,
    "currency": "USD",
    "account_type": "Checking",
    "last_updated": datetime.now().isoformat()
}

@app.get("/")
@app.head("/")
def root():
    """Root endpoint - health check (supports both GET and HEAD requests)"""
    return {
        "message": "Bank Account Agent is running!",
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
@app.head("/health")
def health_check():
    """Dedicated health check endpoint for load balancers"""
    return {"status": "healthy"}

@app.get("/account/balance")
def get_balance():
    """Get account balance"""
    return {
        "account_balance": f"${mock_account_data['balance']:.2f}",
        "currency": mock_account_data["currency"],
        "account_number": mock_account_data["account_number"][-4:].rjust(len(mock_account_data["account_number"]), "*"),
        "last_updated": mock_account_data["last_updated"]
    }

@app.get("/account/info")
def get_account_info():
    """Get full account information"""
    return {
        "account_holder": mock_account_data["account_holder"],
        "account_number": mock_account_data["account_number"][-4:].rjust(len(mock_account_data["account_number"]), "*"),
        "account_type": mock_account_data["account_type"],
        "balance": f"${mock_account_data['balance']:.2f}",
        "currency": mock_account_data["currency"],
        "last_updated": mock_account_data["last_updated"]
    }

@app.get("/account/transactions")
def get_recent_transactions():
    """Get recent transactions (mock data)"""
    return {
        "transactions": [
            {
                "id": "txn_001",
                "date": "2025-07-04",
                "description": "Online Purchase - Amazon",
                "amount": -89.99,
                "balance_after": 1250.75
            },
            {
                "id": "txn_002",
                "date": "2025-07-03",
                "description": "Salary Deposit",
                "amount": 2500.00,
                "balance_after": 1340.74
            },
            {
                "id": "txn_003",
                "date": "2025-07-02",
                "description": "ATM Withdrawal",
                "amount": -100.00,
                "balance_after": -1159.26
            }
        ],
        "account_number": mock_account_data["account_number"][-4:].rjust(len(mock_account_data["account_number"]), "*")
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting server on 0.0.0.0:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
