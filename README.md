# 📈 Momentum Finder - Stock Analysis Platform

A comprehensive stock analysis platform that uses technical indicators to identify momentum opportunities in the Indian stock market (NSE).

## 🚀 Features

- **Stock Screener** - Rank stocks using a proprietary scoring algorithm based on RSI, MACD, price trends, and volume
- **Signal Recommendations** - Get actionable buy/sell signals with target prices
- **Monte Carlo Forecasting** - Price predictions using Monte Carlo simulation
- **Gems Finder** - Discover oversold stocks with strong fundamentals
- **Sector Analysis** - Compare sector performance and identify trends
- **Nifty 50 Dashboard** - Real-time market overview and top movers

## 🛠️ Tech Stack

### Frontend
- **React 18** with Vite for fast development
- **Tailwind CSS** for modern styling
- **Recharts** for interactive charts
- **React Router** for navigation

### Backend
- **Python/Flask** REST API
- **yfinance** for market data
- **pandas-ta** for technical analysis
- **APScheduler** for automated data updates

## 📋 Prerequisites

- **Node.js** v18+ and npm
- **Python** 3.10+
- **pip** package manager

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Jsuryaboi-08/MometumFinder.git
cd MometumFinder
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Copy environment config
cp .env.example .env
```

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install
```

### 4. Initialize Database & Fetch Data
```bash
cd backend

# Fetch stock data (first time setup - takes 5-10 mins)
python run.py --fetch-data
```

## ▶️ Running Locally

### Start Backend (Terminal 1)
```bash
cd backend
python run.py
# API runs at http://localhost:5000
```

### Start Frontend (Terminal 2)
```bash
cd frontend
npm run dev
# App runs at http://localhost:5173
```

Open **http://localhost:5173** in your browser.

## 📡 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/health` | Health check |
| `GET /api/screener` | Stock rankings and scores |
| `GET /api/stock/<symbol>` | Detailed stock analysis |
| `GET /api/signals` | Buy/sell recommendations |
| `GET /api/nifty` | Nifty 50 index data |
| `GET /api/sectors` | Sector performance |
| `GET /api/top-movers` | Top gainers/losers |
| `GET /api/market-overview` | Dashboard summary |
| `GET /api/forecast/<symbol>` | Monte Carlo forecast |
| `GET /api/gems` | Undervalued stock picks |

## 🌐 Deployment

### Vercel (Frontend + Serverless)
The project includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) for automatic deployment to Vercel.

**Required Secrets:**
- `VERCEL_TOKEN`
- `VERCEL_ORG_ID`
- `VERCEL_PROJECT_ID`

### Backend Hosting
For production, deploy the Flask backend to:
- [Render](https://render.com)
- [Railway](https://railway.app)
- [PythonAnywhere](https://pythonanywhere.com)

## 📁 Project Structure

```
MometumFinder/
├── backend/
│   ├── api/            # Flask REST API
│   ├── analysis/       # Technical indicators & scoring
│   ├── data/           # Data fetching & database
│   ├── scheduler/      # Automated jobs
│   ├── config.py       # Configuration
│   └── run.py          # Entry point
├── frontend/
│   ├── src/
│   │   ├── components/ # React components
│   │   ├── pages/      # Page views
│   │   └── App.jsx     # Main app
│   └── vite.config.js  # Vite config
└── README.md
```

## 📄 License

MIT License

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

**Built with ❤️ for Indian retail investors**
