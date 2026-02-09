"""
Stock Analysis Platform - Configuration Settings
"""
import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

# Database - use /tmp on Vercel (only writable directory in serverless)
IS_VERCEL = os.getenv("VERCEL", "") == "1"
if IS_VERCEL:
    DB_PATH = Path("/tmp/stock_analyzer.db")
else:
    DB_PATH = Path(os.getenv("DB_PATH", str(DATA_DIR / "stock_analyzer.db")))

# Ensure data directory exists
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# Analysis Parameters
INDICATOR_PERIODS = {
    "rsi": 14,
    "atr": 14,
    "roc_short": 5,
    "roc_medium": 10,
    "roc_long": 20,
    "sma_short": 20,
    "sma_long": 50,
    "macd_fast": 12,
    "macd_slow": 26,
    "macd_signal": 9,
    "bollinger_period": 20,
    "bollinger_std": 2,
    "volume_avg_period": 20,
}

# Momentum Score Weights (must sum to 1.0)
# Combines technical momentum with fundamental quality
SCORE_WEIGHTS = {
    "roc_5": 0.17,              # Short-term momentum
    "roc_10": 0.12,             # Medium-term momentum
    "roc_20": 0.08,             # Longer-term trend
    "relative_strength": 0.12,  # Market outperformance
    "volume_score": 0.08,       # Volume confirmation
    "rsi_score": 0.16,          # RSI momentum
    "ma_score": 0.07,           # Moving Average signals
    "fundamental_score": 0.10,  # P/E, P/B, ROE, D/E, Current Ratio
    "trading_score": 0.10,      # EPS, Beta, 52-wk range, liquidity
}

# Signal Thresholds
SIGNAL_THRESHOLDS = {
    "strong_buy_min": 80,
    "buy_min": 70,
    "hold_min": 40,
    "overbought_rsi": 75,
    "oversold_rsi": 25,
    "volume_confirmation": 1.5,
    "volume_buy": 1.2,
}

# Data Fetching
DATA_FETCH_DAYS = int(os.getenv("DATA_FETCH_DAYS", "90"))
MIN_DATA_DAYS = int(os.getenv("MIN_DATA_DAYS", "60"))

# API Settings
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "5000"))
API_DEBUG = os.getenv("API_DEBUG", "True").lower() == "true"

# Scheduler Settings
MARKET_CLOSE_HOUR = int(os.getenv("MARKET_CLOSE_HOUR", "15"))
MARKET_CLOSE_MINUTE = int(os.getenv("MARKET_CLOSE_MINUTE", "45"))
TIMEZONE = os.getenv("TIMEZONE", "Asia/Kolkata")
