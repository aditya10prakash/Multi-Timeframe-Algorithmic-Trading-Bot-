<<<<<<< HEAD
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/LiQFGrUV)
# Multi-Timeframe Trading Strategy

A sophisticated trading system that implements a multi-timeframe strategy using Python, with both backtesting and live trading capabilities on Binance Testnet.

## Project Overview

This project implements a trading strategy that combines multiple timeframes (15-minute entries with 1-hour confirmations) to make trading decisions. The system includes both backtesting capabilities using `backtesting.py` and live trading functionality through Binance Testnet API.

### Key Features

- Multi-timeframe strategy implementation (15m entries, 1h confirmations)
- Comprehensive backtesting system with detailed trade logging
- Live trading integration with Binance Testnet
- Trade comparison and analysis tools
- Modular, class-based architecture for maintainability and extensibility

## Project Structure

```
├── README.md
├── requirements.txt
├── config/
│   └── config.py           # Configuration settings and API keys
├── src/
│   ├── strategy/
│   │   ├── base.py        # Base strategy class
│   │   └── multi_tf.py    # Multi-timeframe strategy implementation
│   ├── backtesting/
│   │   ├── backtest.py    # Backtesting engine
│   │   └── analyzer.py    # Backtest results analysis
│   ├── trading/
│   │   ├── exchange.py    # Binance API wrapper
│   │   └── executor.py    # Trade execution logic
│   └── utils/
│       ├── logger.py      # Logging utilities
│       └── data.py        # Data handling utilities
└── data/
    ├── backtest_trades.csv    # Backtest trade logs
    └── live_trades.csv        # Live trading logs

```


## Strategy Details

The strategy combines signals from two timeframes:
- 15-minute timeframe for entry signals
- 1-hour timeframe for trade confirmation

Key components:
- Entry signals generated on 15m timeframe
- Trade confirmation using 1h timeframe indicators
- Risk management rules implemented at both timeframes
- Position sizing based on volatility and account equity

## Trade Logging

Both backtest and live trades are logged with:
- Timestamp
- Trade direction (long/short)
- Entry price
- Exit price
- Position size
- PnL
- Additional metadata

## Development Guidelines

- Document all classes and methods
- Use logging for debugging and monitoring

## Dependencies

Key packages used:
- backtesting.py
- python-binance
- pandas
- numpy
- ta (Technical Analysis library)
- python-dotenv

## Notes

- Always test thoroughly on Binance Testnet before live deployment
- Monitor trade execution latency
- Regularly validate strategy performance
- Keep API keys secure and never commit them to version control


## Author

Siddhant, Numatix

## Acknowledgments

- Binance for providing the Testnet API
- backtesting.py library contributors
- Technical Analysis library contributors 
=======
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/u7GUY31k)
# Multi-Asset Portfolio Analysis Assessment

## Important Notice
**The use of AI tools, large language models (LLMs), code generation tools, or similar automated assistance is strictly prohibited for this assessment. This assignment is designed to test your individual research, coding, and problem-solving skills. Any evidence of using such tools will result in an automatic failure.**

## Objective
Develop a comprehensive Python script that downloads historical price data for multiple assets using yfinance, processes the data, and performs in-depth analysis of a diversified portfolio's performance.

## Implementation Requirements
**You must use object-oriented programming with Python classes for this assessment.** Your implementation should include:

- A Portfolio class to manage the assets, weights, and portfolio calculations
- Appropriate class structure demonstrating proper encapsulation and separation of concerns
- Methods that handle specific tasks like data cleaning, performance calculation, and visualization
- Clean code organization with well-defined class interfaces

Proper use of object-oriented design principles will be a significant factor in your evaluation.

## Deadline
**Monday, May 5**

## Assessment Description

### 1. Data Acquisition
- Use the yfinance library to download historical daily price data for at least 10 different assets over a 10-year period
- Include a diverse selection of assets to build a well-diversified portfolio
- Ensure that the data includes both adjusted and unadjusted closing prices

### 2. Data Cleaning and Preparation
- Handle missing data by:
  - Interpolating minor gaps in the time series
  - Dropping or forward-filling rows with missing data exceeding a threshold (e.g., 5 consecutive days)
