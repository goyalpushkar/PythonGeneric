'''
Created on Mar 2, 2020

@author: goyalpushkar
'''

from DS_DynamicArray import *

def main():
    da = DynamicArray()
    
    print( da.__len__() )
    da.append(1)
    da.append(2)
    
    print( da[0] )
    print( da[3] )
    
    da.append(3)
    da.append(4)
    da.append(5)
    print( da.__len__() )
    
    
if __name__ == '__main__':
    main()