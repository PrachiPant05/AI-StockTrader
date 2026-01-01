# Stock Trading Backtester

A comprehensive Python-based backtesting framework for evaluating multiple trading strategies across different investment styles. Test how various technical analysis strategies would have performed on historical stock data.

## Features

- **Multiple Trading Strategies**
  - Bollinger Bands
  - MACD (Moving Average Convergence Divergence)
  - RSI (Relative Strength Index)
  - SMA (Simple Moving Average)
  - VWAP (Volume Weighted Average Price)

- **Investment Styles**
  - Aggressive: High-frequency trading, maximum capital allocation
  - Moderate: Balanced approach with medium risk
  - Passive: Conservative, long-term focused strategy

- **Performance Metrics**
  - Portfolio value tracking
  - Buy-and-hold comparison (HODL)
  - Return on investment calculations
  - Trade history analysis

- **Interactive Visualizations**
  - Candlestick charts
  - Buy/sell signal markers
  - Price trend analysis
  - Built with Plotly for interactive exploration

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/stock-backtester.git
cd stock-backtester
```

2. Create a virtual environment:
```bash
# Windows
python -m venv stock
stock\Scripts\activate

# macOS/Linux
python3 -m venv stock
source stock/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
stock-backtester/
├── src/
│   ├── data/
│   │   ├── __init__.py
│   │   └── data_loader.py          # Data fetching and preprocessing
│   ├── strategies/
│   │   ├── __init__.py
│   │   ├── base_strategy.py        # Abstract base class
│   │   ├── bollinger_band.py       # Bollinger Bands strategy
│   │   ├── macd.py                 # MACD strategy
│   │   ├── rsi.py                  # RSI strategy
│   │   ├── simple_moving_average.py # SMA strategy
│   │   └── vwap.py                 # VWAP strategy
│   ├── backtest/
│   │   ├── __init__.py
│   │   └── backtester.py           # Backtesting engine
│   └── visualizations.py           # Plotting functions
├── main.py                         # Main execution script
├── requirements.txt                # Project dependencies
└── README.md                       # This file
```

## Usage

### Basic Usage

Run the backtester with default settings (AAPL stock, moderate style):

```bash
python main.py
```

### Customization

Edit `main.py` to customize parameters:

```python
# Configuration
TICKER = "AAPL"              # Change to any stock symbol
INITIAL_CAPITAL = 10000      # Starting investment amount
INVESTMENT_STYLE = "moderate" # Options: 'aggressive', 'moderate', 'passive'

# Backtest period (default: last 2 years)
start_date = (data.index.max() - timedelta(days=365*2)).date()
end_date = data.index.max().date()
```

### Example Output

```
Loading data for AAPL...
Data loaded: 2517 rows
Date range: 2015-01-02 to 2025-01-01

Backtest period: 2023-01-01 to 2025-01-01

Testing strategies with moderate investment style...

Running Bollinger Bands strategy...
  Final Portfolio Value: $12,345.67
  Portfolio Return: 23.46%
  HODL Return: 18.23%
  Number of Trades: 15

Running MACD strategy...
  Final Portfolio Value: $11,892.45
  Portfolio Return: 18.92%
  HODL Return: 18.23%
  Number of Trades: 22
```

## Strategies Explained

### Bollinger Bands
Uses price volatility bands to identify overbought and oversold conditions. Buys when price touches lower band, sells at upper band.

### MACD
Tracks the relationship between two exponential moving averages. Generates buy signals on bullish crossovers and sell signals on bearish crossovers.

### RSI
Measures momentum on a 0-100 scale. Buys when oversold (below 30), sells when overbought (above 70).

### Simple Moving Average
Uses crossover of short-term and long-term moving averages. Buys on golden cross, sells on death cross.

### VWAP
Compares current price to volume-weighted average price. Buys when price exceeds VWAP, sells when below.

## Investment Styles

| Style      | Capital Allocation | Signal Threshold | Trading Frequency |
|------------|-------------------|------------------|-------------------|
| Aggressive | 100% per trade    | Accept all signals | High             |
| Moderate   | 50% per trade     | Medium strength   | Medium           |
| Passive    | 25% per trade     | Strong signals only | Low             |

## Dependencies

- pandas >= 2.0.0 - Data manipulation and analysis
- yfinance >= 0.2.0 - Stock data retrieval from Yahoo Finance
- plotly >= 5.0.0 - Interactive visualizations
- numpy >= 1.24.0 - Numerical computations

## Data Source

Historical stock data is fetched from Yahoo Finance using the yfinance library. The system automatically downloads 10 years of historical data for any valid stock ticker.

## Performance Considerations

- Backtesting results do not guarantee future performance
- Does not account for trading fees, slippage, or taxes
- Assumes perfect order execution at closing prices
- Past performance is not indicative of future results

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-strategy`)
3. Commit your changes (`git commit -m 'Add new trading strategy'`)
4. Push to the branch (`git push origin feature/new-strategy`)
5. Open a Pull Request

### Adding New Strategies

To add a new trading strategy:

1. Create a new file in `src/strategies/`
2. Extend the `BaseStrategy` class
3. Implement the `generate_signals()` method
4. Add your strategy to the `strategies` dictionary in `main.py`

Example:

```python
from .base_strategy import BaseStrategy

class MyStrategy(BaseStrategy):
    def __init__(self, data, capital, investment_style="Moderate"):
        super().__init__(data, capital)
        self.investment_style = investment_style
    
    def generate_signals(self):
        # Your signal generation logic here
        self.data['Signal'] = 0  # 1 for buy, -1 for sell, 0 for hold
        return self.data['Signal']
```

## Troubleshooting

### ModuleNotFoundError
Ensure virtual environment is activated and all dependencies are installed:
```bash
pip install -r requirements.txt
```

### No data loaded
Check internet connection. The system requires access to Yahoo Finance API.

### Import errors
Verify project structure and ensure all `__init__.py` files exist in package directories.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This software is for educational and research purposes only. It is not financial advice. Always consult with a qualified financial advisor before making investment decisions. The authors are not responsible for any financial losses incurred through the use of this software.

## Acknowledgments

- Yahoo Finance for providing free historical stock data
- The Python community for excellent data science libraries
- Technical analysis concepts from industry-standard trading methodologies

## Contact

For questions, suggestions, or issues, please open an issue on GitHub or contact the maintainers.

---

Made with Python | Built for traders and developers | Open Source
