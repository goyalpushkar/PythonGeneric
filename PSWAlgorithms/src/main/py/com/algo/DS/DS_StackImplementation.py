'''
Created on Jan 27, 2020

@author: goyalpushkar
'''
from buildtools import process

if __name__ == '__main__':
    pass

from DS_Stack import Stack


def main( program ):
    if program.upper() == 'PARANTHESIS':
        mainParanthesis()
    elif program.upper() == 'BASE_CONVERTER':
        mainBaseConverter() 
    elif program.upper() == 'INFIX_TO_POSTFIX':
        mainInfixToPostfix()
    elif program.upper() == 'INFIX_TO_PREFIX':
        mainInfixToPrefix()
    elif program.upper() == 'INFIX_TO_POSTFIX_EVAL':    
        mainInfixToPostFixEval()
        
def mainParanthesis():
    symbolString = 'P'
    while symbolString.upper() != 'Q':
        symbolString = raw_input("Enter Paranthesis String and Q to quit: ")
        if symbolString.upper() == 'Q':
            break
        print("Entered String: " + symbolString)
        print( par_checker(symbolString) )
    
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
        print( base_converter( int(decimalValue), int(baseValue) ) )
      
def mainInfixToPostfix():
    symbolString = 'P'
    while symbolString.upper() != 'Q':
        symbolString = raw_input("Enter Infix String and Q to quit: ")
        if symbolString.upper() == 'Q':
            break
        print("Entered String: " + symbolString)
        postFixExpr = infix_to_postfix(symbolString)
        print( "".join(postFixExpr) )
       
        calculateString = raw_input("Want to calculate value (y/n): ")
        if calculateString.upper() == 'Y':
            print( calculatePostFix(postFixExpr) )

def mainInfixToPrefix():
    symbolString = 'P'
    while symbolString.upper() != 'Q':
        symbolString = raw_input("Enter Infix String and Q to quit: ")
        if symbolString.upper() == 'Q':
            break
        print("Entered String: " + symbolString)
        preFixExpr = infix_to_prefix(symbolString)
        print( "".join(preFixExpr) )
       
        calculateString = raw_input("Want to calculate value (y/n): ")
        if calculateString.upper() == 'Y':
            print( calculatePreFix(preFixExpr) )
 
def mainInfixToPostFixEval():
    symbolString = 'P'
    while symbolString.upper() != 'Q':
        symbolString = raw_input("Enter Infix String and Q to quit: ")
        if symbolString.upper() == 'Q':
            break
        print("Entered String: " + symbolString)
        postFixExpr = infix_to_postfix_eval(symbolString)
        print( postFixExpr )
        
######################
#Matching Paranthesis#
######################
def checkMatching(closedParanthesis, stackValue):
    opens = "([{"
    closes = ")]}"
    #print("Close: " + closedParanthesis + " :Open - " + stackValue + " :Match - " + str( opens.index(stackValue) == closes.index(closedParanthesis) ) )
    return opens.index(stackValue) == closes.index(closedParanthesis)
    
    '''
    if closedParanthesis == ')' and stackValue == '(':
        return True
    elif closedParanthesis == ']' and stackValue == '[':
        return True
    elif closedParanthesis == '}' and stackValue == '{':
        return True
    else:
        return False
    '''
      
def par_checker( symbol_string ):
    index = 0
    balanced = True
    paranthesisStack = Stack()
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in ('([{'):
            paranthesisStack.push(symbol)
        else:
            if paranthesisStack.is_empty():
                balanced = False
            else:
                if checkMatching(symbol, paranthesisStack.peek() ):
                    paranthesisStack.pop()
                else:
                    paranthesisStack.push(symbol) 
        
        index = index + 1
                    
    if paranthesisStack.is_empty() and balanced:
        return True
    else:
        return False
 
###########################       
#Decimal to Base Converter#
###########################
def base_converter(dec_number, base):
    digits  = "0123456789ABCDEF"
    RemainderValue = Stack()
    #print(dec_number + " "  + base)
    
    while dec_number > 0:
        RemainderValue.push( dec_number % base )
        dec_number = dec_number // base
        
    finalValue = ""
    while not RemainderValue.is_empty():
        finalValue = finalValue + str( digits[RemainderValue.pop()] )
     
    #print(finalValue)
    return finalValue    

