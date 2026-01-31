# Stock Valuation & Analysis Tool (Python)

A beginner-friendly Python project that pulls real stock market data and generates performance and risk analysis with visual outputs.

This project demonstrates how Python can be used to work with real financial data, calculate key metrics, and produce reusable analysis artifacts.

---

## Features
- Fetches historical stock price data for any ticker using Yahoo Finance (`yfinance`)
- Calculates key financial indicators:
  - Daily returns
  - 20-day and 50-day moving averages
  - Annualized volatility (risk proxy)
- Generates:
  - Price + moving average chart saved to `charts/`
  - Text-based summary report saved to `output/`
- Handles real-world data edge cases (e.g., MultiIndex columns from data sources)

---

## Tech Stack
- Python
- pandas
- numpy
- matplotlib
- yfinance

---

## Project Structure
stock-analysis-tool/
├── stock_analysis.py
├── requirements.txt
├── README.md
├── .gitignore
├── charts/
│   └── sample_aapl.png
├── output/
└── .venv/

---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

## Run the program
python stock_analysis.py

## Example inputs
Ticker: AAPL
Period: 1y (default, press Enter)

## Sample Output
Apple Inc. (AAPL) – 1 Year Analysis


The chart shows the stock’s closing price along with its 20-day and 50-day moving averages to highlight trends and momentum.

## What I Learned
How to retrieve and analyze real-world financial market data using Python
Applying financial concepts such as returns, trend indicators, and volatility
Handling data inconsistencies from external APIs
Structuring a Python project for reuse and sharing (requirements, outputs, documentation)

## Future Improvements
Add benchmark comparison against the S&P 500
Include valuation metrics such as P/E ratio and market capitalization
Convert the script into an interactive dashboard

## Disclaimer
This project is for educational purposes only and does not constitute investment advice.