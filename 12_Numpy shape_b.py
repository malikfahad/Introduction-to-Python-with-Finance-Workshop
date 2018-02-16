import numpy as np
def test_run():
	a=np.random.random((5,4))
	print a
	print a.shape
	print a.shape[0]
	print a.shape[1]
	print a.size
	print a.dtype
	
if __name__=='__main__':
	test_run()
