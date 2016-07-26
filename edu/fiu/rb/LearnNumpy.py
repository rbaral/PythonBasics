__author__ = 'rbaral'
import numpy as np

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

if __name__=="__main__":
    slicing()