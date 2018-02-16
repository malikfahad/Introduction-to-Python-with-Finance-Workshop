import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def path_symbol(symbol, base='C:\Users\Fahad\Desktop\Data'):
    return os.path.join(base, '{}.csv'.format(str(symbol)))
    
def get_data(dates, symbols):
    df=pd.DataFrame(index=dates)
    for symbol in symbols:
        df1=pd.read_csv(path_symbol(symbol), index_col='Date', usecols=['Date', 'Adj Close'], na_values='nan', parse_dates=True)
        df1=df1.rename(columns={'Adj Close':symbol})
        df=df.join(df1)
        df=df.dropna()
    return df
def normalize(df):
    return df/df.ix[0,:]

def plot_data(df,title='Stock Prices'):
    #df=normalize(df)
    ax=df.plot(title=title,fontsize=2)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')
    plot.show()
    
def test_run():
    # Read Data
    dates= pd.date_range('2016-10-26', '2016-11-08')
    symbols=['SPY']
    df=get_data(dates, symbols)
    #Plot SPY data, retain matplotlib axis object
    ax = df['SPY'].plot(title="SPY rolling mean", label ='SPY')
    #Compute rolling mean using a 3 day window (usually 20)
    rm_SPY=pd.rolling_mean(df['SPY'], window=3)
    # Add rolling mean to same plot
    rm_SPY.plot(label='Rolling Mean', ax=ax)
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()
    
if __name__ == "__main__":
    test_run()
    
    
