
from src.data.data_loader import load_data

from src.data.data_loader import load_data
from src.strategies.bollinger_band import BollingerBandStrategy
from src.backtest.backtester import Backtester
from src.visualizations import plot_results

# Step 1: Load data
data = load_data('stock_data.csv')

# Step 2: Initialize strategy
strategy = BollingerBandStrategy(params={'window': 20, 'num_std_dev': 2})

# Step 3: Run backtester
backtester = Backtester(data, strategy, initial_capital=10000)
results = backtester.run()

# Step 4: Visualize results
plot_results(results)
