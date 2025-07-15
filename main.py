import numpy as np
import pandas as pd
import requests
from tvDatafeed import TvDatafeed, Interval

# TradingView credentials (should be secured using environment variables in production)
username = 'Niteshjai'
password = 'Niteshjaiswal1234'

# Initialize TradingView API
tv = TvDatafeed(username, password)

class arbitrage():
    def __init__(self, api_key, stocks):
        self.initial_cash = 100000     # Starting capital in ARS
        self.cash = self.initial_cash  # Current available cash
        self.shares_held = 0           # Total shares held
        self.api_key = api_key         # FastForex API key
        self.stocks = stocks           # Number of stocks to simulate arbitrage with
        self.ratio = 1 / 20            # CEDEAR ratio: 1 CEDEAR = 1/20 foreign share
        self.rate = self.get_usd_to_ars_rate_fastforex()  # Exchange rate USD to ARS

    def get_usd_to_ars_rate_fastforex(self):
        # Fetch real-time USD to ARS conversion rate using FastForex API
        url = f'https://api.fastforex.io/fetch-one?from=USD&to=ARS&api_key={self.api_key}'
        response = requests.get(url)
        data = response.json()

        # Return exchange rate if successful, else raise error
        if response.status_code == 200 and 'result' in data:
            return data['result']['ARS']
        else:
            raise Exception(f"API error or no data: {data}")
    
    def get_data(self):
        # Fetch recent NASDAQ prices for AAPL (foreign listing)
        data_us = tv.get_hist(
            symbol='AAPL',
            exchange='NASDAQ',
            interval=Interval.in_daily,
            n_bars=1000
        )['close']

        # Fetch recent CEDEAR prices for AAPL on BYMA/BCBA (local listing)
        data_ar = tv.get_hist(
            symbol='AAPL',
            exchange='BCBA',  # Buenos Aires stock exchange
            interval=Interval.in_daily,
            n_bars=1000
        )['close']
        
        # Combine into single DataFrame
        df = pd.DataFrame({
            'NASDAQ': data_us,
            'BYMA':   data_ar
        })

        # Calculate the fair CEDEAR price using arbitrage formula
        df['fair_cedear'] = df['NASDAQ'] * self.rate * self.ratio

        # Arbitrage = Actual CEDEAR price - Fair price
        df['arbitrage'] = df['BYMA'] - df['fair_cedear']
        df['profit'] = 0.0  # Placeholder for simulated profit per day

        print(df)  # Print full DataFrame for inspection
        return df

    def buy(self, exchange, shares, price):
        # Simulate buying shares from an exchange
        cost = shares * price
        if self.cash >= cost:
            self.cash -= cost
            self.shares_held += shares

    def sell(self, exchange, shares, price):
        # Simulate selling shares to an exchange
        if self.shares_held >= shares:
            proceeds = shares * price
            self.cash += proceeds
            self.shares_held -= shares

    def profit(self):
        # Run the full arbitrage strategy on historical data
        df = self.get_data()

        for i, row in df.iterrows():
            arb = row['arbitrage']

            if arb > 0:
                # Positive arbitrage: foreign is cheaper → Buy on NASDAQ, sell on BYMA
                self.buy('NASDAQ', self.stocks, row['NASDAQ'])
                self.sell('BYMA', self.stocks, row['BYMA'])
                df.at[i, 'profit'] = arb * self.stocks

            elif arb < 0:
                # Negative arbitrage: local is cheaper → Buy on BYMA, sell on NASDAQ
                self.buy('BYMA', self.stocks, row['BYMA'])
                self.sell('NASDAQ', self.stocks, row['NASDAQ'])
                df.at[i, 'profit'] = abs(arb * self.stocks)

            # If arb ≈ 0 → No trade

        # Sum all simulated profits across days
        total_profit = df['profit'].sum()
        return total_profit, self.cash, self.shares_held


# ========== Usage ==========

api_key = '55614ff050-9418ead798-swtxrx'  # Your FastForex API key
stocks = 100                              # Number of shares to simulate per trade
arb_strat = arbitrage(api_key, stocks)    # Instantiate strategy object

# Run simulation
profit, final_cash, shares_held = arb_strat.profit()

# Display results
print('Total_profit is', profit)
print('Final_cash is', final_cash)
print('Total_sharesheld is', shares_held)
