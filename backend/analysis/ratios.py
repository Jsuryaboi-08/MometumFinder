"""
Fundamental and Trading Ratios Analysis Module

Fetches and scores key business and trading ratios from Yahoo Finance.
Used to enhance the momentum scoring with fundamental quality metrics.

Fundamental Ratios (Valuation & Health):
- P/E Ratio, P/B Ratio, ROE, Debt/Equity, Current Ratio, Dividend Yield

Trading Ratios (Market Activity):
- EPS, Beta, 52-Week Range Position, Average Volume, Market Cap
"""
import yfinance as yf
import pandas as pd
import numpy as np
from typing import Dict, Optional


def fetch_all_ratios(symbol: str) -> Dict:
    """
    Fetch all fundamental and trading ratios for a stock.
    
    Args:
        symbol: Stock symbol with .NS suffix (e.g., 'RELIANCE.NS')
        
    Returns:
        Dictionary with all ratio values
    """
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        
        # Current price for calculations
        current_price = info.get('currentPrice') or info.get('regularMarketPrice', 0)
        
        # 52-week range position
        fifty_two_week_high = info.get('fiftyTwoWeekHigh', 0)
        fifty_two_week_low = info.get('fiftyTwoWeekLow', 0)
        
        if fifty_two_week_high and fifty_two_week_low and fifty_two_week_high != fifty_two_week_low:
            week_52_position = ((current_price - fifty_two_week_low) / 
                               (fifty_two_week_high - fifty_two_week_low)) * 100
        else:
            week_52_position = 50  # Default to middle
        
        return {
            # Fundamental Ratios
            'pe_ratio': info.get('trailingPE') or info.get('forwardPE'),
            'pb_ratio': info.get('priceToBook'),
            'roe': info.get('returnOnEquity', 0) * 100 if info.get('returnOnEquity') else None,
            'debt_to_equity': info.get('debtToEquity', 0) / 100 if info.get('debtToEquity') else None,
            'current_ratio': info.get('currentRatio'),
            'dividend_yield': info.get('dividendYield', 0) * 100 if info.get('dividendYield') else 0,
            
            # Trading Ratios
            'eps': info.get('trailingEps') or info.get('forwardEps'),
            'beta': info.get('beta'),
            'week_52_high': fifty_two_week_high,
            'week_52_low': fifty_two_week_low,
            'week_52_position': round(week_52_position, 2),
            'avg_volume': info.get('averageVolume'),
            'avg_volume_10d': info.get('averageVolume10days'),
            'market_cap': info.get('marketCap'),
            'market_cap_category': _categorize_market_cap(info.get('marketCap')),
            
            # Additional useful info
            'profit_margin': info.get('profitMargins', 0) * 100 if info.get('profitMargins') else None,
            'operating_margin': info.get('operatingMargins', 0) * 100 if info.get('operatingMargins') else None,
            'revenue_growth': info.get('revenueGrowth', 0) * 100 if info.get('revenueGrowth') else None,
        }
        
    except Exception as e:
        print(f"Error fetching ratios for {symbol}: {str(e)}")
        return {}


def _categorize_market_cap(market_cap: Optional[float]) -> str:
    """Categorize market cap into size buckets."""
    if market_cap is None:
        return 'Unknown'
    
    # Values in INR Crores (1 Cr = 10 million)
    cap_in_cr = market_cap / 10_000_000
    
    if cap_in_cr >= 100_000:  # 1 Lakh Cr+
        return 'Mega Cap'
    elif cap_in_cr >= 20_000:  # 20,000 Cr+
        return 'Large Cap'
    elif cap_in_cr >= 5_000:  # 5,000 Cr+
        return 'Mid Cap'
    elif cap_in_cr >= 500:  # 500 Cr+
        return 'Small Cap'
    else:
        return 'Micro Cap'


# ============================================================
# FUNDAMENTAL RATIO SCORING
# ============================================================

