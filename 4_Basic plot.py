import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df=pd.read_csv("C:\Users\Fahad\Desktop\Data\AAPL.csv")
    df['Adj Close'].plot()
    plt.show()
    
    
if __name__=='__main__':
    test_run()