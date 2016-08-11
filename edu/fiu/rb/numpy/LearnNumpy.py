__author__ = 'rbaral'
#Ref: http://cs231n.github.io/python-numpy-tutorial/#numpy
#Ref: Python for Data Analysis by Wes McKinney
import numpy as np
import timeit
import matplotlib.pyplot as plt

'''
array slices are views to the original array, so the
modification to the view will be reflected in the original array
'''
def slicing():
    # Create the following rank 2 array with shape (3, 4)
    # [[ 1  2  3  4]
    #  [ 5  6  7  8]
    #  [ 9 10 11 12]]
    a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

    # Use slicing to pull out the subarray consisting of the first 2 rows
    # and columns 1 and 2; b is the following array of shape (2, 2):
    # [[2 3]
    #  [6 7]]
    b = a[:2, 1:3]   #first parameter is for the rows, and second is for the columns
    print b
    # A slice of an array is a view into the same data, so modifying it
    # will modify the original array.
    print a[0, 1]   # Prints "2"
    b[0, 0] = 77    # b[0, 0] is the same piece of data as a[0, 1]
    print a[0, 1]   # Prints "77"

def indexing():
    a = np.array([1, 2, 3])  # Create a rank 1 array
    print type(a)            # Prints "<type 'numpy.ndarray'>"
    print a.shape            # Prints "(3,)"
    print a[0], a[1], a[2]   # Prints "1 2 3"
    a[0] = 5                 # Change an element of the array
    print a                  # Prints "[5, 2, 3]"

    b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
    print b.shape                     # Prints "(2, 3)"
    print b[0, 0], b[0, 1], b[1, 0]   # Prints "1 2 4"

def createArrays():
    a = np.zeros((2,2))  # Create an array of all zeros
    print a              # Prints "[[ 0.  0.]
                         #          [ 0.  0.]]"

    b = np.ones((1,2))   # Create an array of all ones
    print b              # Prints "[[ 1.  1.]]"

    #bb = b*7
    #print bb
    c = np.full((2,2), 7) # Create a constant array
    print c               # Prints "[[ 7.  7.]
                          #          [ 7.  7.]]"

    d = np.eye(2)        # Create a 2x2 identity matrix
    print d              # Prints "[[ 1.  0.]
                         #          [ 0.  1.]]"

    e = np.random.random((2,2)) # Create an array filled with random values
    print e                     # Might print "[[ 0.91940167  0.08143941]

'''
When you index into numpy arrays using slicing, the resulting array view will always
be a subarray of the original array. In contrast, integer array indexing allows you
to construct arbitrary arrays using the data from another array
'''
def intIndexing():
    a = np.array([[1,2], [3, 4], [5, 6]])

    # An example of integer array indexing.
    # The returned array will have shape (3,) and
    # the first list contains the list that we want to include
    # and the second list contains the index of elements on those lists
    print a[[0, 1, 2], [0, 1, 0]]  # Prints "[1 4 5]"
    #print a.shape
    # The above example of integer array indexing is equivalent to this:
    print np.array([a[0, 0], a[1, 1], a[2, 0]])  # Prints "[1 4 5]"

    # When using integer array indexing, you can reuse the same
    # element from the source array:
    print a[[0, 0], [1, 1]]  # Prints "[2 2]"

    # Equivalent to the previous integer array indexing example
    print np.array([a[0, 1], a[0, 1]])  # Prints "[2 2]"

'''
Boolean array indexing lets you pick out arbitrary elements of an array.
Frequently this type of indexing is used to select the elements of an array that satisfy some condition
'''
def boolArrayIndexing():
    a = np.array([[1,2], [3, 4], [5, 6]])

    bool_idx = (a > 2)  # Find the elements of a that are bigger than 2;
                        # this returns a numpy array of Booleans of the same
                        # shape as a, where each slot of bool_idx tells
                        # whether that element of a is > 2.

    print bool_idx      # Prints "[[False False]
                        #          [ True  True]
                        #          [ True  True]]"

    # We use boolean array indexing to construct a rank 1 array
    # consisting of the elements of a corresponding to the True values
    # of bool_idx
    print a[bool_idx]  # Prints "[3 4 5 6]"

    # We can do all of the above in a single concise statement:
    print a[a > 2]     # Prints "[3 4 5 6]"