def score_pe_ratio(pe: Optional[float]) -> float:
    """
    Score P/E ratio (0-100).
    
    Optimal range: 8-20 (fair value)
    - Very low (<5): Could indicate problems or deep value
    - Low (5-12): Good value
    - Fair (12-20): Reasonable
    - High (20-30): Growth premium
    - Very high (>30): Expensive or high growth
    """
    if pe is None or pe <= 0:
        return 50  # Neutral for missing/negative
    
    if 12 <= pe <= 20:
        return 85 + (1 - abs(pe - 16) / 4) * 15  # Peak at 16
    elif 8 <= pe < 12:
        return 75 + (pe - 8) / 4 * 10
    elif 20 < pe <= 25:
        return 70 - (pe - 20) / 5 * 10
    elif 5 <= pe < 8:
        return 60 + (pe - 5) / 3 * 15
    elif 25 < pe <= 35:
        return 50 - (pe - 25) / 10 * 15
    elif pe < 5:
        return 40 + pe / 5 * 20  # Very low could be value trap
    else:  # pe > 35
        return max(20, 35 - (pe - 35) * 0.5)


def score_pb_ratio(pb: Optional[float]) -> float:
    """
    Score P/B ratio (0-100).
    
    Optimal: 0.5-3.0
    - <1: Trading below book value (could be undervalued)
    - 1-3: Fair range
    - >3: Premium valuation
    """
    if pb is None or pb <= 0:
        return 50
    
    if 1 <= pb <= 2:
        return 85 + (1 - abs(pb - 1.5) / 0.5) * 15
    elif 0.5 <= pb < 1:
        return 70 + (pb - 0.5) / 0.5 * 15  # Below book can be good
    elif 2 < pb <= 3:
        return 70 - (pb - 2) * 10
    elif pb < 0.5:
        return 50 + pb / 0.5 * 20  # Very low might be troubled
    else:  # pb > 3
        return max(20, 60 - (pb - 3) * 5)


def score_roe(roe: Optional[float]) -> float:
    """
    Score Return on Equity (0-100).
    
    Higher is better:
    - <5%: Poor
    - 5-10%: Below average
    - 10-15%: Average
    - 15-25%: Good
    - >25%: Excellent
    """
    if roe is None:
        return 50
    
    if 15 <= roe <= 25:
        return 80 + (roe - 15) / 10 * 20
    elif 10 <= roe < 15:
        return 60 + (roe - 10) / 5 * 20
    elif 25 < roe <= 35:
        return 95 + min(5, (roe - 25) / 10 * 5)
    elif 5 <= roe < 10:
        return 40 + (roe - 5) / 5 * 20
    elif roe > 35:
        return 100  # Cap at 100
    else:  # roe < 5
        return max(10, 20 + roe * 4)


def score_debt_to_equity(de: Optional[float]) -> float:
    """
    Score Debt/Equity ratio (0-100).
    
    Lower is generally better:
    - 0-0.3: Very low debt (conservative)
    - 0.3-0.7: Low debt (healthy)
    - 0.7-1.0: Moderate debt
    - 1.0-2.0: Higher debt
    - >2.0: High leverage (risky)
    """
    if de is None:
        return 50
    
    if de < 0:
        de = 0  # Negative D/E shouldn't happen, treat as 0
    
    if 0.2 <= de <= 0.5:
        return 90 + (1 - abs(de - 0.35) / 0.15) * 10
    elif de < 0.2:
        return 85 + de / 0.2 * 5  # Very low is good but not perfect
    elif 0.5 < de <= 0.8:
        return 75 - (de - 0.5) / 0.3 * 10
    elif 0.8 < de <= 1.0:
        return 60 - (de - 0.8) / 0.2 * 10
    elif 1.0 < de <= 1.5:
        return 45 - (de - 1.0) / 0.5 * 10
    elif 1.5 < de <= 2.0:
        return 30 - (de - 1.5) / 0.5 * 10
    else:  # de > 2.0
        return max(10, 20 - (de - 2.0) * 5)


def score_current_ratio(cr: Optional[float]) -> float:
    """
    Score Current Ratio (0-100).
    
    Measures liquidity:
    - <1: Liquidity concerns
    - 1-1.5: Adequate
    - 1.5-2.5: Good
    - 2.5-3: Very good
    - >3: Might be inefficient use of assets
    """
    if cr is None:
        return 50
    
    if 1.5 <= cr <= 2.5:
        return 85 + (1 - abs(cr - 2.0) / 0.5) * 15
    elif 1.2 <= cr < 1.5:
        return 70 + (cr - 1.2) / 0.3 * 15
    elif 2.5 < cr <= 3.0:
        return 85 - (cr - 2.5) / 0.5 * 10
    elif 1.0 <= cr < 1.2:
        return 55 + (cr - 1.0) / 0.2 * 15
    elif cr > 3.0:
        return max(60, 75 - (cr - 3.0) * 5)
    else:  # cr < 1.0
        return max(20, 55 * cr)


