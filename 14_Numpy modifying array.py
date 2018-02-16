import numpy as np

def test_run():
    a=np.random.rand(5,4)
    print "Array \n", a
    
    print 'Select Columns 0, 2 with all rows \n', a[:,0:3:2]
    
    a[:,3]=[1,2,3,4,5]
    print 'Modified by replacing a columns with list \n', a
    
    

if __name__=='__main__':
    test_run()
    
    