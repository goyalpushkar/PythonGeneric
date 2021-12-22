'''
Created on Mar 4, 2020

@author: goyalpushkar
'''
from TestClass import *

'''
Given a string, determine if it is comprised of all unique characters. For example, the string 'abcde' has all unique characters 
and should return True. The string 'aabcde' contains duplicate characters and should return false.
'''

def uniqueChar(userList):
    _uniqueCharacters = set()
    
    for elem in userList:
        if elem in _uniqueCharacters:
            return False
        else:
            _uniqueCharacters.add(elem)
            
    return True 
    
def unique_char(userList):
    return len(set(userList)) == len(userList)
    
def main():
    noOfTests = raw_input("Enter number of test cases: ")
    for test in range( 1, int(noOfTests) + 1, 1 ):
        print( "-"*15)
        print("Test Case - " + str(test))
        actual_string = raw_input("Enter String to check for Unique Characters: ")
        
        compressed_string = unique_char(actual_string)
        print( compressed_string )
        
def test():
    testObject = Testing()
    testObject.test(uniqueChar, "Test Unique Char ", "", True )
    testObject.test(uniqueChar, "Test Unique Char ", "goo", False )
    testObject.test(uniqueChar, "Test Unique Char ", "abcdefg", True )
    testObject.test(uniqueChar, "Test Unique Char ", "Pushkar", True )
    testObject.test(uniqueChar, "Test Unique Char ", "Duplicated Chars", False )
    
    '''
    try:
        assert_equal(stringCompression("Pushkar Goyal has open heart"),"heart open has Goyal Pushkar","Test sentenceReversal ",True )
    except:
        print("Error Required")
    '''
    print("All test cases passed!!!")
    

if __name__ == '__main__':
    main()
    test()