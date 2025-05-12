# src/backtesting/analyzer.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_results(stats, save_path=None):
    """
    Analyze backtest stats dictionary from backtesting.py and optionally save to a CSV.
    """
    metrics = {
        "Total Return (%)": stats['Return [%]'],
        "Sharpe Ratio": stats['Sharpe Ratio'],
        "Win Rate (%)": stats['Win Rate [%]'],
        "Max Drawdown (%)": stats['Max. Drawdown [%]'],
        "Avg Trade Duration": str(stats['Avg. Trade Duration']),
        "Total Trades": stats['# Trades'],
        "Profit Factor": stats['Profit Factor'],
        "Expectancy": stats['Expectancy [%]'],
        "SQN": stats.get('SQN', None)
    }

    # Print metrics
    print("\n=== Backtest Performance Metrics ===")
    for key, val in metrics.items():
        print(f"{key}: {val}")

    if save_path:
        df = pd.DataFrame(metrics.items(), columns=["Metric", "Value"])
        df.to_csv(save_path, index=False)
        print(f"\nMetrics saved to {save_path}")

    return metrics


def plot_equity_curve(stats):
    """
    Plot the equity curve from stats['_equity_curve']
    """
    equity_curve = stats['_equity_curve']
    equity_curve['Equity'].plot(title="Equity Curve", figsize=(10, 4))
    plt.xlabel("Time")
    plt.ylabel("Equity")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_trade_pnl_distribution(stats):
    """
    Plot a histogram of trade PnL
    """
    trades = stats['_trades']
    pnl = trades['PnL']
    sns.histplot(pnl, kde=True, bins=30)
    plt.title("Trade PnL Distribution")
    plt.xlabel("PnL")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
