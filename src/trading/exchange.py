from binance.client import Client
from ..config.config import BINANCE_API_KEY, BINANCE_API_SECRET

class BinanceExchange:
    def __init__(self):
        self.client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
        
    def get_balance(self):
        """Get balance of account"""
        return self.client.get_account()

    def place_order(self, symbol, side, quantity, price):
        """Place a buy/sell order on Binance"""
        if side == "BUY":
            order = self.client.order_market_buy(symbol=symbol, quantity=quantity)
        else:
            order = self.client.order_market_sell(symbol=symbol, quantity=quantity)
        return order
