# 📈 Stock Analytics Dashboard – Backend

This is the **FastAPI backend** for the Stock Analytics Dashboard project. It handles secure API endpoints to fetch and process historical stock data from Yahoo Finance based on user input. Firebase Authentication is used to validate access tokens and authorize users.

---

## 🔧 Features

- 🔐 Firebase Authentication verification for each request
- 📊 Fetch historical stock data using `yfinance`
- 📁 Supports multiple tickers and various timeframes
- 🧠 Caching using `cachetools` to optimize API usage
- 🛡️ Proper CORS setup for frontend integration

---

## ⚙️ Tech Stack

- **FastAPI** – Backend API framework
- **Firebase Admin SDK** – Authentication token validation
- **yfinance** – Stock data retrieval
- **cachetools** – In-memory caching
- **Uvicorn** – ASGI server
- **Pydantic** – Request and response validation

---

## 📂 Project Structure

stock-dashboard-backend/
├── app/
│ ├── init.py
│ ├── config.py # Firebase Admin SDK init
│ ├── routes/
│ │ └── stocks.py # Main API endpoint
│ └── utils/
│ └── auth.py # Token verification helper
├── firebase-adminsdk.json # (ignored via .gitignore)
├── main.py # Entry point for FastAPI
├── requirements.txt
└── README.md

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/stock-dashboard-backend.git
cd stock-dashboard-backend
```

2. Set Up Virtual Environment

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install Dependencies
   pip install -r requirements.txt

4. Firebase Setup

   Go to Firebase Console

   Create a new project (or use existing)

   Navigate to Project Settings > Service Accounts

   Click Generate new private key → Save the JSON file as firebase-adminsdk.json in the root

   🔐 IMPORTANT: This file should be listed in .gitignore and never committed.

5 Running the Server
uvicorn main:app --reload

By default, the app will be running at: http://localhost:8000

Authentication
Authorization: Bearer <firebase_id_token>

API Endpoint
POST /api/stocks
Fetch historical stock data for one or more tickers.

Request Body
{
"tickers": ["AAPL", "GOOGL"],
"timeframe": "1w", // Options: 1d, 1w, 1m, 3m, 6m, 1y
"start_date": "2025-05-25",
"end_date": "2025-06-01"
}
Response
{
"AAPL": [
{"date": "2025-05-25", "close": 175.3},
...
],
"GOOGL": [
{"date": "2025-05-25", "close": 120.9},
...
]
}

Dependencies
All required packages are listed in requirements.txt, including:

    fastapi

    uvicorn

    firebase-admin

    yfinance

    cachetools

    python-multipart

    pydantic

Gen AI Tool Usage
This project was built with guidance from ChatGPT, including:

    Firebase Admin SDK integration in FastAPI

    CORS middleware setup

    Efficient caching with cachetools

    Debugging 405/401 CORS + token issues

    Pythonic structure & code cleanup

🧪 Future Improvements
⏳ Rate limiting per IP or Firebase UID

      📥 Store request logs or preferences in Firestore

      📈 Add support for technical indicators (e.g., SMA, RSI)

      ✅ Unit tests and integration test coverage

      🔒 Token expiry handling and refresh support

📄 License
This project is licensed under the MIT License

🙌 Acknowledgments
FastAPI

      Firebase Admin SDK

      Yahoo Finance via yfinance

      ChatGPT by OpenAI
