'''
Created on Feb 24, 2020

@author: goyalpushkar
'''

if __name__ == '__main__':
    pass

from random import randrange
from DS_BinaryHeap import *


def build_binary_heap():
    list = [randrange(1,200) for i in range(1,200)]
    buildHeap = BinaryHeap(200)
    buildHeap.build_heap(list)
    
    buildHeap.print_heap()
    #for elem in buildHeap.heap_list:
    #        print( elem )   #end=','
   
def build_sorted_heap(list, size):
    if not size:
        size = len(list)
    sortedHeap = BinaryHeap(size)
    print( 'Heap Size Limit - ' + str(sortedHeap.find_max_size()) )
    sortedHeap.build_sorted_heap(list)
    sortedHeap.print_heap()
    print( 'Heap Size - ' + str(sortedHeap.current_size) )
    #for elem in buildHeap.heap_list:
    #        print( elem )   #end=','
             
#Heapsort algorithm is developed using below 2 steps:
# Build Max/Min Heap using bototm up method - build_heap
# Repeatedly delete the largest/smallest remaining item - del_min without pop i loop
def heap_sort(list):
    sortedHeap = BinaryHeap(len(list))
    print( 'Heap Size Limit - ' + str(sortedHeap.find_max_size()) )
    sortedHeap.build_heap(list)
    sortedHeap.print_heap()
    print( 'Heap Size - ' + str(sortedHeap.current_size) )
    #listLength = len(list)
    while sortedHeap.current_size > 1: 
        sortedHeap.heap_list[1], sortedHeap.heap_list[sortedHeap.current_size] = sortedHeap.heap_list[sortedHeap.current_size], sortedHeap.heap_list[1]
        sortedHeap.current_size = sortedHeap.current_size - 1
        sortedHeap.perc_down(1)
        #listLength = listLength - 1
    
    sortedHeap.current_size = len(list)
    sortedHeap.print_heap()            
    
def main():
    
    
    userInput = 'P'
    while userInput != 'Q':
        print("Enter number for below programs")
        print("\t 1. Generate Heap from Random list of integers")
        print("\t 2. Binary Heap Sort")
        userInput = raw_input("Enter number corresponding to above function or Q to quit: ")
        
        if userInput.upper() == 'Q':
            break
        
        if userInput == '1':
            build_binary_heap()
        elif userInput == '2':
            userList = raw_input("Enter comma separated values for list: ")
            userListConverted = list( map(int, userList.split(",")) )
            size = raw_input("Do you wish to enter heap size then enter any number: ")
            if size == 'N' or size == 'n':
                heap_sort(userListConverted, None )
            else:
                build_sorted_heap(userListConverted, int(size) )
main()