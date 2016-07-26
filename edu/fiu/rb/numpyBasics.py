__author__ = 'rbaral'
import numpy as np
import timeit

def testNumpy():
    a = np.array([0,1,2,3])
    print a
    #print timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print a.ndim,a.shape
    b = np.array([[0, 1, 2], [3, 4, 5]])# 2 x 3 array
    print b.ndim,b.shape
    c = np.array([[[1,2], [2,3]], [[3,4], [4,5]]])
    print c.ndim,c.shape
    d= np.arange(10,100,10)# start, end (exclusive), step
    #print d[1]
    #using number of points
    d = np.linspace(0, 1, 6) # start, end, number of items
    print d
    d = np.linspace(0, 1, 5, endpoint=False)# start, end, number of items excluding the end point
    print d
    a = np.ones((3, 3)) # reminder: (3, 3) is a tuple
    print a
    print np.zeros((2,2))
    print np.eye(3)#3*3 matrix with diagonal 1s and other zeros
    print np.diag(np.array([1,2,3]))
    np.random.seed(1234)#setting the random seed
    print np.random.randint(1,100,5)#find random number (low,high,size)
    c = np.array([1, 2, 3], dtype=int)#numpy auto detects the type from the data though
    c[0] = 2.5#loses precision because c only holds int type data
    print c
    d = np.array([1+2j, 3+4j, 5+6*1j])#array with the complex numbers
    print d.dtype

if __name__=="__main__":
    testNumpy()