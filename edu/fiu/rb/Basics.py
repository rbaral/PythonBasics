__author__ = 'rbaral'
import os
import glob
import sys
import pickle

def printFilesInDir():
    for dirpath, dirnames, filenames in os.walk(os.curdir):
        for fp in filenames:
            print os.path.abspath(fp)

def testOSCommand():
    #print os.system('ls ../ -al')
    print os.environ.keys()
    #printFilesInDir()

'''
The glob module provides convenient file pattern matching
'''
def testGlob():
    print glob.glob('*.py')

'''
system related functions
'''
def testSys():
    print sys.platform
    print sys.version
    print sys.prefix
    #List of command line arguments passed to a Python script
    print sys.argv
    print sys.path

'''
Useful to store arbitrary objects to a file. Not safe or fast!
'''
def testPickle():
    l = [1, None, 'Stan1']
    m = [1, None, 'Stan2']
    pickle.dump(l, file('test.pkl', 'a'))
    pickle.dump(m, file('test.pkl', 'a'))
    print pickle.load(file('test.pkl'))


def testExcepRaise(val):
    if val<10:
        raise StopIteration
    return

def testExcepHandling():
    while True:
        try:
            x = int(raw_input("Please enter a number:"))
            testExcepRaise(x)
            break
        except StopIteration:
            print "small number"
            break
            #raise "Stop Iteration"
        except ValueError, e:
            print("That was not a valid number, Try again")
            #raise e
        finally:
            print "inside finally"

if __name__=="__main__":
    #testPickle()
    #testOSCommand()
    #testGlob()
    #testSys()
    testExcepHandling()

