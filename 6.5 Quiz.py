import os
import pandas as pd

def symbol_to_path(symbol, base='C:\Users\Fahad\Desktop\Data'):
    return os.path.join(base, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY2')

    for symbol in symbols:
	df_temp=pd.read_csv(symbol_to_path(symbol) ,index_col='Date', parse_dates=True, na_values='nan', usecols=['Date', 'Adj Close'])
	df_temp=df_temp.rename(columns={'Adj Close': symbol})
	df=df.join(df_temp)
#	df=df.dropna()
        if symbol == 'SPY2':
	    df=df.dropna(subset=["SPY2"])
    
    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2012-10-26', '2012-11-08')

    # Choose stock symbols to read
    symbols = ['IBM', 'AAPL']
    
    # Get stock data
    df = get_data(symbols, dates)
    print df
    
    
    


if __name__ == "__main__":
    test_run()
