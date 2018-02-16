import os
import pandas as pd
import matplotlib.pyplot as plot

def path_to_symbol(symbol, base='C:\Users\Fahad\Desktop\Data'):
    return os.path.join(base, '{}.csv'.format(str(symbol)))

def get_data(dates,symbols):
    df=pd.DataFrame(index=dates)
    for symbol in symbols:
        df1=pd.read_csv(path_to_symbol(symbol), index_col='Date', usecols=['Date', 'Adj Close'], na_values='nan', parse_dates=True)
        df1=df1.rename(columns={'Adj Close':symbol})
        df=df.join(df1)
        df=df.dropna()
    return df

def normalize(df):
    return df/df.ix[0,:]

def plot_data(df,title='Stock Prices'):
    df=normalize(df)
    ax=df.plot(title=title, fontsize=2)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plot.show()

def plot_selected(df,start_date,end_date,columns):
    df=(df.ix[start_date:end_date, columns])
    plot_data(df,title='Selected Stock Prices')

def test_run():
    dates= pd.date_range('2012-01-26', '2012-11-08')
    symbols=['XOM', 'IBM', 'AAPL', 'SPY2']
    df=get_data(dates, symbols)
    plot_data(df,title='Stock Prices')
    plot_selected(df,'2012-10-27', '2016-12-04', ['AAPL', 'SPY2'])
    
if __name__ == "__main__":
    test_run()
    
