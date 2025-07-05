# Bank Account Agent

A FastAPI-based bank account agent that provides basic banking operations through a REST API.

## Features

- ✅ Account balance inquiry
- ✅ Account information retrieval
- ✅ Recent transactions view
- ✅ Health check endpoint
- ✅ CORS enabled for web frontend compatibility
- ✅ Ready for deployment on Render's free tier

## API Endpoints

### Base URL
- Local: `http://localhost:8000`
- Production: `https://your-app-name.onrender.com`

### Available Endpoints

1. **Health Check**
   - `GET /`
   - Returns API status and timestamp

2. **Account Balance**
   - `GET /account/balance`
   - Returns current account balance with masked account number

3. **Account Information**
   - `GET /account/info`
   - Returns full account details (masked sensitive data)

4. **Recent Transactions**
   - `GET /account/transactions`
   - Returns list of recent transactions

## Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Access the API:**
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - OpenAPI spec: http://localhost:8000/openapi.json

## Deployment on Render (Free Tier)

### Prerequisites
- GitHub account
- Render account (no credit card required)

### Steps

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/bank-account-agent.git
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Go to [Render](https://render.com)
   - Click "New Web Service"
   - Connect your GitHub repository
   - Select this repository
   - Render will auto-detect Python and use `render.yaml`
   - Click "Create Web Service"

3. **Access your deployed API:**
   - Your app will be available at: `https://bank-agent.onrender.com`

## Example API Responses

### GET /account/balance
```json
{
  "account_balance": "$1250.75",
  "currency": "USD",
  "account_number": "*****6789",
  "last_updated": "2025-07-05T12:00:00.000000"
}
```

### GET /account/info
```json
{
  "account_holder": "John Doe",
  "account_number": "*****6789",
  "account_type": "Checking",
  "balance": "$1250.75",
  "currency": "USD",
  "last_updated": "2025-07-05T12:00:00.000000"
}
```

## Security Notes

- This is a demo application with mock data
- In production, implement proper authentication
- Use environment variables for sensitive data
- Connect to a real database
- Add input validation and error handling
- Implement rate limiting

## Free Tier Limitations

- **Sleep Mode**: Service sleeps after 15 minutes of inactivity
- **Cold Start**: First request after sleep may take 30-60 seconds
- **Resource Limits**: 512 MB RAM, 0.1 CPU
- **750 hours/month**: Sufficient for continuous operation

## Tech Stack

- **FastAPI**: Modern, fast web framework
- **Uvicorn**: ASGI server
- **Python 3.8+**: Programming language
- **Render**: Cloud hosting platform
