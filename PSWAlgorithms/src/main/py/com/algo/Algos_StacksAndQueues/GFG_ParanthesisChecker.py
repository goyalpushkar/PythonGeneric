'''

Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

Input:
The first line of input contains an integer T denoting the number of test cases.  Each test case consists of a string of expression, in a separate line.

Output:
Print 'balanced' without quotes if the pair of parenthesis is balanced else print 'not balanced' in a separate line.

Constraints:
1 ≤ T ≤ 100
1 ≤ |s| ≤ 105

Example:
Input:
3
{([])}
()
([]

Output:
balanced
balanced
not balanced
'''

from collections import deque
def paranthesis_check(paran_string):

    paran_deque = deque()
    out_parans = [')', '}', ']']
    in_parans = ['(', '{', '[']
    match_parans = {')': '(', '}': '{', ']': '['}
    for index in range(len(paran_string)):
        #print("Paran Deque: " + " ".join(list(map(str, paran_deque))))
        #print(paran_string[index])
        if paran_string[index] in in_parans:
            paran_deque.append(paran_string[index])
        elif paran_string[index] in out_parans:
            if len(paran_deque) > 0:
                top_elem = paran_deque[len(paran_deque)-1]
                #print("Match Elem: " + match_parans[paran_string[index]])
                if top_elem == match_parans[paran_string[index]]:
                    paran_deque.pop()
                else:
                    paran_deque.append(paran_string[index])
            else:
                paran_deque.append(paran_string[index])

    #print("Paran Deque Final: " + " ".join(list(map(str, paran_deque))))
    if len(paran_deque) > 0:
        return "not balanced"
    else:
        return "balanced"


if __name__ == '__main__':
    test_cases = int(input("No of test cases: "))
    for elem in range(test_cases):
        paran_string = input("String: ").strip() #.split()

        print(paranthesis_check(paran_string))