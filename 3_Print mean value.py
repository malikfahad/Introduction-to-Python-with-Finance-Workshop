import pandas as pd
def get_mean_value(symbol):
    df=pd.read_csv("C:\Users\Fahad\Desktop\Data\{}.csv".format(symbol))
    return df['Close'].mean()

def test_run():
    for symbol in ['AAPL','IBM']:
        print 'Mean Close Value'
        print symbol, get_mean_value(symbol)
    
if __name__=="__main__":
    test_run()
    