- Adjust prices for corporate actions (splits, dividends) to ensure consistency across the time series
- Create a clean, consistent dataset ready for analysis

### 3. Portfolio Construction
- Create a DataFrame representing a diversified portfolio by assigning different weights to each asset
- Ensure all weights sum to 1
- Calculate daily portfolio returns based on these weights and the adjusted closing prices

### 4. Performance Metrics Calculation
- Cumulative Return: Total portfolio return over the entire period
- Annualized Return: Yearly equivalent return
- Annualized Volatility: Standard deviation of returns (annualized)
- Sharpe Ratio: Risk-adjusted return using a 3-month Treasury yield as risk-free rate
- Drawdown Analysis: Maximum drawdown and duration of drawdowns to understand downside risk
- **Important**: Use QuantStats to generate comprehensive portfolio performance metrics and tear sheets

### 5. Correlation and Risk Analysis
- Create a correlation matrix of assets using daily returns to analyze diversification benefits
- Perform rolling correlation analysis to observe changing relationships between assets over time
- Identify periods where diversification benefits may have been reduced

### 6. Advanced Data Visualization
Create the following visualizations:
- Cumulative portfolio return over time
- Correlation matrix heatmap with annotations for correlation coefficients
- Rolling volatility of the portfolio and individual assets
- Drawdown curve visualizing periods of portfolio losses relative to peak
- Comparison of individual asset performances
- QuantStats performance and risk tear sheets

### 7. Portfolio Optimization (Optional but Recommended)
- Implement a mean-variance optimization routine to maximize the Sharpe ratio or minimize risk
- Compare the optimized portfolio metrics to the original portfolio
- Provide insights on the optimization results

## Required Libraries
- pandas
- numpy
- yfinance
- matplotlib
- seaborn
- scipy
- quantstats

## Assessment Deliverables

1. Python script or Jupyter Notebook containing:
   - Complete code with all steps documented
   - Proper implementation of Python classes for portfolio management
   - Markdown cells explaining your approach and key decisions
   - All required visualizations

2. Performance summary including:
   - Cumulative and annualized returns
   - Volatility and risk-adjusted performance
   - Maximum drawdown and recovery periods
   - Asset correlations and diversification benefits
   - Complete QuantStats tear sheet (HTML export)

3. Visualization portfolio including:
   - Time series plots of portfolio performance
   - Risk-return charts
   - Correlation heatmaps
   - Drawdown charts
   - QuantStats performance visualizations

4. (Optional) Optimization results:
   - Comparison between original and optimized portfolios
   - Recommendations for portfolio improvements

## Submission Guidelines

1. This assessment must be submitted through GitHub Classroom:
   - Accept the assignment invitation link
   - Clone your assignment repository
   - Push your completed notebook and all generated files to your repository

2. Ensure your repository contains:
   - Your Jupyter notebook (.ipynb file) or Python modules (.py files) with class implementations
   - Generated HTML tear sheets
   - Any additional data files or visualizations
   - This README file

3. Submit a final commit before the deadline (Monday, May 5)

## Evaluation Criteria

Your submission will be evaluated based on:
- Code quality and organization
- Proper implementation of object-oriented programming principles
- Class design and structure
- Data handling and cleaning techniques
- Depth and accuracy of financial analysis
- Quality and clarity of visualizations
- Insights derived from the analysis
- QuantStats tear sheet completeness and analysis
- Optional: effectiveness of portfolio optimization
- Independent research and implementation of all components (no AI-generated code)

## Academic Integrity

This is an individual assessment meant to evaluate your personal skills in financial data analysis and Python programming. You are expected to:

1. Write all code yourself without using AI code generation tools
2. Conduct your own research on financial concepts and implementation techniques 
3. Properly cite any external resources used (documentation, articles, etc.)
4. Not share your code with classmates or use code from others

## Resources

- [yfinance Documentation](https://pypi.org/project/yfinance/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [QuantStats Documentation](https://github.com/ranaroussi/quantstats)
- [Modern Portfolio Theory](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)
- [Sharpe Ratio Explanation](https://www.investopedia.com/terms/s/sharperatio.asp) 
>>>>>>> 2f1401b258c2c7071a0578d1a052fda9ce8747e9
