'''
Created on Mar 2, 2020

@author: goyalpushkar
'''

import ctypes
import sys

class DynamicArray(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
        
    def __len__(self):
        print("Get Size of ")
        print( sys.getsizeof(self.A) )
        print("Capactiy ")
        print( self.capacity )
        return self.n
    
    def __getitem__(self, index):
        if not 0 <= index < self.n:
            return IndexError( str(index) + " is out of bound")
        
        return self.A[index] 
    
    def append(self, elem):
        
        if self.n == self.capacity:
            self._resize( 2 * self.capacity )
            
        self.A[self.n] = elem
        self.n +=1
        
    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        
        for k in range(self.n):
            B[k] = self.A[k]
            
        self.A = B
        self.capacity = new_cap
        
    def make_array(self, new_cap):
        return ( new_cap * ctypes.py_object )()