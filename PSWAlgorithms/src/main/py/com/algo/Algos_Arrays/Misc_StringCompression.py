'''
Created on Mar 4, 2020

@author: goyalpushkar
'''
from numpy.testing.utils import print_assert_equal
from TestClass import *

'''
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. 
For this problem, you can falsely "compress" strings of single or double letters. 
For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
'''

def stringCompression(usrString):
    
    compressedString = ""
    dictCount = {}
    prevElem = usrString[0]
    for elem in usrString:
        if elem in dictCount:
            dictCount[elem] += 1
        else:
            dictCount[elem] = 1
            
        if elem != prevElem:
            compressedString = compressedString + prevElem + str(dictCount[prevElem])
        
        prevElem = elem

    #Add last element
    compressedString = compressedString + prevElem + str(dictCount[prevElem])
    
    return compressedString

#Without dictionary
def string_compression(usrString):
    
    compressedString = ""
    count = 1
    for index in range(1, len(usrString)):
        if usrString[index] == usrString[index-1]:
            count += 1
        else:
            compressedString = compressedString + usrString[index-1] + str(count)
            count = 1
            
        
    #Add last element
    compressedString = compressedString + usrString[len(usrString)-1] + str(count)
    
    return compressedString

def main():
    noOfTests = raw_input("Enter number of test cases: ")
    for test in range( 1, int(noOfTests) + 1, 1 ):
        print( "-"*15)
        print("Test Case - " + str(test))
        actual_string = raw_input("Enter String for reversal: ")
        
        compressed_string = string_compression(actual_string)
        print( compressed_string )
        
def test():
    testObject = Testing()
    testObject.test(stringCompression, "Test String Compression ", "AAAABBBBCCCCCDDEEEE", "A4B4C5D2E4" )
    testObject.test(stringCompression, "Test String Compression ", "AAB", "A2B1" )
    testObject.test(stringCompression, "Test String Compression ", "AAAaaa", "A3a3" )
    testObject.test(stringCompression, "Test String Compression ", "AAABCCDDDDD", "A3B1C2D5" )
    testObject.test(stringCompression, "Test String Compression ", "This is the best", "T1h1i1s1 1i2s2 2t1h2e1 3b1e2s3t2" )
    
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