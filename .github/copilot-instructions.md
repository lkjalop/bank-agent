# GitHub Copilot Instructions

## Architecture Overview
This is a single-file FastAPI application (`main.py`) designed for Render's free tier deployment. The architecture is intentionally simple: one FastAPI app with in-memory mock data, no database, minimal dependencies.

**Key architectural decisions:**
- Single `main.py` file contains all logic to minimize cold start time on Render
- Mock data stored in global dictionary `mock_account_data` for simplicity
- CORS middleware configured for broad web frontend compatibility
- Account number masking pattern: `[-4:].rjust(len(account_number), "*")` used consistently

## Critical Developer Workflows

### Local Development
```bash
# Install and run locally
pip install -r requirements.txt
uvicorn main:app --reload

# Test endpoints
curl http://localhost:8000/account/balance
# Access interactive docs at http://localhost:8000/docs
```

### Deployment (Render)
- Push to GitHub, connect to Render
- `render.yaml` configures: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- No build steps needed beyond `pip install -r requirements.txt`

## Project-Specific Patterns

### Account Number Masking
Always mask account numbers in responses using this exact pattern:
```python
"account_number": mock_account_data["account_number"][-4:].rjust(len(mock_account_data["account_number"]), "*")
```

### Response Structure
All endpoints return JSON with:
- Consistent field naming (snake_case in data, exact field names matter)
- ISO timestamp format: `datetime.now().isoformat()`
- Currency formatting: `f"${amount:.2f}"`
- Account number reference in all account-related responses

### Mock Data Management
- Single global dict `mock_account_data` in `main.py`
- Timestamp set once at startup: `"last_updated": datetime.now().isoformat()`
- Transaction amounts use realistic values with proper negative/positive signs
- Transaction IDs follow pattern: `txn_001`, `txn_002`, etc.

## Integration Points

### FastAPI Specifics
- App instantiation includes title, description, version for OpenAPI docs
- CORS middleware configured with `allow_origins=["*"]` for demo purposes
- Health check at root `/` endpoint returns status and timestamp
- All endpoints use simple functions (no classes/dependency injection)

### Render Deployment
- Environment variable `$PORT` provided by Render
- No database connection required
- Free tier limits: 512 MB RAM, 0.1 CPU, 15-minute sleep
- `render.yaml` service type: `web`, env: `python`

## Code Conventions

### Adding New Endpoints
Follow the existing pattern in `main.py`:
```python
@app.get("/account/new-endpoint")
def get_new_data():
    """Descriptive docstring"""
    return {
        "field_name": "value",
        "account_number": mock_account_data["account_number"][-4:].rjust(len(mock_account_data["account_number"]), "*"),
        "last_updated": mock_account_data["last_updated"]
    }
```

### Error Handling (Not Yet Implemented)
When adding error handling, use FastAPI's `HTTPException`:
```python
from fastapi import HTTPException, status
raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Account not found")
```

This is a demo application with mock data. Focus on maintaining the simple, single-file architecture and consistent response patterns rather than adding complex features.
