# src/backtesting/backtest.py

import pandas as pd
from backtesting import Backtest, Strategy
from ta.trend import SMAIndicator
from backtesting.lib import crossover
from binance.client import Client
import os
#from config.config import API_KEY, API_SECRET
class SMAMultiTFStrategy(Strategy):
    sma_short = 50
    sma_long = 100

    def init(self):
        close = pd.Series(self.data.Close) 

        self.sma_50 = self.I(lambda x: SMAIndicator(x, window=self.sma_short).sma_indicator(), close)
        self.sma_200 = self.I(lambda x: SMAIndicator(x, window=self.sma_long).sma_indicator(), close)

    def next(self):
        if crossover(self.sma_50,self.sma_200):
            self.buy()
        elif crossover(self.sma_200,self.sma_50):
            self.position.close()


def convert_to_dataframe(kline_data):
    df = pd.DataFrame(kline_data, columns=[
        'timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'close_time',
        'quote_asset_volume', 'num_trades', 'taker_buy_base_vol', 'taker_buy_quote_vol', 'ignore'
    ])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Convert timestamp to datetime
    df.set_index('timestamp', inplace=True)  # Set timestamp as the index
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
    df['High'] = pd.to_numeric(df['High'], errors='coerce')
    df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
    df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')
    return df
api_key='NHSMqF5cVs6jHun0ZBM8ca8p1YgHFGlh346UU61HQlXuI94V9DyjwOYbejqkBVfH'
api_secret='IpmoR9gJgBPDf28Hwj2NnBBfNHzOhVJTt6V5dQdhas9QIDdw1Roqjqj3ppuUXgnQ'
client = Client(api_key, api_secret)
price1 = client.get_klines(symbol="BTCUSDT",interval=Client.KLINE_INTERVAL_15MINUTE, limit=50000)
price2 = client.get_klines(symbol="BTCUSDT",interval=Client.KLINE_INTERVAL_4HOUR, limit=50000)
price1 = convert_to_dataframe(price1)
price2 = convert_to_dataframe(price2)
print(price1)
print(price2)



bt = Backtest(
    price1,
    SMAMultiTFStrategy,
    cash=1000000,
    commission=.001,
    exclusive_orders=True
)


stats = bt.run()
print(stats)

# Extract trade log
trades = stats['_trades']
trades = trades[['EntryTime', 'ExitTime', 'EntryPrice', 'ExitPrice', 'Size', 'PnL']]
trades['Direction'] = trades['Size'].apply(lambda x: 'LONG' if x > 0 else 'SHORT')
trades = trades.rename(columns={
    'EntryTime': 'Timestamp',
    'EntryPrice': 'Price'
})

# Keep only essential columns
trades_log = trades[['Timestamp', 'Direction', 'Price']]

log_path = os.path.join('..', 'data', 'backtest_trades.csv')  # Going up to save in data/
# Ensure directory exists
os.makedirs(os.path.dirname(log_path), exist_ok=True)

# Save to CSV
trades_log.to_csv(log_path, index=False)

print(f"Trade log saved to {log_path}")

