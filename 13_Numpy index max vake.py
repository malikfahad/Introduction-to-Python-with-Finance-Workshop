import numpy as np


def get_max_index(a):
    return np.argmax(a,axis=None)


def test_run():
    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    print "Array:", a
    
    # Find the maximum and its index in array
    print "Maximum value:", a.max()
    print "Index of max.:", get_max_index(a)


if __name__ == "__main__":
    test_run()
