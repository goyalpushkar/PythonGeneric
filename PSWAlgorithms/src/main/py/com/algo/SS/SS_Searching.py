'''
Created on Feb 4, 2020

@author: goyalpushkar
'''

if __name__ == '__main__':
    pass

def sequential_search( a_list, item):
    
    found = False
    for items in a_list:
        print("items - " + str(items))
        if items == item:
            found = True
            break
    
    return found

def ordered_sequential_search(a_list, item):
    found = False
    for items in a_list:
        print("items - " + str(items))
        if items == item:
            found = True
            break
        elif items > item:
            found = False
            break
    
    return found

def binary_search( a_list, item ):
    first = 0
    last = len(a_list) - 1
    found = False
    
    while first < last and not found:
        midpoint = first + ( ( last - first ) // 2 )
        print( a_list[midpoint] )
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
            
    return found        

def binary_search_rec( a_list, item ):
    
    if len(a_list) == 0:
        return False
    
    midpoint = len(a_list) // 2
    print( a_list[midpoint] )
    if a_list[midpoint] == item:
        return True
    else:
        if a_list[midpoint] < item:
            return binary_search_rec( a_list[ midpoint + 1: ], item)
        else:
            return binary_search_rec( a_list[ :midpoint ], item)
            
def mainSequentailSearch(ordered_yn): 
    if ordered_yn.upper() == 'N':
        test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0] 
        print("Check for 3 : " + str(sequential_search(test_list, 3))) 
        print("Check for 13 : " + str(sequential_search(test_list, 13)))
    else:
        test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42] 
        print("Check for 3 : " + str(ordered_sequential_search(test_list, 3))) 
        print("Check for 13 : " + str(ordered_sequential_search(test_list, 13)))
    
def mainBinarySearch(recursive_yn): 
    if recursive_yn.upper() == 'N':
        test_list = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
        print("Check for 3 : " + str(binary_search(test_list, 8)))
        print("Check for 13 : " + str(binary_search(test_list, 16)))
    else:
        test_list = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
        print("Check for 3 : " + str(binary_search_rec(test_list, 8)))
        print("Check for 13 : " + str(binary_search_rec(test_list, 16)))
    
    
def main():
    usrInput = 'P'
    while usrInput.upper() != 'Q':
        print("Run one of the following functions: ")
        print( "\t 1. Sequential Search" )
        print( "\t 2. Binary Search" )
        usrInput = raw_input("Enter Number for above programs or q to quit: ")
   
        if usrInput == '1':
            usrInput = raw_input("List is ordered or not, enter Y or N: ")
            mainSequentailSearch(usrInput)
        elif usrInput == '2':
            usrInput = raw_input("Recursive Call or not, enter Y or N: ")
            mainBinarySearch(usrInput)

main()