'''
Created on Mar 2, 2020

@author: goyalpushkar
'''
from numpy.testing.utils import print_assert_equal
from numpy.testing.utils import assert_equal
from oauthlib.oauth2.rfc6749.endpoints.base import catch_errors_and_unavailability

'''
Given an array of integers (positive and negative) find the largest continuous sum.
'''

#from nose.tools import assert

# 0,   1,   2,  3,   4,   5,  6
#-8,  -2,   7,  4,   5,   8, -1
#-8, -10,  -3,  1,   6
#           7, 11,  16,  24, 23
def continousSum(userList):
    
    current_sum = 0
    max_sum = 0
    startIndex = 0
    endIndex = 0
    newSum = 0
    for index in range(len(userList)):
        
        # if sign changes after sum then it reverting the direction of sum
        if ( current_sum < 0 and ( current_sum + userList[index] ) >= 0 ) or ( current_sum > 0 and ( current_sum + userList[index] ) <= 0 ):
            newSum = userList[index-1] + userList[index]
            current_sum += userList[index]
            
            if newSum > current_sum:
                startIndex = index - 1
                current_sum = newSum
            elif userList[index] > current_sum:
                startIndex = index
                current_sum = userList[index] 
        else:        
            current_sum += userList[index]
        
        if abs(max_sum) <= abs(current_sum):
            endIndex = index
            max_sum = current_sum
        
    return max_sum
    
def large_cont_sum(userlist):
    max_sum = current_sum = userlist[0]
    
    for elem in userlist[1:]:
        
        current_sum = max( current_sum+elem, elem)
        max_sum = max( current_sum, max_sum )
        
    return max_sum
    
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
            
        summed = continousSum(userList)
        print( summed )
        
def test():
    print_assert_equal("Test continousSum ", continousSum([1,2,-1,3,4,-1]),9 )
    print_assert_equal("Test continousSum ", continousSum([1,2,-1,3,4,10,10,-10,-1]),29 )
    print_assert_equal("Test continousSum ", continousSum([-1,1]),1 )
    
    #large_cont_sum does not work for below test case
    print_assert_equal("Test continousSum ", continousSum([-8,-2,2]), -10 )
    '''
    try:
        assert_equal(continousSum([1,2,-1,3,4,-1]),9,"Test continousSum ",True )
    except:
        print("Error Required")
    '''
    print("All test cases passed!!!")
    
if __name__ == '__main__':
    #main()
    test()