__author__ = 'rbaral'

from pandas import Series, DataFrame
import pandas as pd

'''
some basic features of Series DataStructure
'''
def testSeriesDatastruct():
    obj = Series([4, 7, -5, 3])
    #print obj
    obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
    #print obj2
    #print 'b' in obj2
    states = ['California', 'Ohio', 'Oregon', 'Texas']
    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
    obj3 = Series(sdata)
    obj4 = Series(sdata, index=states)
    #print obj4
    # automatic alignment of data
    obj5 = obj3+obj4
    #print obj5
    #alter the index in place
    obj5.index = ['Bob', 'Steve', 'Jeff', 'Ryan', 'Raj']
    #print obj5

'''
some basic features of DataFrame DataStructure
'''
def testDataFrame():
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = DataFrame(data)
    print frame



if __name__=="__main__":
    #testSeriesDatastruct()
    testDataFrame()