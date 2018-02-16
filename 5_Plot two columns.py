import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df=pd.read_csv("C:\Users\Fahad\Desktop\Data\AAPL1.csv")
    df[['Adj Close','Close']].plot()
    plt.show()
    plt.xlabel('No. of Days')
    plt.ylabel('Price')
    plt.title('Plotting Adjusted Close')
    
    
if __name__=="__main__":
    test_run()
    