##################   
#Infix to Postfix#
##################
def checkPrecedence(infixValue, stackValue):
    orderOfPrecedence = { '(':1, '+': 2, '-':2, '*':3, '/':3, '^':4 }
    #print( "Infix - " + str(orderOfPrecedence.get(infixValue)) + " :Stack - " + str(orderOfPrecedence.get(stackValue)) )
    return orderOfPrecedence.get(infixValue) <= orderOfPrecedence.get(stackValue)
    
    
def infix_to_postfix(infix):
    infixList = infix.split()
    processingStack = Stack()
    postFixList = []
    #index = 0
    #while not infixList.is_empty():
    for index in range( len(infixList) ):    
        value = infixList[index]
        #print( "value - " + value )
        if value.isalnum():  #value.isdigit() or value.isalpha()    
            postFixList.append(value)
        elif value == '(':
            processingStack.push(value)  
        elif value == ')':
            while ( not processingStack.is_empty() ) and processingStack.peek() != '(':
                postFixList.append(processingStack.pop())
                
            processingStack.pop()
        else:
            while ( not processingStack.is_empty() ) and checkPrecedence(value, processingStack.peek()): #and processingStack.peek() != '(' 
                #print( "less precedence" )
                postFixList.append(processingStack.pop())
                
            processingStack.push(value)
        #index = index + 1
        #print( "Stack - " + processingStack.__str__() )
        
    while not processingStack.is_empty():
        postFixList.append(processingStack.pop())
           
    '''
    postFixString = ""
    for char in postFixList:
        if postFixString != "":
            postFixString = postFixString + " "
        postFixString = postFixString + char
    '''
            
    return postFixList  #"".join(postFixList) #postFixList.__str__()

def calculate( operand, operator1, operator2 ):
    if operand == '*':
        return operator1 * operator2
    elif operand == '+':
        return operator1 + operator2
    elif operand == '-':
        return operator1 - operator2
    elif operand == '/':
        return operator1 / operator2
    elif operand == '^':
        return pow(operator1, operator2)
        
def calculatePostFix(postFix):
    processingStack = Stack()
    #postFixList = postFix.split()
    for charVal in postFix:
        #print(char)
        if charVal.isalpha():
            return "Expression cannot be calculated as it contains alphabets"
        
        if charVal.isdigit():
            processingStack.push( int(charVal) )
        else:
            value1 = processingStack.pop()
            value2 = processingStack.pop()
            #print( calculate( char, value2, value1 ) )
            processingStack.push( calculate( charVal, value2, value1 ) )
    
    return processingStack.pop()


##################   
#Infix to Prefix#
##################
'''
def checkPrecedencePre(infixValue, stackValue):
    orderOfPrecedence = { '(':1, '+': 2, '-':2, '*':3, '/':3, '^':4 }
    #print( "Infix - " + str(orderOfPrecedence.get(infixValue)) + " :Stack - " + str(orderOfPrecedence.get(stackValue)) )
    return orderOfPrecedence.get(infixValue) >= orderOfPrecedence.get(stackValue)
'''    
    
def infix_to_prefix(infix):
    infixList = infix.split()
    processingStack = Stack()
    operatorStack = Stack()
    #postFixList = []
    #index = 0
    #while not infixList.is_empty():
    for index in range( len(infixList) ):    
        value = infixList[index]
        
        if value.isalnum():  #value.isdigit() or value.isalpha()    
            operatorStack.push(value)
        elif value == '(':
            processingStack.push(value)  
        elif value == ')':
            while processingStack.peek() != '(':
                value1 = operatorStack.pop()
                value2 = operatorStack.pop()
                operand = processingStack.pop()
                operatorStack.push( operand + " " + str(value2) + " " + str(value1) )
                
            processingStack.pop()
        else:
            while ( not processingStack.is_empty() ) and checkPrecedence(value, processingStack.peek()): #and processingStack.peek() != '(' 
                value1 = operatorStack.pop()
                value2 = operatorStack.pop()
                operand = processingStack.pop()
                operatorStack.push( operand + " " + str(value2) + " " + str(value1) )
                
            processingStack.push(value)
        #index = index + 1
     
    while not processingStack.is_empty():
        value1 = operatorStack.pop()
        value2 = operatorStack.pop()
        operand = processingStack.pop()
        operatorStack.push( operand + " " + str(value2) + " " + str(value1) )
                
           
    return "".join(operatorStack.pop()) #postFixList.__str__()


