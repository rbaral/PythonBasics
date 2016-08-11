__author__ = 'rbaral'
#Ref: http://docs.scipy.org/doc/scipy/reference/tutorial/basic.html
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import linalg, optimize
from numpy import poly1d

'''
this function can be used to construct 1d ranges as a convenient substitute for arange.
It also allows the use of complex-numbers in the step-size to indicate the number of points
to place between the (inclusive) end-points. The real purpose of this function however is to
produce N, N-d arrays which provide coordinate arrays for an N-dimensional volume
'''
def mGridFunction():
    print np.mgrid[0:5,0:5]
    #use the complex numbers to indicate the step
    print np.mgrid[0:5:4j,0:5:4j]

def poly1dFunction():
    p = poly1d([3,4,5]) #This class accepts coefficients or polynomial roots to initialize a polynomial.
    print p
    print p*p
    print p.integ(k =6)
    print p.deriv()
    print p([4,5])

'''
 select is a vectorized form of the multiple if-statement. It allows rapid construction of a function which returns an array of results based on a list of conditions.
 Each element of the return array is taken from the array in a choicelist corresponding to the first condition in condlist that is true
'''
def selectFunction():
    x = np.r_[-2:3]
    print x
    print [x+2]
    print np.select([x > 3, x>=0], [0, x+2])


'''
perform the integration
'''
def integrateFunction():
    import scipy.integrate as integrate
    import scipy.special as special
    result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
    print result


if __name__=="__main__":
    print "started"
    #mGridFunction()
    #poly1dFunction()
    integrateFunction()
