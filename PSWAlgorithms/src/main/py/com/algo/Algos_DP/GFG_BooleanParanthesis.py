'''
Given a boolean expression with following symbols.

Symbols
    'T' ---> true
    'F' ---> false

And following operators filled between symbols

Operators
    &   ---> boolean AND
    |   ---> boolean OR
    ^   ---> boolean XOR

Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

For Example:
The expression is "T | T & F ^ T", it evaluates true
in 4 ways ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T)
and (T|((T&F)^T)).

Return No_of_ways Mod 1003.

Input:
First line contains the test cases T.  1<=T<=500
Each test case have two lines
First is length of string N.  1<=N<=100
Second line is string S (boolean expression).
Output:
No of ways Mod 1003.


Example:
Input:
2
7
T|T&F^T
5
T^F|F

Output:
4
2
'''

'''




'''

def boolean_paranthesis(array_size, array):
    return 0

if __name__ == '__main__':
    t = int(input("No of test case: "))
    for index in range(t):
        array_size = int(input("Array Size: "))
        array = input("Values: ").strip()

        output_result = boolean_paranthesis(array_size, array)
        print(output_result)