def calculate_fundamental_score(ratios: Dict) -> float:
    """
    Calculate combined fundamental score (0-100).
    
    Weights:
    - P/E: 25%
    - P/B: 15%
    - ROE: 30%
    - D/E: 20%
    - Current Ratio: 10%
    """
    pe_score = score_pe_ratio(ratios.get('pe_ratio'))
    pb_score = score_pb_ratio(ratios.get('pb_ratio'))
    roe_score = score_roe(ratios.get('roe'))
    de_score = score_debt_to_equity(ratios.get('debt_to_equity'))
    cr_score = score_current_ratio(ratios.get('current_ratio'))
    
    weighted_score = (
        pe_score * 0.25 +
        pb_score * 0.15 +
        roe_score * 0.30 +
        de_score * 0.20 +
        cr_score * 0.10
    )
    
    return round(weighted_score, 2)


# ============================================================
# TRADING RATIO SCORING
# ============================================================

def score_eps(eps: Optional[float]) -> float:
    """
    Score EPS (0-100).
    
    Higher is better, but context matters.
    Positive EPS is good, negative is concerning.
    """
    if eps is None:
        return 50
    
    if eps <= 0:
        return max(10, 30 + eps * 2)  # Negative EPS is bad
    elif eps >= 100:
        return 95  # Very high EPS
    elif eps >= 50:
        return 85 + (eps - 50) / 50 * 10
    elif eps >= 20:
        return 70 + (eps - 20) / 30 * 15
    elif eps >= 5:
        return 50 + (eps - 5) / 15 * 20
    else:  # eps 0-5
        return 40 + eps / 5 * 10


def score_beta(beta: Optional[float]) -> float:
    """
    Score Beta (0-100).
    
    Measures volatility relative to market:
    - Beta < 0.8: Low volatility (defensive)
    - Beta 0.8-1.2: Market-like
    - Beta > 1.2: High volatility
    
    For momentum trading, moderate beta is preferred.
    """
    if beta is None:
        return 50
    
    if 0.8 <= beta <= 1.2:
        return 85 + (1 - abs(beta - 1.0) / 0.2) * 15
    elif 0.5 <= beta < 0.8:
        return 65 + (beta - 0.5) / 0.3 * 20
    elif 1.2 < beta <= 1.5:
        return 70 - (beta - 1.2) / 0.3 * 15
    elif beta < 0.5:
        return 50 + beta / 0.5 * 15
    elif 1.5 < beta <= 2.0:
        return 50 - (beta - 1.5) / 0.5 * 15
    else:  # beta > 2.0
        return max(20, 35 - (beta - 2.0) * 10)


def score_52week_position(position: float) -> float:
    """
    Score 52-week price position (0-100).
    
    Position is percentage from low to high (0-100).
    - Near low (0-20%): Potential value or falling knife
    - Mid-low (20-40%): Could be accumulation zone
    - Middle (40-60%): Neutral
    - Mid-high (60-80%): Uptrend, momentum
    - Near high (80-100%): Strong but watch for reversal
    
    For momentum, we favor stocks in uptrend (60-85%).
    """
    if position is None:
        return 50
    
    if 60 <= position <= 80:
        return 85 + (1 - abs(position - 70) / 10) * 15  # Peak at 70%
    elif 50 <= position < 60:
        return 70 + (position - 50) / 10 * 15
    elif 80 < position <= 90:
        return 80 - (position - 80) / 10 * 10
    elif 40 <= position < 50:
        return 55 + (position - 40) / 10 * 15
    elif 90 < position <= 100:
        return 65 - (position - 90) / 10 * 15  # Near high, be cautious
    elif 25 <= position < 40:
        return 40 + (position - 25) / 15 * 15
    else:  # position < 25
        return max(25, 40 - (25 - position))


