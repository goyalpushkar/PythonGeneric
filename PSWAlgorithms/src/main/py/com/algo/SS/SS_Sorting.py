'''
Created on Feb 8, 2020

@author: goyalpushkar
'''

#__package__ = 'SS.SS_Sorting'
#__name__ = '__mainSS__'

#if __package__ == 'SS':
#    pass

#_userList = list()

def initialize_list( userList ):
    _userList = list()
    for values in userList.split(","):
        _userList.append( int(values.strip()) )
    
    return _userList
    #print( "Length of List - " + str(len(_userList)) )
    
##Multiple Exchanges will take place in each pass
#20, 30, 40, 90, 50, 60, 70, 80, 100, 110
# O(n^2)
def bubble_sort(a_list):
    print("-" * 4 + "Bubble Sort Selected" + "-" * 4)
    
    iindex = len(a_list) - 1
    exchange = True
    while iindex > 0 and exchange:
        print( "Pass No - " + str(len(a_list) - iindex) + " :iindex - " + str(iindex) )
        exchange = False
        for jindex in range(iindex):
            if a_list[jindex] > a_list[jindex+1]:
                exchange = True
                a_list[jindex], a_list[jindex+1] = a_list[jindex+1], a_list[jindex]

        print(a_list)
        iindex = iindex - 1
  
##One Exchange will take place in each pass   
#54, 26, 93, 17, 77, 31, 44, 55, 20   
# O(n^2)
def selection_sort(a_list):
    print("-" * 4 + "Selection Sort Selected" + "-" * 4)
    
    iindex = len(a_list) - 1
    while iindex > 0:
        print( "Pass No - " + str(len(a_list) - iindex) + " :iindex - " + str(iindex) )
        position = 0
        for jindex in range(1, iindex+1, 1):
            if a_list[position] < a_list[jindex]:
                position = jindex
                
        a_list[iindex], a_list[position] = a_list[position], a_list[iindex]
        print(a_list)
        iindex = iindex - 1
    
##Shifting takes place instead of exchanging. In general, a shift operation requires approximately a third of the processing
# work of an exchange since only one assignment is performed
#54, 26, 93, 17, 77, 31, 44, 55, 20   
# O(n^2)
def insertion_sort(a_list):
    print("-" * 4 + "Insertion Sort Selected" + "-" * 4)
    for iindex in range(1, len(a_list) ):
        print("Pass No - " + str(iindex) + " :iindex - ", a_list[iindex] )
        value = a_list[iindex]
        stop = False
        jindex = iindex - 1
        while jindex >= 0 and not stop:
            if a_list[jindex] > value:
                a_list[jindex+1] = a_list[jindex]
                jindex = jindex - 1
            else:
                stop = True
            
        a_list[jindex+1] = value
        print(a_list)   

#A general analysis of the shell sort tends to fall somewhere between O(n) and O(n^2)
#By changing the increment, for example using 2^k - 1 (1, 3, 7, 15, 31, and so on), a shell sort can perform at O(n^3/2 )
#54, 26, 93, 17, 77, 31, 44, 55, 20
#Between O(n) and O(n^2)
#There are different ways to shell sort 
#        Power of 2 - 1, 2, 4, 8, 16, 32.... Not a good way
#        Power of 2 minus 1 -  1, 3, 7, 15, 31.... May be
#        3x + 1 - 1, 4, 13, 40, 121, 364..... Easy to Compute x = len(a_list) / 3
#        Sedgewick - 1, 5, 19, 41, 109, 209, 505, 929, 2161, 3905.... 
def shell_sort(a_list):
    print("-" * 4 + "Shell Sort Selected" + "-" * 4)
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
            
        print( "After increments of size - " + str(sublist_count) + ". The list is - " + "\n" )
        print( a_list )
        sublist_count = sublist_count // 2
    
