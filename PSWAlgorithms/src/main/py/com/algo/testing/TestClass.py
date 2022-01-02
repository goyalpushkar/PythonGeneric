'''
Created on Mar 4, 2020

@author: goyalpushkar
'''

from numpy.testing.utils import print_assert_equal

class Testing(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def test(self, functionName, messageName, passedValue, desiredValue):
        #print("Test " + functionName)
        print_assert_equal(messageName, functionName(passedValue), desiredValue )