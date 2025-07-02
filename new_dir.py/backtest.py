from backtesting import backtest
bt = Backtest(
    price1,
    SMAMultiTFStrategy,
    cash=1000000,
    commission=.001,
    exclusive_orders=True
)


stats = bt.run()
print(stats)