import pandas as pd
def test_run():
    start_date='2016-10-26'
    end_date='2016-11-09'
    dates=pd.date_range(start_date,end_date)
# Create an empty dataframe
    df1=pd.DataFrame(index=dates)

#Read SPY data in temp dataframe
    dfSPY=pd.read_csv("C:\Users\Fahad\Desktop\Data\SPY.csv")
#    dfSPY=pd.read_csv("C:\Users\Fahad\Desktop\Data\SPY.csv", index_col='Date', parse_dates=True, na_values='nan', usecols=['Date', 'Adj Close'])
    dfSPY=dfSPY.rename(columns={'Adj Close':'SPY'})

#Join two dataframe
    df1=df1.join(dfSPY)
    #df1=df1.join(dfSPY, how='inner')
    #df1=df1.dropna()    
    #print dfSPY
    print df1
    
    
if __name__ == "__main__":
    test_run()
    
    
