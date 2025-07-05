# Port Binding Fix for Render Deployment

## Problem
The application was failing to deploy on Render with the error:
```
No open ports detected on 0.0.0.0, continuing to scan...
Port scan timeout reached, no open ports detected on 0.0.0.0
```

## Root Cause
The FastAPI application was hardcoded to use port 8000 in the `if __name__ == "__main__"` block, but Render expects applications to use the `$PORT` environment variable that it provides dynamically.

## Solution
### 1. Added `os` import
```python
import os
```

### 2. Updated port configuration
**Before:**
```python
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**After:**
```python
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
```

### 3. How it works
- `os.environ.get("PORT", 8000)` gets the PORT environment variable from Render
- If PORT is not set (local development), it defaults to 8000
- `int()` converts the string to an integer as required by uvicorn

## Files Updated
- `main.py` - Added port environment variable handling

## Render Configuration
The `render.yaml` was already correctly configured:
```yaml
startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
```

## Expected Result
After this fix:
- ✅ Application will bind to Render's assigned port
- ✅ Render will detect the open port successfully
- ✅ Application will be accessible at your Render URL
- ✅ Local development still works on port 8000

## Next Steps
1. The fix has been pushed to GitHub
2. Render will automatically redeploy your application
3. Your app should be accessible at: `https://bank-agent.onrender.com`

## Testing
Once deployed, test these endpoints:
- `GET /` - Health check
- `GET /account/balance` - Account balance
- `GET /account/info` - Account information
- `GET /account/transactions` - Transaction history
- `GET /docs` - Interactive API documentation