'''
Basic mathematical functions operate elementwise on arrays,
and are available both as operator overloads and as functions in the numpy module
'''
def arrayMath():
    x = np.array([[1,2],[3,4]], dtype=np.float64)
    y = np.array([[5,6],[7,8]], dtype=np.float64)

    # Elementwise sum; both produce the array
    # [[ 6.0  8.0]
    #  [10.0 12.0]]
    print x + y
    print np.add(x, y)

    # Elementwise difference; both produce the array
    # [[-4.0 -4.0]
    #  [-4.0 -4.0]]
    print x - y
    print np.subtract(x, y)

    # Elementwise product; both produce the array
    # [[ 5.0 12.0]
    #  [21.0 32.0]]
    print x * y
    print np.multiply(x, y)

    # Elementwise division; both produce the array
    # [[ 0.2         0.33333333]
    #  [ 0.42857143  0.5       ]]
    print x / y
    print np.divide(x, y)

    # Elementwise square root; produces the array
    # [[ 1.          1.41421356]
    #  [ 1.73205081  2.        ]]
    print np.sqrt(x)

'''
We instead use the dot function to compute inner products of vectors,
to multiply a vector by a matrix, and to multiply matrices.
dot is available both as a function in the numpy module and as an instance method of array objects
'''
def innerProducts():
    x = np.array([[1,2],[3,4]])
    y = np.array([[5,6],[7,8]])

    v = np.array([9,10])
    w = np.array([11, 12])

    # Inner product of vectors; both produce 219
    print v.dot(w)
    print np.dot(v, w)

    # Matrix / vector product; both produce the rank 1 array [29 67]
    print x.dot(v)
    print np.dot(x, v)

    # Matrix / matrix product; both produce the rank 2 array
    # [[19 22]
    #  [43 50]]
    print x.dot(y) # its just a matrix multiplication
    print np.dot(x, y)


def arrayComputation():
    x = np.array([[1,2],[3,4]])

    print np.sum(x)  # Compute sum of all elements; prints "10"
    print np.sum(x, axis=0)  # Compute sum of each column; prints "[4 6]"
    print np.sum(x, axis=1)  # Compute sum of each row; prints "[3 7]"

'''
Broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes when performing arithmetic operations.
Frequently we have a smaller array and a larger array, and we want to use the smaller array multiple times to perform some operation on the larger array.
'''
def broadCasting():
    # We will add the vector v to each row of the matrix x,
    # storing the result in the matrix y
    x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    y = np.empty_like(x)   # Create an empty matrix with the same shape as x

    # Add the vector v to each row of the matrix x with an explicit loop
    for i in range(4):
        y[i, :] = x[i, :] + v

    # Now y is the following
    # [[ 2  2  4]
    #  [ 5  5  7]
    #  [ 8  8 10]
    #  [11 11 13]]
    print y
    '''
    Python could be slow. Note that adding the vector v to each row of the matrix x is equivalent to forming a matrix vv
    by stacking multiple copies of v vertically, then performing elementwise summation of x and vv. We could implement
    this approach like this:
    '''
    vv = np.tile(v, (4, 1))  # Stack 4 copies of v on top of each other
    print vv                 # Prints "[[1 0 1]
                             #          [1 0 1]
                             #          [1 0 1]
                             #          [1 0 1]]"
    y = x + vv  # Add x and vv elementwise
    print y  # Prints "[[ 2  2  4
             #          [ 5  5  7]
             #          [ 8  8 10]
             #          [11 11 13]]"
    '''
    Numpy broadcasting allows us to perform this computation without actually creating multiple copies of v.
    Consider this version, using broadcasting:
    '''
    # We will add the vector v to each row of the matrix x,
    # storing the result in the matrix y
    x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    y = x + v  # Add v to each row of x using broadcasting
    print y  # Prints "[[ 2  2  4]
             #          [ 5  5  7]
             #          [ 8  8 10]
             #          [11 11 13]]"


