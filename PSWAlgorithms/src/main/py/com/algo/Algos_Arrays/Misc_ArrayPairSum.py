'''
Created on Mar 2, 2020

@author: goyalpushkar
'''

'''
Given an integer array, output all the unique pairs that sum up to a specific value k.
So the input:
pair_sum([1,3,2,2],4)

would return 2 pairs:
 (1,3)
 (2,2)
'''

def arrayPairSum(usrlist, sumValue):
    print("Sum Value - " + str(sumValue) ) 
    
    counter = 0
    dictList = {}
    pairs = set()
    
    #Add elements and their count in dictionary
    for elem in usrlist:
        if elem in dictList:
            dictList[elem] += 1
        else:
            dictList[elem] = 1
            
    for elem in usrlist:
        #print(dictList)
        secondElem = sumValue - elem 
        if dictList.get(secondElem, 0) > 0 and dictList.get(elem, 0) > 0:
        #if secondElem in dictList and dictList[secondElem] > 0:
            #if dictList[secondElem] > 0:
            counter += 1
            dictList[secondElem] -= 1
            dictList[elem] -= 1
            pairs.add( (elem, secondElem) )
    
    return counter, pairs

def arrayPairSum1(usrList, sumValue):
    
    seen = set()
    pairs = set()
    for elem in usrList:
        secondElem = sumValue - elem
        
        if secondElem not in seen:
            seen.add(elem)
        else:
            pairs.add( ( min(elem, secondElem), max(elem, secondElem) ) )
        
    #print( len(pairs) )
    #print( )
    return len(pairs), pairs  
        
def main():
    noOfTests = raw_input("Enter number of test cases: ")
    for test in range( 1, int(noOfTests) + 1, 1 ):
        print( "-"*15)
        print("Test Case - " + str(test))
        noOfValues = raw_input("Enter number of elements in List: ")
        userList = list()
        for i in range( int(noOfValues) ):
            value = raw_input("Enter value: ")
            userList.append(int(value))
            
        sumValue = raw_input("Enter Sum Value: ")   
        #userList = raw_input("Enter comma seperated list of values")
        
        noOfPairs = arrayPairSum1( userList, int(sumValue) )
        print( "No of Pairs - " + str(noOfPairs[0]) )
        print( "\n".join( map(str, list(noOfPairs[1]) )))
        print( "-"*15)
        
if __name__ == '__main__':
    main()