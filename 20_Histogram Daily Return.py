"""Compute daily returns."""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base='C:\Users\Fahad\Desktop\Data'):
    return os.path.join(base, '{}.csv'.format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY2' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY2')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY2':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY2"])

    return df


def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_ret=df.pct_change(1)
    daily_ret.ix[0,:] = 0 
    return daily_ret
    # Note: Returned DataFrame must have the same number of rows

def compute_cumulative_returns(df):
    cum_ret = (1 + compute_daily_returns(df)).cumprod() - 1
    return cum_ret
    

def test_run():
    # Read data
    dates = pd.date_range('2012-01-01', '2012-12-31')  # one month only
    symbols = ['AAPL','SPY2']
    df = get_data(symbols, dates)
#    plot_data(df)

    
    

    
    # plot a histogram with mean, std dev
    # Compute daily returns
    dr = compute_daily_returns(df)
    #plot_data(dr, title="Daily returns", ylabel="Daily returns")
    dr['SPY2'].hist(bins=20, label='SPY') # bins default is 10
        
    mean = dr['SPY2'].mean()
    print 'mean=',mean
    stddev = dr['SPY2'].std()
    print 'Std Dev=',stddev
    plt.axvline(mean,color='w',linestyle='dashed',linewidth=2) # axis vertical
    plt.axvline(stddev,color='r',linestyle='dashed',linewidth=2)
    plt.axvline(-stddev,color='r',linestyle='dashed',linewidth=2)
    
#    w = white
    #plt.axvline(mean stddev,color='w',linestyle='dashed',linewidth=2)
    #color 
 #   r = red
    plt.show()    

if __name__ == "__main__":
    test_run()
	
