'''
Created on Mar 4, 2020

@author: goyalpushkar
'''
from numpy.testing.utils import print_assert_equal

'''
Given a string of words, reverse all the words. For example:
Given:
'This is the best'

Return:
'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
'  space here'  and 'space here      '

both become:
'here space'
'''

def sentence_reversal(userString):

    finalString = ""
    splittedString = userString.split()
    for index in range( len(splittedString), 0, -1 ):
        
        if index == len(splittedString):
            finalString = finalString + (splittedString[index-1])
        else:
            finalString = finalString + " " + (splittedString[index-1])
        
    return finalString

def sentenceReversal(userString):
    
    return " ".join(reversed(userString.split()))
    
def main():
    noOfTests = raw_input("Enter number of test cases: ")
    for test in range( 1, int(noOfTests) + 1, 1 ):
        print( "-"*15)
        print("Test Case - " + str(test))
        actual_string = raw_input("Enter String for reversal: ")
        
        reverse_string = sentence_reversal(actual_string)
        print( reverse_string )
        
def test():
    print_assert_equal("Test String Reversal ", sentenceReversal("This is the best"), "best the is This" )
    print_assert_equal("Test String Reversal ", sentenceReversal("  space here"), "here space" )
    print_assert_equal("Test String Reversal ", sentenceReversal("space here    "), "here space" )
    print_assert_equal("Test String Reversal ", sentenceReversal("Pushkar Goyal has open heart"), "heart open has Goyal Pushkar" )
    
    '''
    try:
        assert_equal(sentenceReversal("Pushkar Goyal has open heart"),"heart open has Goyal Pushkar","Test sentenceReversal ",True )
    except:
        print("Error Required")
    '''
    print("All test cases passed!!!")
    
if __name__ == '__main__':
    main()
    test()