'''
Created on Mar 2, 2020

@author: goyalpushkar
'''

'''
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.
Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
Input:
finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:
5 is the missing number
'''




def missingElement( list1, list2 ):
    
    dictElem = {}
    missingElems= set()
    for elem in list1:
        if elem in dictElem:
            dictElem[elem] += 1
        else:
            dictElem[elem] = 1
    
    for elem in list2:
        if elem in dictElem:
            dictElem[elem] -= 1
        else:
            dictElem[elem] = 1
    
    for elem in dictElem:
        if dictElem[elem] != 0:
            missingElems.add(elem)
            
    print( "\t".join( map(str, list(missingElems)) ))
    return len(missingElems)

def missingElement1( list1, list2 ):
    number = 0
    for elem in list1:
        number += elem
    
    for elem in list2:
        number -= elem
        
    return number    
    
def main():
    noOfTests = raw_input("Enter number of test cases: ")
    for test in range( 1, int(noOfTests) + 1, 1 ):
        print( "-"*15)
        print("Test Case - " + str(test))
        noOfValues = raw_input("Enter number of elements in List 1: ")
        userList = list()
        for i in range( int(noOfValues) ):
            value = raw_input("Enter value: ")
            userList.append(int(value))
            
        noOfValues = raw_input("Enter number of elements in List 2: ")
        userList2 = list()
        for i in range( int(noOfValues) ):
            value = raw_input("Enter value: ")
            userList2.append(int(value))
        
        missed = missingElement1(userList, userList2)
        print( missed )
        
if __name__ == '__main__':
    main()