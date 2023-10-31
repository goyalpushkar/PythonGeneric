'''
You have to check whether a given string is a valid mathematical expression or not. A string is 
considered valid if it contains matching opening and closing parenthesis as well as valid mathematical operations. The string contains the following set of parentheses ‘(‘, ’)’, ’[’, ’]’, ’{’, ’}’, numbers from 0 to 9 and following operators ‘+’, ’-’ and ‘*’.

Example One
{
"expression": "{(1+2)*3}+4"
}
Output:

1
The mathematical expression as well as the parentheses are valid.

Example Two
{
"expression": "((1+2)*3*)"
}
Output:

0
Here the parentheses are valid but the mathematical expression is not. There is an operator ‘*’ 
without any operand after it.

Notes
An expression that consists of only parentheses is considered valid if it contains correct opening
 and closing parentheses. Example: “{()}” is considered valid.
Constraints:

1 <= length of the expression <= 100000
Possible characters in the expression string: ‘+’, ‘-’, ‘*’ and [0-9]
.
.
.
.
.

Autocomplete

I/O
'''
def is_valid(expression):
    from collections import deque
    
    matching_brackets = {'}': '{', ']': '[', ')': '('}
    operators = ["*", "+", "-"]
    operators = set(operators)
    opening_brackets = ["{", "[", "("]
    opening_brackets = set(opening_brackets)
    
    expres_stack = []
    number_stack = []
    
    curr_express = ""
    
    # def calculate_value(number_stack, operator):
    #     if number_stack:
    #         operand2 = number_stack.pop()
    #     else: 
    #         return False
        
    #     if number_stack:
    #         operand1 = number_stack.pop()
    #     else:
    #         return False
            
    #     result = eval(str(operand1) + operator + str(operand2))
    #     # print(f"result: {result}")
    #     number_stack.append(result)
        
    #     return True
    
    # isDigit is used to verify that there is no case where there is no number after an operator
    # e.g. (2)3+ will work fine without isDigit usage
    isDigit = True
    for i, val in enumerate(expression):
        # print(f"i: {i}, val: {val}, expres_stack: {expres_stack}, number_stack: {number_stack}")
        
        # if it is not a closing bracket push values in the corresponding stacks
        # if val not in matching_brackets.keys():
        if val.isdigit():
            number_stack.append(val)
            isDigit = True
        elif val in operators and number_stack:
            expres_stack.append(val)
            isDigit = False
        elif val in opening_brackets:
            expres_stack.append(val)
        # else try to find matching opening bracket
        elif val in matching_brackets.keys():
            # if current value is a closing bracket and stack is already empty
            if not expres_stack or not isDigit:
                return False
                
            # curr_val = expres_stack.pop()
            # Pop elements from expres_stack until we have opening bracket
            while expres_stack:  # curr_val not in ('(','[','{'):
                curr_val = expres_stack.pop()
                # Check if top value is an opening bracket and a matching bracket
                if curr_val == matching_brackets[val]:
                    break
                # If curr_val is an operator then calcualte value
                elif curr_val in operators:
                    if len(number_stack) <= 1:
                        return False
                    
                    number_stack.pop()
                    # if not calculate_value(number_stack, curr_val):
                    #     return False
                else:
                    return False
                    
                # curr_val = expres_stack.pop()
            
            # # Check if top value is an opening bracket and not a matching bracket
            # if curr_val != matching_brackets[val]:
            #     return False
        else:
            return False
        
    # print(f"expres_stack: {expres_stack}, number_stack: {number_stack}")
    while expres_stack:
        curr_val = expres_stack.pop()
            
        # Pop elements from express_stack until we have opening bracket
        # If curr_val is an opoerator then calcualte value
        if curr_val in operators:
            # if not calculate_value(number_stack, curr_val):
            #     return False
            if len(number_stack) <= 1:
                return False
            else:
                number_stack.pop()
        # if it is not an operator then it must be opening bracket as 
        # closing brackets are handled earlier
        else:
            return False
    
    # print(f"expres_stack: {expres_stack}, number_stack: {number_stack}")
    # if there are more than 2 values left in number_stack or anything left in express_stack then it is invalid
    if len(number_stack) > 1 or expres_stack or not isDigit:
        return False
    
    return True