def outerProduct():
    # Compute outer product of vectors
    v = np.array([1,2,3])  # v has shape (3,)
    w = np.array([4,5])    # w has shape (2,)
    # To compute an outer product, we first reshape v to be a column
    # vector of shape (3, 1); we can then broadcast it against w to yield
    # an output of shape (3, 2), which is the outer product of v and w:
    # [[ 4  5]
    #  [ 8 10]
    #  [12 15]]

    print np.reshape(v, (3, 1)) * w

    # Add a vector to each row of a matrix
    x = np.array([[1,2,3], [4,5,6]])
    # x has shape (2, 3) and v has shape (3,) so they broadcast to (2, 3),
    # giving the following matrix:
    # [[2 4 6]
    #  [5 7 9]]
    print x + v

    # Add a vector to each column of a matrix
    # x has shape (2, 3) and w has shape (2,).
    # If we transpose x then it has shape (3, 2) and can be broadcast
    # against w to yield a result of shape (3, 2); transposing this result
    # yields the final result of shape (2, 3) which is the matrix x with
    # the vector w added to each column. Gives the following matrix:
    # [[ 5  6  7]
    #  [ 9 10 11]]
    print (x.T + w).T
    # Another solution is to reshape w to be a row vector of shape (2, 1);
    # we can then broadcast it directly against x to produce the same
    # output.
    print x + np.reshape(w, (2, 1))

    # Multiply a matrix by a constant:
    # x has shape (2, 3). Numpy treats scalars as arrays of shape ();
    # these can be broadcast together to shape (2, 3), producing the
    # following array:
    # [[ 2  4  6]
    #  [ 8 10 12]]
    print x * 2

'''
miscelleneous numpy functions
'''
def numpyMisc():
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
    arr = np.random.randn(5, 4) # normally-distributed data
    print arr.mean() # get the mean of all the elements
    print arr.mean(axis=1) # get the mean of elements on axis=1
    arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    arr.cumsum(0) # cumulative sum across axis =0
    arr.cumprod(1) # cumulative product acros axis =1
    arr = np.random.randn(5, 3)
    print arr
    arr.sort(1) # sort the array across axis =1
    print arr
    large_arr = np.random.randn(1000)
    large_arr.sort()
    print large_arr[int(0.05 * len(large_arr))] # 5% quantile
    # find unique elements in a list
    names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
    print np.unique(names)
    # check if elements of one array is present in another
    values = np.array([6, 0, 0, 3, 2, 5, 6])
    print np.in1d(values, [2, 3, 6]) # checks if the element of values are present in the given list and returns boolean array

'''
plot (x^2+y^2)^0.5
'''
def plotQuadratic():
    points = np.arange(-5, 5, 0.01) # 1000 equally spaced points
    # create a 2-D array from the combination of elements of the two 1-D arrays
    xs, ys = np.meshgrid(points, points)
    z = np.sqrt(xs ** 2 + ys ** 2)
    plt.imshow(z, cmap=plt.cm.gray)
    #plt.colorbar()
    plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
    plt.show()

'''
apply np.where for the conditional operator
'''
def cond():
    xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond = np.array([True, False, True, True, False])
    result = np.where(cond, xarr, yarr) # when True take the element from first array, else take the element from the second array
    print result


if __name__=="__main__":
    print "started"
    #slicing()
    #intIndexing()
    #boolArrayIndexing()
    #innerProducts()
    #arrayComputation()
    #broadCasting()
    #outerProduct()
    #plotQuadratic()
    #cond()



