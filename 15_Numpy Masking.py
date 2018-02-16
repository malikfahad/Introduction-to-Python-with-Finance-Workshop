import numpy as np

def test_run():
    a=np.random.rand(5)
    print "Array \n", a
    
    indices=np.array([1,1,2,3])
    print a[indices]

    b=np.array([(20,25,10,23,26,32,10,5,0),(0,2,50,20,0,10,28,5,0)])
    mean=b.mean()
    print b
    print
    #masking
    print 'Masking b[b<mean]=mean \n'
    b[b<mean]=mean
    print b
    

if __name__=='__main__':
    test_run()
    
    