#Same as insertion sort but takes gap as parameter
def gap_insertion_sort(a_list, start, gap):
    for iindex in range(start+gap, len(a_list), gap ):
        #print( "Pass No - " + str(iindex) + " :iindex - " + str(iindex) )
        value = a_list[iindex]
        jindex = iindex
        while jindex >= gap and a_list[jindex-gap] > value:
                a_list[jindex] = a_list[jindex-gap]
                jindex = jindex - gap
            
        a_list[jindex] = value
        #print(a_list) 
    
#Merge sort takes extra space to hold the 2 halves as they are extracted using slicing operation
#The result of this analysis is that log n splits, each of which costs n for a total of n log n operations.
#A merge sort is an O(n log n ) algorithm.
#Slicing Operation takes O(k). where k is the size of the slice. In order to guarantee that merge_sort will be O(n log n) we will need to remove the slice operator
#21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40
def merge_sort(a_list):
    
    print( "Splitting - " )
    print(a_list)
    if len(a_list) > 1:
        
        mid = len(a_list) // 2
        left_half = a_list[ :mid]
        right_half = a_list[mid: ]
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
        
            k = k + 1
        
        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1
    
        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    
    print("Merging - " )
    print(a_list)
    
def split(a_list, copy_list, start, end):
    #print( "Splitting - " )
    #print(a_list)
    #print(copy_list)
    
    '''
    Improvement1
    if end <= start + CUTOFF - 1:
        Insertion.sort(a_list, start, end)
        return
    '''
    if end <= start:
        return
    else:
        #if len(a_list) > 1:
        mid = start + ( end - start ) // 2
        split(a_list, copy_list, start, mid)           #Improvement 3 interchanged lists
        split(a_list, copy_list, mid+1, end)           #Improvement 3 interchanged lists
        '''
        Improvement 2
        '''
        if a_list[mid+1] > a_list[mid]:                 #Improvement 3 interchanged lists
            return 
        merge(a_list, copy_list, start, mid, end)
            
def merge(a_list, copy_list, start, mid, end):
    #print( "\n start - " + str(start) + " :mid - " + str(mid) + " :end - " + str(end) )
    
    '''
    Improvement 3
    '''
    for k in range(start, end+1):
        copy_list[k] = a_list[k]
       
    #print(a_list)
    #print(copy_list)
    
    i = start
    j = mid + 1
    for k in range(start, end+1, 1):
        if i > mid:
            a_list[k] = copy_list[j]   #Improvement 3  a_list  copy_list
            j = j + 1
        elif j > end:
            a_list[k] = copy_list[i]   #Improvement 3  a_list  copy_list
            i = i + 1
        elif copy_list[i] > copy_list[j]:    #Improvement 3  a_list  copy_list
            a_list[k] = copy_list[j]   #Improvement 3  a_list  copy_list 
            j = j + 1
        else:
            a_list[k] = copy_list[i]  #Improvement 3  a_list  copy_list
            i = i + 1
    
    #print( "Merging - " )
    #print(a_list)
    #print(copy_list)
    #print("\n")
    #return a_list
    
## Merge Sort Improvements
'''
1. Use insertion sort for small subarrays. CUTOFF = 7
    Mergesort has too much overhead for tiny subarrays. Cutoff to insertion sort for ~~ 7 items
2. Stop if already sorted.
    Is biggest item in first half <= smallest item in second half? Helps for partially-ordered arrays
3. Eliminate the copy to the auxiliary array. Save time (but not space)
 by switching the role of the input and auxiliary array in each recursive call
'''
def merge_sort_woutslicing(a_list):
    
    #Below modification is done to avoid slicing
    copy_list = [None] * len(a_list)
    split( a_list, copy_list, 0, len(a_list)-1)
    #print(a_list)
    #print(copy_list)
    return a_list

def quick_sort_helper( a_list, start, end ):
    if start < end:
        split_position = partition(a_list, start, end)
    
        quick_sort_helper( a_list, start, split_position-1 )
        quick_sort_helper( a_list, split_position+1, end )
        
