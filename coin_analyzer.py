import ccxt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os


coin = "BTC/USDT"
timeframe = "1d"
exchange = ccxt.binance()


since = int((datetime.now() - timedelta(days=90)).timestamp() * 1000)  

def coin_fetch_ohlcv(symbol, timeframe, since=since):
    data = exchange.fetch_ohlcv(symbol, timeframe, since)
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df


if not os.path.exists("data"):
    os.makedirs("data")

# --- Fetch data ---
df = coin_fetch_ohlcv(coin, timeframe, since)
df.to_csv("data/coin_data.csv")
print("Data saved to data/coin_data.csv")

def basic_stats(df):
    stats = {
        "Count": len(df),
        "Min": df['close'].min(),
        "Max": df['close'].max(),
        "Mean": df['close'].mean(),
        "Median": df['close'].median(),
        "Std": df['close'].std(),
        "Var": df['close'].var(),
        "Skew": df['close'].skew(),
        "Kurtosis": df['close'].kurtosis()
    }
    return pd.Series(stats)


basic_stats(df)

# ---Close price and Average close plotting---
average_price = df['close'].mean()
time = df.index
plt.figure(figsize=(12,6))
plt.plot(time, df['close'], label='Close Price', color='blue')
plt.axhline(average_price, color='red', linestyle='--', label='Average Price')
plt.title(f'{coin} Close Price Over Time')
plt.xlabel('Time')
plt.ylabel('Price (USDT)')
plt.legend()
plt.grid()
plt.show()



# --- High-Low Difference Plot ---
diff = df['high'] - df['low']
plt.figure(figsize=(12,6))
plt.plot(time, diff, label='High-Low Difference', color='green')
plt.title(f'{coin} High-Low Price Difference Over Time')
plt.xlabel('Time')
plt.ylabel('Price Difference (USDT)')
plt.legend()
plt.grid()
plt.show()
