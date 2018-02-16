import pandas as pd
def test_run():
    start_date='2016-10-26'
    end_date='2016-11-09'
    dates=pd.date_range(start_date,end_date)
    print dates
    #print dates[0]
    df1=pd.DataFrame(index=dates)
    #print df1
if __name__ == "__main__":
    test_run()
    
    
