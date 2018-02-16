
import numpy as np
def test_run():
	np.random.seed(693) #seed the random number generator
	a=np.random.randint(0,10, size=(5,4))
	print "Array: \n", a

#sum of all elements
	print "Sum of all elements:", a.sum()
# Iterate over rows, to compute sum of each column
	print "sum of each column: \n", a.sum(axis=0)
# Iterate over columns, to compute sum of each row
	print "sum of each row: \n", a.sum(axis=1)
	
	print 'Minimum of each column: \n', a.min(axis=0)
	print 'Maximum of each row: \n', a.max(axis=1)
	print 'Mean of all elements: \n', a.mean()

	

if __name__=='__main__':
	test_run()

