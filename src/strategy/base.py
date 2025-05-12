from abc import ABC, abstractmethod


class BaseStrategy(ABC):
    def __init__(self, client, symbol):
        self.client = client
        self.symbol = symbol

    @abstractmethod
    def fetch_data(self, timeframe, limit=500):
        """Fetch historical data for a given timeframe"""
        pass

    @abstractmethod
    def calc_sma(self, df, window: int):
        """Calculate SMA for the given DataFrame"""
        pass

    @abstractmethod
    def sell_buy_condition(self, df_15m, df_1h):
        """Define the buy and sell conditions based on strategy logic"""
        pass
