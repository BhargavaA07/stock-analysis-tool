import os
from datetime import datetime

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


def fetch_price_data(ticker: str, period: str = "1y") -> pd.DataFrame:
    df = yf.download(ticker, period=period, auto_adjust=False, progress=False)

    if df.empty:
        raise ValueError(f"No data found for ticker '{ticker}'. Check the symbol and try again.")

    # Handle MultiIndex columns from yfinance
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.columns = [str(c).lower().replace(" ", "_") for c in df.columns]
    return df



def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["daily_return"] = df["close"].pct_change()
    df["ma20"] = df["close"].rolling(20).mean()
    df["ma50"] = df["close"].rolling(50).mean()
    df["volatility_20d"] = df["daily_return"].rolling(20).std() * np.sqrt(252)
    return df


def summarize(df: pd.DataFrame, ticker: str) -> dict:
    latest_close = float(df["close"].iloc[-1])
    start_close = float(df["close"].iloc[0])
    total_return = (latest_close / start_close) - 1

    avg_daily_return = float(df["daily_return"].mean())
    daily_vol = float(df["daily_return"].std())
    annual_vol = daily_vol * np.sqrt(252)

    return {
        "Ticker": ticker.upper(),
        "Period Start": df.index.min().date().isoformat(),
        "Period End": df.index.max().date().isoformat(),
        "Start Close": round(start_close, 2),
        "Latest Close": round(latest_close, 2),
        "Total Return (%)": round(total_return * 100, 2),
        "Avg Daily Return (%)": round(avg_daily_return * 100, 4),
        "Annualized Volatility (%)": round(annual_vol * 100, 2),
    }


def plot_price_with_mas(df: pd.DataFrame, ticker: str, out_dir: str = "charts") -> str:
    os.makedirs(out_dir, exist_ok=True)

    plt.figure()
    plt.plot(df.index, df["close"], label="Close")
    plt.plot(df.index, df["ma20"], label="MA20")
    plt.plot(df.index, df["ma50"], label="MA50")
    plt.title(f"{ticker.upper()} Price with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(out_dir, f"{ticker.upper()}_price_ma_{timestamp}.png")
    plt.tight_layout()
    plt.savefig(filepath, dpi=150)
    plt.close()
    return filepath


def save_summary(summary: dict, ticker: str, out_dir: str = "output") -> str:
    os.makedirs(out_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(out_dir, f"{ticker.upper()}_summary_{timestamp}.txt")

    with open(filepath, "w", encoding="utf-8") as f:
        for k, v in summary.items():
            f.write(f"{k}: {v}\n")

    return filepath


def main():
    print("📈 Stock Valuation & Analysis Tool")
    ticker = input("Enter a stock ticker (e.g., AAPL): ").strip()
    period = input("Enter a period (6mo, 1y, 5y). Press Enter for 1y: ").strip() or "1y"

    df = fetch_price_data(ticker, period=period)
    df = add_indicators(df)
    clean = df.dropna()

    summary = summarize(clean, ticker)
    chart_path = plot_price_with_mas(df, ticker)
    summary_path = save_summary(summary, ticker)

    print("\n✅ Done! Summary:")
    for k, v in summary.items():
        print(f"  {k}: {v}")

    print(f"\nSaved chart: {chart_path}")
    print(f"Saved summary: {summary_path}")


if __name__ == "__main__":
    main()
