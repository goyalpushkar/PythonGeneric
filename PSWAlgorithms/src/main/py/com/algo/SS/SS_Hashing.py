'''
Created on Feb 5, 2020

@author: goyalpushkar
'''

if __name__ == '__main__':
    pass

import math 

final_list = dict()

def remainder_hash( item, table_size ):
    return item % table_size

def folding_method( item, group_size, table_size ):
    noOfGroups = len(str(item)) / group_size
    sumValue = 0 
    for i in range( noOfGroups ):
        tensPower = math.pow(10, group_size)
        sumValue = sumValue + ( item % tensPower)
        item = item // tensPower
    
    print( "sum - " + str(sumValue) )
    return int( sum % table_size )

def mid_square( item, table_size ):
    square = int( math.pow(item, 2) )
    mid = len(str(square)) // 2
    middleTwo = int( str(square)[mid-1] + str(square)[mid] ) 
    print( "middleTwo - " + str(middleTwo) )
    return int( middleTwo % table_size )

def char_hash( a_string, table_size ):
    sumValue = 0
    for chr in a_string:
        sumValue = sumValue + ord(chr)
    
    print( "sum - " + str(sumValue))
    return sum % table_size

#Anagrams will have same positional value so use weighted factor
def char_hash_weighted( a_string, table_size ):
    sumValue = 0
    for pos in range(len(a_string)):
        sumValue = sumValue + ( (pos+1) * ord( a_string[pos] ) )
    
    print( "sum - " + str(sumValue))
    return sum % table_size

def checkValueExistence(key):
    if final_list.get(key, None) == None:
        return True
    else:
        return False
    
def linearProbing( item, step_size, table_size ):    
    print("Step Size - " + str(step_size) )
    original_hash = remainder_hash( item, table_size )
    found = False
    weight = 1
    new_hash = original_hash
    while not found:
        found = checkValueExistence( int( original_hash + (weight * step_size) ) % table_size ) 
        new_hash = int( original_hash + (weight * step_size) ) % table_size
        weight = weight + 1

    return new_hash

def linearProbingRehash( original_hash, weight, step_size, table_size ):  
    return int( original_hash + (weight * step_size) ) % table_size

def quadraticProbing( item, table_size ):    
    original_hash = remainder_hash( item, table_size )
    found = False
    weight = 1
    new_hash = original_hash
    while not found:
        found = checkValueExistence( int( original_hash + int( math.pow(weight, 2) ) ) % table_size ) 
        new_hash = int( original_hash + int( math.pow(weight, 2) ) ) % table_size
        weight = weight + 1

    return new_hash

def quadraticProbingRehash( original_hash, weight, table_size ):    
    return int( original_hash + int( math.pow(weight, 2) ) ) % table_size

def putHashValue( item, step_size, linQuadProb, table_size ):
    original_hash = remainder_hash( item, table_size )
    print( "original_hash - " + str(original_hash) )
    if checkValueExistence(original_hash):
        final_list[original_hash] = item
    else:
        if linQuadProb.upper() == 'L':
            new_hash = linearProbing( item, step_size, table_size )
        else:
            new_hash = quadraticProbing( item, table_size )
            
        print( "new_hash - " + str(new_hash) )
        final_list[new_hash] = item
        
def getHashValueIndex( item, step_size, linQuadProb, table_size ):
    original_hash = remainder_hash( item, table_size )
    #print( "original_hash - " + str(original_hash) )
    
    index = original_hash
    found = False
    weight = 1
    while final_list[index] != None and not found:
        #print( "index - " + str(index) )
        if final_list[index] == item:
            found = True 
        else:
            if linQuadProb.upper() == 'L':
                index = linearProbingRehash( original_hash, weight, step_size, table_size )
            else:
                index = quadraticProbingRehash( original_hash, weight, table_size )
                
            weight = weight + 1
            
    return index

#113, 117, 97, 100, 114, 108, 116, 105, 99
#  3,   7,  9,   1,   4,   9,   6,   6,  0
#{0: 99, 1: 100, 3: 113, 4: 114, 6: 116, 7: 117, 8: 105, 9: 97, 10: 108}
def populateHashTable( itemList, step_size, linQuadProb, table_size ):
    values = itemList.split(", ")    
    for value in values:
        print( "value - " + str(value) )
        putHashValue( int(value), step_size, linQuadProb, table_size )
        
    print( final_list.__repr__() )
    
def getHashTableIndex( item, step_size, linQuadProb, table_size ):
    print( "item - " + str(item) )
    indexValue = getHashValueIndex( int(item), step_size, linQuadProb, table_size )
        
    print( "Index Value - " + str(indexValue)  )
    
def main():
    usrInput = 'P'
    while usrInput.upper() != 'Q':
        print( "Run one of the following functions: ")
        print( "\t 1. Remainder Hash")
        print( "\t 2. Folding Method")
        print( "\t 3. Mid Square")
        print( "\t 4. Character Hash")
        print( "\t 5. Weighted Character Hash")
        print( "\t 6. Push Hash Table")
        print( "\t 7. Get Hash Value Index")
        usrInput = raw_input("Enter Number for above programs or q to quit: ") 
        if usrInput.upper() == 'Q':
            break
        
        table_size = int( raw_input("Enter table size for storing hash values: ") )
        if usrInput == '1':
            item = raw_input("Enter Number to get Hash value: ") 
            print( remainder_hash( int(item), table_size) )
        elif usrInput == '2':
            item = raw_input("Enter Number to get Hash value: ") 
            groupSize = raw_input("Enter Group Size for folding: ") 
            print( folding_method( int(item), int(groupSize), table_size) )
        elif usrInput == '3':
            item = raw_input("Enter Number to get Hash value: ") 
            print( mid_square( int(item), table_size) )
        elif usrInput == '4':
            item = raw_input("Enter String to get Hash value: ") 
            print( char_hash( item,table_size) )
        elif usrInput == '5':
            item = raw_input("Enter String to get Hash value: ") 
            print( char_hash_weighted( item,table_size) )
        elif usrInput == '6':
            item = raw_input("Enter comma seperated numbers to put into Hash table: ") 
            linQuadP = raw_input("Enter L for Linear Probing or Q for Quadratic Probing: ")
            stepSize = 1
            if linQuadP.upper() == 'L':
                stepSize = int( raw_input("Enter step size for Linear Probing: ") )
                
            populateHashTable( item, stepSize, linQuadP, table_size )     
        elif usrInput == '7':
            item = raw_input("Enter Item value to get index from Hash table: ") 
            linQuadP = raw_input("Enter L for Linear Probing or Q for Quadratic Probing: ")
            stepSize = 1
            if linQuadP.upper() == 'L':
                stepSize = int( raw_input("Enter step size for Linear Probing: ") )
             
            getHashTableIndex( item, stepSize, linQuadP, table_size )
main()