def partition(a_list, start, end):
    pivot_value = a_list[start]
    left_marker = start+1
    right_marker = end
    
    print("\n pivot_value - " + str(pivot_value) )
    done = True
    while done:
        while left_marker <= right_marker and a_list[left_marker] <= pivot_value:
            left_marker = left_marker + 1
            
        while left_marker <= right_marker and a_list[right_marker] >= pivot_value:
            right_marker = right_marker - 1
          
        #Exchange only if left_marker <= right_marker otherwise exit
        if right_marker < left_marker:
            done = False
        else:   
            a_list[left_marker], a_list[right_marker] = a_list[right_marker], a_list[left_marker]
        
    a_list[start], a_list[right_marker] = a_list[right_marker], a_list[start]
    
    print(a_list)
    print("split_position - " + str(right_marker))
    return right_marker
    
# In the worst case, the split points may not be in the middle and can be very skewed to the left or the right, 
#leaving a very uneven division. The result is an O(n^2) sort with all of the overhead that recursion requires.
# O(n log n). In addition, there is no need for additional memory as in the merge sort process.
#54, 26, 93, 17, 77, 31, 44, 55, 20
#14, 17, 13, 15, 19, 10, 3, 16, 9, 12
# Other ways to check pivot value = median of three
# small arrays - middle entry
# medium arrays - median of 3
# large arrays - Turkey's ninther
#              - Median of Median of 3 samples, each of 3 enteries. Pick 9 random elements, make 3 groups with 3 elements each.
#                  and get median of each group and then get median of final 3 elements. Use it as pivot value
#              - Uses at most 12 compares
def quick_sort(a_list):
    print("-" * 4 + "Quick Sort Selected" + "-" * 4)
    print(a_list)
    quick_sort_helper( a_list, 0, len(a_list) - 1 )
    
    print(a_list)
    
def main():
    usrInput = 'P'
    while usrInput.upper() != 'Q':
        print("Run one of the following functions: ")
        print( "\t 1. Bubble Sort" )
        print( "\t 2. Selection Sort" )
        print( "\t 3. Insertion Sort" )
        print( "\t 4. Shell Sort" )
        print( "\t 5. Merge Sort" )
        print( "\t 6. Bottom Up Merge Sort" )
        print( "\t 7. Quick Sort" )
        print( "\t 8. Binary Heap Sort" )
        #A bubble sort, a selection sort, and an insertion sort are O(n^2) algorithms.
        #A shell sort improves on the insertion sort by sorting incremental sublists. It falls between O(n) and O(n^2)
        #A merge sort is O(nlog n), but requires additional space for the merging process.
        #A quick sort is O(nlog  n), but may degrade to O(n^2) if the split points are not near the middle of the list. It does not require additional space
        usrInput = input("Enter Number for above programs or q to quit: ")
        if usrInput.upper()== 'Q':
            break
        
        userListP = input("Enter comma separated values to sort: ")
        _userList = initialize_list(userListP)
        print( "Length of List - " + str(len(_userList)) )
        
        if usrInput == '1':
            bubble_sort(_userList)
        elif usrInput == '2':
            selection_sort(_userList)
        elif usrInput == '3':
            insertion_sort(_userList)
        elif usrInput == '4':
            shell_sort(_userList)
        elif usrInput == '5':
            slicing = input("Merge Sort using Slicing (S) or without Slicing (WOS): ")
            print("-" * 4 + "Merge Sort Selected" + "-" * 4)
            if slicing.upper() == 'S':
                merge_sort(_userList)
            else:
                merge_sort_woutslicing(_userList)
        elif usrInput == '6':
            merge_sort(_userList)
        elif usrInput == '7':
            quick_sort(_userList)
        elif usrInput == '8':
            selection_sort(_userList)
       
    if __name__ == '__main__' and __package__ is None:
        __package__ = "SS"
        print(  {__name__}, {__file__},  {repr(__package__)} )       
        #print( "name: " + {__name__}, "__file__ : " + {__file__}, "__package__: " + {repr(__package__)} )      

main()
