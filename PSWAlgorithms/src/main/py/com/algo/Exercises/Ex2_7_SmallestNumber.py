'''
Created on Jan 31, 2020

@author: goyalpushkar
'''
from pprint import pprint
import sys
from os import path
#from ..SS.SS_Sorting import *

'''
if __name__ == '__main__':
    if __package__ is None:
        #import src.main.py.com.algo.SS.SS_Sorting as ssSort
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname(path.abspath(__file__)) ) )
        from SS.SS_Sorting import *
    else:
        from ..SS.SS_Sorting import merge_sort_woutslicing
'''

#4 5 2 10 9 8 3 6
#2 3 4 5 6 8 9 10 

#from SS.__main__ import *
#from SS.SS_Sorting import *

#from SS.SS_Sorting import *
#src.main.py.com.algo.SS
#Given a list of numbers in random order write a linear time algorithm to find the kth smallest number
# in the list. Explain why your algorithm is linear.
def kthsmallestNumber( listOfNumbers, k ):
    print(listOfNumbers)
    #Sort the list of Numbers 
    #sortedList = merge_sort_woutslicing(listOfNumbers)
    #Return the element at position k+1
    #print(sortedList)
    #print( sortedList[k-1] )

def mainKth():
    userList = input("Enter comma separated values: ")
    if userList == 'Q' or userList == 'q':
        return
    
    intList = list(map( int, userList.split(",")))
    element = raw_input("Enter kth value : ")
    kthsmallestNumber(intList, int(element) )
    
#text = "print(f'{__name__}, __file__: {__file__}, __package__: {repr(__package__)}')"
if __name__ == '__main__':
    #pprint.print("Name" + "File" + "Package")
    print(  {__name__}, {__file__},  {repr(__package__)} )
    #print( path.dirname(path.abspath(__file__) ) )
    #print( sys.path )
    for value in sys.modules:
        print(value)
    mainKth()