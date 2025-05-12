import pandas as pd
import numpy as np
from ta.trend import SMAIndicator
from binance.client import Client



class MultiTimeFrameStrategy:
    def __init__(self, client, symbol):
        self.client = client
        self.symbol = symbol
        self.entry_timeframe = Client.KLINE_INTERVAL_15MINUTE 
        self.confirmation_timeframe = Client.KLINE_INTERVAL_1HOUR  
    
    def fetch_data_15_minutes(self,limit=500):
        klines = self.client.get_klines(symbol=self.symbol, interval=self.entry_timeframe, limit=limit)
        df = pd.DataFrame(klines, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 
            'quote_asset_volume', 'num_trades', 'taker_buy_base_vol', 'taker_buy_quote_vol', 'ignore'
        ])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        return df
    
    def fetch_data_1_Hour(self,limit=500):
        klines = self.client.get_klines(symbol=self.symbol, interval=self.confirmation_timeframe, limit=limit)
        df = pd.DataFrame(klines, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 
            'quote_asset_volume', 'num_trades', 'taker_buy_base_vol', 'taker_buy_quote_vol', 'ignore'
        ])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        return df
    
    
    @staticmethod
    def calc_sma_fast(df):
        sma = SMAIndicator(close=df['close'], window=50)
        df['sma_50'] = sma.sma_indicator()
        return df
    
    @staticmethod
    def calc_sma_slow(df):
        sma = SMAIndicator(close=df['close'], window=200)
        df['sma_200'] = sma.sma_indicator()
        return df
    
    @staticmethod
    def sell_buy_condition(df_15m,df_1h):
        signal = pd.DataFrame(index=df_15m.index)
        df_15m['sma_50'] = df_15m['sma_50'].astype(float)
        df_15m['sma_200']=df_15m['sma_200'].astype(float)
        df_1h['sma_50'] = df_1h['sma_50'].astype(float)
        df_1h['sma_200']=df_1h['sma_200'].astype(float)
        signal['Buy']=(df_15m['sma_200']<df_15m['sma_50']) & (df_1h['sma_200']<df_1h['sma_50'])
        signal['Sell']=(df_15m['sma_200']>df_15m['sma_50']) | (df_1h['sma_200']>df_1h['sma_50'])
        signal['Buy'] = signal['Buy'].astype(bool)
        signal['Sell'] = signal['Sell'].astype(bool)
        signal['Buy'] = signal['Buy'].astype(bool).shift().fillna(False).astype(bool)
        signal['Sell'] = signal['Sell'].astype(bool).shift().fillna(False).astype(bool)
        return signal
    

    

