'''
Created on Jan 31, 2020

@author: goyalpushkar
'''
#from audioop import reverse
from timeit import Timer
from matplotlib import pyplot
#from functools import lru_cache

if __name__ == '__main__':
    pass

def calc_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calc_factorial(n-1)
        
def base_conversion(n, base):
    digits  = "0123456789ABCDEF"
    
    if n < base:
        return digits[n]
    else:
        return base_conversion(n / base, base) + digits[n%base]
    
def reverse_string(passedValue):
    
    if len(passedValue) == 1:
        return passedValue
    else:
        return reverse_string( passedValue[1:]) + passedValue[0]
    
def palindrome( palinString ):
    found = False
    
    if palinString[0] != palinString[ len(palinString) - 1 ]:
        return False
    else:
        palindrome( palinString[ 1: len(palinString) - 2 ] )
        
def fibonaciRecu(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaciRecu(n-1) + fibonaciRecu(n-2)
  
memory = {0:0, 1:1}
def fibonaciRecuMemory(n):
    
    if not n in memory:
        memory[n] = fibonaciRecuMemory(n-1) + fibonaciRecuMemory(n-2)
        
    return memory[n]

def fibonaciNonRecu(n):
    a = 0
    b = 1
    for n in range(n):
        a = b
        b = a + b
        
    return a
       
'''
#@functools.lru_cache(maxsize = None)       
def fibonaciReculru(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaciRecu(n-1) + fibonaciRecu(n-2)
'''

def mainFactorial():
    userInput = raw_input("Enter Number to get factorial or q to quit: ")
    while userInput.upper() != 'Q':
        print( calc_factorial( int( userInput ) ) )
        userInput = raw_input("Enter Number to get factorial or q to quit: ")
        
def mainReverseString():
    userInput = raw_input("Enter String to reverse or q to quit: ")
    while userInput.upper() != 'Q':
        print( reverse_string( userInput ) )
        userInput = raw_input("Enter String to reverse or q to quit: ")
        
def mainBaseConverter():
    decimalValue = 'P'
    baseValue = 'P'
    while decimalValue != 'Q' or baseValue != 'Q':
        decimalValue =  raw_input("Enter Decimal Value and Q to quit: ")
        if decimalValue.upper() == 'Q':
            break
        
        baseValue = raw_input("Enter Base Value and Q to quit: ") 
        if baseValue.upper() == 'Q':
            break
        
        print( "Decimal: " + str(decimalValue) + " Base: " + str(baseValue) )
        print( base_conversion( int(decimalValue), int(baseValue) ) )

def mainPalindrome():
    userInput = raw_input("Enter String to check Palindrome or q to quit: ")
    while userInput.upper() != 'Q':
        print( palindrome( userInput ) )
        userInput = raw_input("Enter String to check Palindrome or q to quit: ")
     
def mainFibonacci():
    fibonaciRecuList = list()
    fibRecuMemoryList = list()
    fibNonRecuList = list()
    #fibNonRecuLRUList = list()
    indexList = list()
    print("Fibonacci Series Calculation")
    for index in range(41):
        fibRecu = Timer("fibonaciRecu(%d)"%(index), "from Recursion import fibonaciRecu")
        fibRecuVal = fibRecu.timeit(3)
        fibRecuMemory = Timer("fibonaciRecuMemory(%d)"%(index), "from Recursion import fibonaciRecuMemory")
        fibRecuMemoryVal = fibRecuMemory.timeit(3)
        fibNonRecu = Timer("fibonaciNonRecu(%d)"%(index), "from Recursion import fibonaciNonRecu")
        fibNonRecuVal= fibNonRecu.timeit(3)
        #fibNonRecuLRU = Timer("fibonaciReculru(%d)"%(index), "from Recursion import fibonaciNonRecu")
        #fibNonRecuLRUVal= fibNonRecuLRU.timeit(3)
        
        fibonaciRecuList.append(fibRecuVal)
        fibRecuMemoryList.append(fibRecuMemoryVal)
        fibNonRecuList.append(fibNonRecuVal)
        #fibNonRecuLRUList.append(fibNonRecuLRUVal)
        indexList.append(index)
        print( "n=%2d, fibRec: %8.6f, fibNonRecu:  %8.6f, fibRecuMemory:  %8.6f, percent(fibRec/fibNonRec): %10.2f, percent(fibRecMemo/fibNonRec): %10.2f" % (index, fibRecuVal, fibNonRecuVal, fibRecuMemoryVal, fibRecuVal/fibNonRecuVal, fibRecuMemoryVal/fibNonRecuVal) )  
        #, fibNonRecuLRUVal: %8.6f  fibNonRecuLRUVal
     
    pyplot.title("Compare Fibonacci Series")

    print("Show plot")
    subplot = pyplot.subplot()
    pyplot.ylabel("Time(s) to execute statements")
    pyplot.xlabel("List Size")
 
    pyplot.xticks(indexList)
    subplot.plot(indexList, fibonaciRecuList, color='red', linestyle='solid', label='Fibonacci Recursive', marker='^', linewidth = 6)
    subplot.plot(indexList, fibRecuMemoryList, 'bo--', label='Fibonacci Recursive Memory', marker='.',linewidth = 7)  
    subplot.plot(indexList, fibNonRecuList, 'g', linestyle='dashed', label='Fibonaci Non Recursive', marker='p',linewidth = 8)
    #subplot.plot(indexList, fibNonRecuLRUList, 'br', linestyle='dashed', label='Fibonaci Non Recursive', marker='o',linewidth = 8)  

    chartBox = subplot.get_position()  ##This is required to put legend outside
    subplot.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.7, chartBox.height])
    subplot.legend(loc='upper center', bbox_to_anchor=(1.30, 0.8), shadow=True, ncol=1)
    #pyplot.legend
    #(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2) Put legend in the bottom
    #(loc='upper center', bbox_to_anchor=(0.5, 1.00), shadow=True, ncol=2) Put legend on the top
     
    pyplot.show()
     
def main():
    print("Run any of the below programs - ")
    print("\t 1. Factorial")
    print("\t 2. Base Converter")
    print("\t 3. Reverse String")
    print("\t 4. Palindrome String")
    print("\t 5. Fibonacci String")
    userInput = raw_input("Enter Number corresponding to the program or q to quit: ")
    while userInput.upper() != 'Q':
        if userInput == '1':
            mainFactorial()
        elif userInput == '2':
            mainBaseConverter()
        elif userInput == '3':
            mainReverseString()
        elif userInput == '4':
            mainPalindrome()
        elif userInput == '5':
            mainFibonacci()
            
        print("Run any of the below programs - ")
        print("\t 1. Factorial")
        print("\t 2. Base Converter")
        print("\t 3. Reverse String")
        print("\t 4. Palindrome String")
        print("\t 5. Fibonacci String")
        userInput = raw_input("Enter Number corresponding to the program or q to quit: ")
    
main()