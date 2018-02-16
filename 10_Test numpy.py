import numpy as np
def test_run():
	#Empty Array
	print np.empty(5)
	print np.empty((5,4))
	print np.ones((5,4), dtype=np.int_)
#Generate an array full of random numbers from [0.0,1.0)
        print
        print'Generate an array full of random numbers from [0.0,1.0)'
	print np.random.rand(5,4)
#Generate an array from Gaussian Normal Dist. Mean=0 & Std. Dev. =1
	print
	print 'Generate an array from Gaussian Normal Dist. Mean=0 & Std. Dev. =1'
	print np.random.normal(size=(2,3))
	
#a single integer in [0,10)
        print 'single integer in [0,10)'
	print np.random.randint(10)
#same as above, specifying [low,High) explicitly
        print 'specifying [low,High) explicitly'
	print np.random.randint(0,10)
#5 random integers as 1D array
	print np.random.randint(0,10, size=5)
	print np.random.randint(0,10, size=(2,3))



	
if __name__=="__main__":
	test_run()

