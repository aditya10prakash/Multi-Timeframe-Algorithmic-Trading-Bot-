from binance.client import Client
import pandas as pd
from backtesting.lib import crossover
from ta.trend import SMAIndicator
import os
from datetime import datetime
import csv
import time
API_KEY = "NHSMqF5cVs6jHun0ZBM8ca8p1YgHFGlh346UU61HQlXuI94V9DyjwOYbejqkBVfH"
API_SECRET = "IpmoR9gJgBPDf28Hwj2NnBBfNHzOhVJTt6V5dQdhas9QIDdw1Roqjqj3ppuUXgnQ"
client=Client(API_KEY,API_SECRET,testnet=True)
print(client.get_account())
LIVE_TRADES_FILE = "data/live_trades.csv"
class Trading_bot:
    def __init__(self,ticker):
        self.ticker=ticker

    def get_current_price(self):
        symbol=client.get_symbol_ticker(self.ticker)
        return float(symbol['price'])
    
    @staticmethod
    def log_trade_to_csv(side, symbol, quantity, price):
        file_exists = os.path.isfile(LIVE_TRADES_FILE)
        with open(LIVE_TRADES_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Time', 'Symbol', 'Side', 'Quantity', 'Price'])
            writer.writerow([datetime.now(), symbol, side, quantity, price])

    @staticmethod
    def place_buy_order(symbol, quantity=1):
        print("BUY")
        order = client.order_market_buy(symbol=symbol, quantity=quantity)
        price = float(order['fills'][0]['price'])
        Trading_bot.log_trade_to_csv('BUY', symbol, quantity, price)

    @staticmethod
    def place_sell_order(symbol, quantity=1):
        print("SELL")
        order = client.order_market_sell(symbol=symbol, quantity=quantity)
        price = float(order['fills'][0]['price'])
        Trading_bot.log_trade_to_csv('SELL', symbol, quantity, price)

    
    @staticmethod
    def buy_sell_order_condition(symbol):
        df_15=client.get_klines(symbol=symbol,interval=Client.KLINE_INTERVAL_1MINUTE, limit=500)
        df_15=Trading_bot.convert_to_dataframe(df_15)
        sma_50=SMAIndicator(df_15['Close'],window=50).sma_indicator()
        sma_200=SMAIndicator(df_15['Close'],window=100).sma_indicator()
        sma_50_values = sma_50.iloc[-2:].values
        sma_200_values = sma_200.iloc[-2:].values
        if sma_50_values[0] < sma_200_values[0] and sma_50_values[1] > sma_200_values[1]:
            print("BUY signal detected (SMA50 crossed above SMA200)")
            Trading_bot.place_buy_order(symbol)
        elif sma_50_values[0] > sma_200_values[0] and sma_50_values[1] < sma_200_values[1]:
            print("SELL signal detected (SMA50 crossed below SMA200)")
            Trading_bot.place_sell_order(symbol)
    
    @staticmethod
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

bot =Trading_bot('EPICUSDT')
start_time = time.time()
duration = 5 * 60  # 5 minutes in seconds

while time.time() - start_time < duration:
    Trading_bot.buy_sell_order_condition('BTCUSDT')
