# coin_analyzer
📊 Price Data Analyzer

A Python project that fetches cryptocurrency price data using Binance API via ccxt, calculates descriptive statistics, and generates visualizations including price trends and volatility.

✨ Features

✅ Fetches OHLCV (Open, High, Low, Close, Volume) data from Binance

✅ Saves data to CSV (data/coin_data.csv)

✅ Computes basic descriptive statistics:

Count, Min, Max, Mean, Median

Standard Deviation, Variance

Skewness, Kurtosis

✅ Visualizations:

Close Price vs Average Close

High–Low Difference

This will:

Fetch the last 90 days of price data for BTC/USDT (daily candles).

Save it to data/coin_data.csv.

Print basic statistics in the console.

Display two charts:

Close Price with Average Line

High–Low Price Difference Over Time

📝 Example Output
Console Stats
Count        90
Min       60251.0
Max       71150.0
Mean      65521.4
Median    65440.5
Std        2910.2
Var     8461453.1
Skew         0.25
Kurtosis    -0.89
dtype: float64

Charts

Close Price with Average Line
Blue line = daily close price
Red dashed line = overall average

High–Low Price Difference
Green line = daily volatility measured as high − low
