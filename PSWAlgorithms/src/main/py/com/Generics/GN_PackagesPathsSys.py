'''
Created on Feb 27, 2020

@author: goyalpushkar
'''
import sys
from os import path

#ImportError: No module named SS.SS_Sorting - wth SS.SS_Sorting
#ValueError: Attempted relative import in non-package - with .SS.SS_Sorting
#from .SS.SS_Sorting import *
#from ..SS.SS_Sorting import *
from GN_Email import *

if __name__ == '__main__':
    print(  {__name__}, {__file__},  {repr(__package__)} )
    #print(SS.__path__)
    #print( path.dirname(path.abspath(__file__) ) )
    #print( sys.path )
    sys.path.append( path.dirname( path.dirname(path.abspath(__file__)) ) )
    from SS.SS_Sorting import *
    #print( path.dirname( path.dirname(path.abspath(__file__)) ) )
    
    print( "-"*15)
    print("Modules")
    for value in sys.modules:
        print(value)
    
    print( "-"*15)  
    print("Meta Path")  
    for value in sys.meta_path:
        print(value)
        
    print( "-"*15)
    print("Path")  
    #Available paths without above append
    #/Users/goyalpushkar/Library/Mobile Documents/com~apple~CloudDocs/Documents/STSworkspace/WarehouseConnect/PSWAlgorithms/src/main/py/com/algo/Generics
    #/Users/goyalpushkar/Library/Mobile Documents/com~apple~CloudDocs/Documents/STSworkspace/WarehouseConnect/PSWAlgorithms
    #Available paths after above append
    #/Users/goyalpushkar/Library/Mobile Documents/com~apple~CloudDocs/Documents/STSworkspace/WarehouseConnect/PSWAlgorithms/src/main/py/com/algo
    
    #https://docs.python.org/3/reference/import.html#__package__ - 5.4.5. module.__path__
    for value in sys.path:
        print(value)