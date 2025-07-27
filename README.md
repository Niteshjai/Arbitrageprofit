
# Arbitrage Trading Strategy: NASDAQ vs CEDEARs

This Python project simulates an arbitrage strategy between the NASDAQ (U.S. market) and BYMA/BCBA (Argentinian market) using CEDEARs for a foreign asset (e.g., AAPL). It leverages real-time forex data and historical price data from TradingView.

---

## 📌 Overview

CEDEARs are Argentine certificates representing foreign shares. Since each CEDEAR represents a fraction of a foreign stock, price discrepancies between the local (BYMA) and international (NASDAQ) markets can create arbitrage opportunities.

This tool calculates and simulates profits from such opportunities based on the difference between the **actual CEDEAR price** and its **theoretical fair value**.

---

## 📂 Project Structure

```
main.py          # Main script containing the Arbitrage class and simulation
```

---

## ⚙️ How It Works

- Retrieves historical price data for a stock (e.g., AAPL) from:
  - NASDAQ (foreign market)
  - BYMA/BCBA (Argentinian CEDEAR)
- Fetches real-time USD to ARS exchange rate via FastForex API
- Calculates **fair CEDEAR value** using:
  
  Fair CEDEAR Price = NASDAQ Price × USD/ARS Rate × CEDEAR Ratio

- Simulates trades:
  - **Positive Arbitrage:** Buy from NASDAQ and sell on BYMA
  - **Negative Arbitrage:** Buy from BYMA and sell on NASDAQ
- Outputs simulated profit, final cash, and remaining shares

---

## 🧪 Example Usage

```python
api_key = 'your_fastforex_api_key'
stocks = 100

arb_strat = arbitrage(api_key, stocks)
profit, final_cash, shares_held = arb_strat.profit()

print('Total_profit is', profit)
print('Final_cash is', final_cash)
print('Total_sharesheld is', shares_held)
```

---

## 🔐 Security Warning

- Do **NOT** hardcode credentials (`username`, `password`, `api_key`) directly in production code.
- Use **environment variables** or a `.env` file with secure loading (e.g., via `python-dotenv`).

---

## 📦 Dependencies

Install required packages via pip:

```bash
pip install pandas numpy requests tvDatafeed
```

---

## 📈 Data Sources

- 📊 **Stock Prices:** [tvDatafeed](https://github.com/StreamAlpha/tvdatafeed)
- 💱 **Forex Rates:** [FastForex API](https://fastforex.io/)

---

## 📌 Notes

- CEDEAR ratio (1/20) is hardcoded for AAPL. Adjust accordingly for other stocks.
- Uses 1000 bars of daily historical data from TradingView.
- Designed for educational/backtesting purposes; not intended for live trading without further development.

---

## 🧠 Author

Nitesh Jaiswal — [LinkedIn](https://www.linkedin.com/in/nitesh-jaiswal)

---

## 📜 License

This project is licensed for educational use. Modify freely for personal or academic purposes.
