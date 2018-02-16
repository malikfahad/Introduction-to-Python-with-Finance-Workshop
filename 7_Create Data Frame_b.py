import pandas as pd

def test_run():
    start_date='2016-10-26'
    end_date='2016-11-09'
    dates=pd.date_range(start_date,end_date)
    df1=pd.DataFrame(index=dates)
    symbols = ['AAPL', 'IBM', 'GOOG','SPY']
    for symbol in symbols:
        df_temp=pd.read_csv("C:\Users\Fahad\Desktop\Data\{}.csv".format(symbol),index_col='Date', parse_dates=True, na_values='nan', usecols=['Date', 'Adj Close'])
        df_temp=df_temp.rename(columns={'Adj Close':symbol})
        df1=df1.join(df_temp)
        df1=df1.dropna()
        
    
    
    print df1
    
    
if __name__ == "__main__":
    test_run()
    
    
