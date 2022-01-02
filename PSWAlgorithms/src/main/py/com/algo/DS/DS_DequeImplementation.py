'''
Created on Jan 29, 2020

@author: goyalpushkar
'''

from Deque import Deque 
if __name__ == '__main__':
    pass

def main( program ):
    if program.upper() == 'PALINDROME_CHECK':
        mainPalindrome()
        
def mainPalindrome():
    symbolString = 'P'
    while symbolString.upper() != 'Q':
        symbolString = raw_input("Enter String or Q to quit: ")
        if symbolString.upper() == 'Q':
            break
        #print("Entered String - " + symbolString )
        print( palindrome_check(symbolString) )
    
    
##################    
#Palindrome Check#
##################
###Discuss - What is Big(O) for this function and can it be improved
def palindrome_check(string):
    dequeString = Deque()
    for characterS in string:
        dequeString.add_rear(characterS)
    
    equal= True
    print("Entered String - " + dequeString.__str__() )
    while dequeString.size() > 1 and equal:
        front = dequeString.remove_front()
        rear = dequeString.remove_rear()
        if front != rear:
            equal = False
            
    return equal

###################
#######Test#######
###################      
main("PALINDROME_CHECK")
    