def score_liquidity(avg_volume: Optional[float]) -> float:
    """
    Score based on average trading volume (0-100).
    
    Higher volume = better liquidity = easier trading.
    """
    if avg_volume is None or avg_volume <= 0:
        return 50
    
    # Volume thresholds (for NSE stocks)
    if avg_volume >= 10_000_000:  # 1 Cr+ shares
        return 95
    elif avg_volume >= 5_000_000:  # 50 Lakh+
        return 85 + (avg_volume - 5_000_000) / 5_000_000 * 10
    elif avg_volume >= 1_000_000:  # 10 Lakh+
        return 70 + (avg_volume - 1_000_000) / 4_000_000 * 15
    elif avg_volume >= 500_000:  # 5 Lakh+
        return 55 + (avg_volume - 500_000) / 500_000 * 15
    elif avg_volume >= 100_000:  # 1 Lakh+
        return 40 + (avg_volume - 100_000) / 400_000 * 15
    else:
        return max(20, 40 * avg_volume / 100_000)


def calculate_trading_score(ratios: Dict) -> float:
    """
    Calculate combined trading score (0-100).
    
    Weights:
    - EPS: 25%
    - Beta: 20%
    - 52-week position: 35%
    - Liquidity: 20%
    """
    eps_score = score_eps(ratios.get('eps'))
    beta_score = score_beta(ratios.get('beta'))
    position_score = score_52week_position(ratios.get('week_52_position', 50))
    liquidity_score = score_liquidity(ratios.get('avg_volume'))
    
    weighted_score = (
        eps_score * 0.25 +
        beta_score * 0.20 +
        position_score * 0.35 +
        liquidity_score * 0.20
    )
    
    return round(weighted_score, 2)


def get_ratio_breakdown(ratios: Dict) -> Dict:
    """Get detailed breakdown of ratio scores."""
    return {
        'fundamental': {
            'pe_ratio': {
                'value': ratios.get('pe_ratio'),
                'score': score_pe_ratio(ratios.get('pe_ratio')),
            },
            'pb_ratio': {
                'value': ratios.get('pb_ratio'),
                'score': score_pb_ratio(ratios.get('pb_ratio')),
            },
            'roe': {
                'value': ratios.get('roe'),
                'score': score_roe(ratios.get('roe')),
            },
            'debt_to_equity': {
                'value': ratios.get('debt_to_equity'),
                'score': score_debt_to_equity(ratios.get('debt_to_equity')),
            },
            'current_ratio': {
                'value': ratios.get('current_ratio'),
                'score': score_current_ratio(ratios.get('current_ratio')),
            },
            'total_score': calculate_fundamental_score(ratios),
        },
        'trading': {
            'eps': {
                'value': ratios.get('eps'),
                'score': score_eps(ratios.get('eps')),
            },
            'beta': {
                'value': ratios.get('beta'),
                'score': score_beta(ratios.get('beta')),
            },
            'week_52_position': {
                'value': ratios.get('week_52_position'),
                'score': score_52week_position(ratios.get('week_52_position', 50)),
            },
            'liquidity': {
                'value': ratios.get('avg_volume'),
                'score': score_liquidity(ratios.get('avg_volume')),
            },
            'total_score': calculate_trading_score(ratios),
        }
    }


if __name__ == "__main__":
    # Test with sample stock
    print("Testing ratios module with RELIANCE.NS...")
    ratios = fetch_all_ratios("RELIANCE.NS")
    
    print("\n=== Fetched Ratios ===")
    for key, value in ratios.items():
        print(f"  {key}: {value}")
    
    print("\n=== Fundamental Score ===")
    print(f"  Score: {calculate_fundamental_score(ratios)}/100")
    
    print("\n=== Trading Score ===")
    print(f"  Score: {calculate_trading_score(ratios)}/100")
    
    print("\n=== Detailed Breakdown ===")
    breakdown = get_ratio_breakdown(ratios)
    print("Fundamental:")
    for k, v in breakdown['fundamental'].items():
        if k != 'total_score':
            print(f"  {k}: value={v['value']}, score={v['score']}")
    print("Trading:")
    for k, v in breakdown['trading'].items():
        if k != 'total_score':
            print(f"  {k}: value={v['value']}, score={v['score']}")
