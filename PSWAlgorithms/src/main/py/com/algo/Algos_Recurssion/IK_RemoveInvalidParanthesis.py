'''
Given a string that contains parentheses and letters, remove the minimum number of invalid parentheses to make
it a valid parentheses expression. Find All possible results.

Example One
{
"expression": "()())"
}
Output:

["()()", "(())"]
We can remove the last parenthesis (“()())”) or 2nd parenthesis (“()())”) to make the string valid.
We are removing only one parenthesis in both cases, hence both are valid output.

Example Two
{
"expression": "()(a))"
}
Output:

["()(a)", "((a))"]
Notes
Return an array which contains all the valid expressions which have the minimum number of removed parentheses.
All these expressions should be unique, that is, an expression should not repeat more than once.
The order of the elements in the output array does not matter.
Constraints:

1 <= length of the input string <= 30
Input string consists of lowercase English letters and parentheses '(' and ')'.
0 <= number of parentheses in the input string <= 20

'''


def remove_invalid_parentheses(expression):
    """
    Args:
     expression(str)
    Returns:
     list_str
    """
    # Write your code here.
    result = []

    def helper(slate, open, closed, index):
        print(f"slate: {slate}, open: {open}, closed: {closed}, index: {index}")
        if index == len(expression) and open == closed:
            result.append(slate)
            return

        if expression[index] == "(":
            helper(slate + expression[index], open + 1, closed, index + 1)
        elif expression[index].isalpha():
            helper(slate + expression[index], open, closed, index + 1)
        else:
            if open >= closed + 1:
                helper(slate, open, closed, index + 1)
                helper(slate + expression[index], open, closed + 1, index + 1)

    helper("", 0, 0, 0)
    set_result = set(result)
    print(f"result: {result} set_Result:{set_result}")
    return [elem for elem in set_result]