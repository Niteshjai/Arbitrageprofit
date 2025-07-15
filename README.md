# Arbitrage Trading Strategy

This project implements an arbitrage trading strategy between the NASDAQ and the Buenos Aires Stock Exchange (BYMA/BCBA) for the Apple Inc. (AAPL) stock.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/arbitrage-trading-strategy.git
   ```
2. Install the required dependencies:
   ```
   pip install numpy pandas requests tvDatafeed
   ```

## Usage

1. Obtain a FastForex API key from [FastForex](https://www.fastforex.io/) and replace `'55614ff050-9418ead798-swtxrx'` in the code with your own API key.
2. Adjust the `stocks` variable to set the number of shares to simulate per trade.
3. Run the `main.py` script:
   ```
   python main.py
   ```
4. The script will output the total profit, final cash, and total shares held after running the arbitrage strategy on historical data.

## API

The project uses the following APIs:

1. [TradingView API](https://www.tradingview.com/pine-script-docs/en/v4/index.html) to fetch historical stock prices for AAPL on the NASDAQ and BYMA/BCBA exchanges.
2. [FastForex API](https://www.fastforex.io/) to fetch the real-time USD to ARS exchange rate.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Testing

The project does not currently include any automated tests. However, you can manually test the functionality by running the `main.py` script and verifying the output.