def calculatePreFix(preFix):
    processingStack = Stack()
    preFixList = preFix.split(" ")
    index = 0
    
    for index in range( len(preFixList) - 1, -1, -1):
        charVal = preFixList[index]
        if charVal.isalpha():
            return "Expression cannot be calculated as it contains alphabets"
        
        if charVal.isdigit():
            processingStack.push( int(charVal) )
        else:
            value1 = processingStack.pop()
            value2 = processingStack.pop()
            #print( calculate( char, value2, value1 ) )
            processingStack.push( calculate( charVal, value1, value2 ) )
    
        #print( "Index - " + str(index) + " :charVal - " + charVal + " :processingStack - " + processingStack.__str__() )
    '''
    operatorStack = Stack()
    #for index in range( len(preFixList) ):
    while index < len(preFixList):
        value = preFixList[index]
        #print( "Index - " + str(index) + " :Process - " +  value)
        if value.isdigit():
            operatorStack.push( int (value) )
            index = index + 1
        else:
            if ( index + 1 < len(preFixList) ) and ( index + 2 < len(preFixList) ):
                if ( preFixList[index+1].isdigit() and preFixList[index+2].isdigit() ):
                    operatorStack.push( calculate( value, int(preFixList[index+1]), int(preFixList[index+2]) ) )
                    index = index + 3 
                else:
                    if checkPrecedence(value, processingStack.peek()):
                        if operatorStack.size() >= 2:
                            value1 = operatorStack.pop()
                            value2 = operatorStack.pop()
                            operatorStack.push( calculate( processingStack.pop(), value2, value1 ) )
                        
                    processingStack.push(value)
                    index = index + 1
            else:
                if checkPrecedence(value, processingStack.peek()):
                    if operatorStack.size() >= 2:
                        value1 = operatorStack.pop()
                        value2 = operatorStack.pop()
                        operatorStack.push( calculate( processingStack.pop(), value2, value1 ) )
                      
                processingStack.push(value)
                index = index + 1
        
        #print( "Operator Stack - " + operatorStack.__str__() )
        #print( "Processing stack - " + processingStack.__str__() )
        
    while not processingStack.is_empty():
        operator = processingStack.pop()
        value1 = operatorStack.pop()
        value2 = operatorStack.pop()
        operatorStack.push( calculate( operator, value2, value1 ) )
     '''
           
    return processingStack.pop() #operatorStack.pop()

############################   
#Infix to PostFix Evaluator#
############################
def infix_to_postfix_eval( infix ):
    infixList = infix.split()
    operandStack = Stack()
    operatorStack = Stack()
    
    for charVal in infixList:
        
        if charVal.isalpha():
            return "Expression cannot be calculated as it contains alphabets"
    
        if charVal.isdigit():
            operandStack.push(charVal)
        elif charVal == '(':
            operatorStack.push(charVal)
        elif charVal == ')':
            while operatorStack.peek() != '(':
                value1 = int( operandStack.pop() )
                value2 = int( operandStack.pop() )
                operandStack.push( calculate( operatorStack.pop(), value2, value1 ) )
            
            operatorStack.pop()
        else:
            if not operatorStack.is_empty():
                if checkPrecedence( charVal, operatorStack.peek() ):
                    value1 = int( operandStack.pop() )
                    value2 = int( operandStack.pop() )
                    operandStack.push( calculate( operatorStack.pop(), value2, value1 ) )
            
        
            operatorStack.push( charVal )   
              
    while not operatorStack.is_empty():
        value1 = int( operandStack.pop() )
        value2 = int( operandStack.pop() )
        operandStack.push( calculate( operatorStack.pop(), value2, value1 ) )
            
        
    return operandStack.pop()
       

##################
## Call Program ##         
##################
programName = raw_input("Mention Program Name to Run: ")
main(programName.upper()) #PARANTHESIS  BASE_CONVERTER INFIX_TO_POSTFIX  INFIX_TO_PREFIX INFIX_TO_POSTFIX_EVAL
#mainParanthesis() 
#mainBaseConverter()
#INFIX_TO_PREFIX ( 10 + 5 ) * 6 - ( 4 - 2 ) * ( 3 + 7 ) 
#                ( 3 + 2 ) * 4 - ( ( 5 * 3 ) - ( 5 * 2 ) + ( 2 * 3 ) )