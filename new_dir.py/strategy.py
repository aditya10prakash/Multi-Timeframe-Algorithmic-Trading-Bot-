# src/backtesting/backtest.py

import pandas as pd
#from backtesting import Backtest, Strategy
from ta.trend import SMAIndicator
from backtesting.lib import crossover
from binance.client import Client
from abc import ABC, abstractmethod
import time
class Strategy(ABC):
    def __init__(self):
        self.data = None
        self.symbol=None
        self.quantity=None

    def I(self, func, *args, **kwargs):
        return func(*args, **kwargs)

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def next(self):
        pass

    def buy(self):
        print("Buy")
        client.order_market_buy(symbol=self.symbol, quantity=self.quantity)

    def sell(self):
        print("Sell")
        client.order_market_sell(symbol=self.symbol, quantity=self.quantity)
    
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
            self.sell()


class forward_test_class:
    def __init__(self, strategy_cls, data, symbol, quantity):
        self.strategy = strategy_cls()
        self.strategy.data = data
        self.strategy.symbol = symbol
        self.strategy.quantity = quantity

    def run(self):
        self.strategy.init()
        self.strategy.next()


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
client = Client(api_key, api_secret,testnet=True)
client.API_URL = 'https://testnet.binance.vision/api'
price1 = client.get_klines(symbol="BTCUSDT",interval=Client.KLINE_INTERVAL_15MINUTE, limit=50000)
price2 = client.get_klines(symbol="BTCUSDT",interval=Client.KLINE_INTERVAL_4HOUR, limit=50000)
price1 = convert_to_dataframe(price1)
price2 = convert_to_dataframe(price2)
print(price1)
print(price2)



bt = forward_test_class(
    strategy_cls=SMAMultiTFStrategy,
    data=price1,
    symbol='BTCUSDT',
    quantity=0.001,
)
start_time = time.time()
duration = 5 * 60  # 5 minutes in seconds

while time.time() - start_time < duration:
    price1 = client.get_klines(symbol="BTCUSDT",interval=Client.KLINE_INTERVAL_15MINUTE, limit=50000)
    price2 = client.get_klines(symbol="BTCUSDT",interval=Client.KLINE_INTERVAL_4HOUR, limit=50000)
    price1 = convert_to_dataframe(price1)
    price2 = convert_to_dataframe(price2)



    bt = forward_test_class(
        strategy_cls=SMAMultiTFStrategy,
        data=price1,
        symbol='BTCUSDT',
        quantity=0.001,
    )
    bt.run()
