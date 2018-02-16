import pandas as pd

def test_run():
    df=pd.read_csv("C:\Users\Fahad\Desktop\Data\AAPL.csv")
    print df
    print df.head()
    print df.tail()
    print df[0:5]
    
if __name__=="__main__":
    test_run()