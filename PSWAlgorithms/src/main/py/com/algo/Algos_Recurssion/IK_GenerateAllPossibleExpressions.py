'''
Given a string s that consists of digits ("0".."9") and target, a non-negative integer, find all expressions that can
be built from string s that evaluate to the target.

When building expressions, you have to insert one of the following operators between each pair of consecutive characters
 in s: join or * or +. For example, by inserting different operators between the two characters of string "12" we can
 get either 12 (1 joined with 2 or "12") or 2 ("1*2") or 3 ("1+2").

Other operators such as - or ÷ are NOT supported.

Expressions that evaluate to the target but only utilize a part of s do not count: entire s has to be consumed.

Precedence of the operators is conventional: join has the highest precedence, * – medium and + has the lowest precedence.
 For example, 1 + 2 * 34 = (1 + (2 * (34))) = 1 + 68 = 69.

You have to return ALL expressions that can be built from string s and evaluate to the target.

Example
{
"s": "202",
"target": 4
}
Output:

["2+0+2", "2+02", "2*02"]
Same three strings in any other order are also a correct output.

Notes
Order of strings in the output does not matter.
If there are no expressions that evaluate to target, return an empty list.
Returned strings must not contain spaces or any characters other than "0",..., "9", "*", "+".
All returned strings must start and end with a digit.
Constraints:

1 <= length of s <= 13
1 <= target <= 10^13
'''

def generate_all_expressions(s, target):
    """
    Args:
     s(str)
     target(int64)
    Returns:
     list_str
    """
    # Write your code here.
    result = []

    def helper(slate, index, value_so_far, last_value):
        nonlocal result
        # print(f"slate: {slate}, index: {index}, value_so_far: {value_so_far}, last_value: {last_value}")
        if value_so_far == target:
            if index == len(s):
                result.append(slate)
            
                return
                
        
        for i in range(index, len(s)):
            curr_expr = s[index:i+1]
            # print(f"curr_expr: {curr_expr}")
            curr_val = int(curr_expr)
            
            if index == 0:
                helper(curr_expr, i+1, value_so_far + curr_val, curr_val)
            else:
                # +
                helper(slate+"+"+curr_expr, i+1, value_so_far + curr_val, curr_val)
                
                # *
                helper(slate+"*"+curr_expr, i+1, (value_so_far - last_value) + (last_value*curr_val), last_value*curr_val)

        
        return

    helper("", 0, 0, 0)
    return result if result else []


# Didnt pass all tests
# half of them failed with time limit exceeded
def generate_all_expressions(s, target):
    """
    Args:
     s(str)
     target(int64)
    Returns:
     list_str
    """
    # Write your code here.
    result = []

    def helper(slate, index):

        # print(f"slate: {slate}, index:{index}")
        if index == len(s):
            # expres = "".join(str(int(x)) if x.isdigit() else x for x in slate)
            expres = ""
            for index in range(len(slate)):
                # if last value is 0 in the slate then appending 0 with digit like 02 is failing
                if slate[index].isdigit() and index - 1 >= 0 and slate[index - 1] == '0':
                    expres = expres[:-1] + str(int(slate[index]))
                elif slate[index].isdigit():
                    expres += str(int(slate[index]))
                # elif slate[index] == "":
                #     continue
                else:
                    expres += slate[index]

            actual_expres = "".join(slate)
            # print(f"expres: {expres}, actual_expres: {actual_expres}")
            if eval(expres) == target:
                result.append(actual_expres)

            return

        # print(f"slate JS: {slate}, index:{index}")
        # eval does not allow numbers atrting with 0
        # if slate and slate[-1] == "0":
        #     slate.pop()
        # slate.append(s[index])
        # helper(slate, index+1)
        # slate.pop()
        # print(f"slate JE: {slate}, index:{index}")

        # slate = s[index:id+1]
        # slate.append("*")
        # slate.append(s[index])
        # helper(slate, index+1)
        # slate.pop()
        # slate.pop()

        # slate.append("+")
        # slate.append(s[index])
        # helper(slate, index+1)
        # slate.pop()
        # slate.pop()

        for id in range(index, len(s)):
            # print(id, index)
            if index == 0:
                # slate.append(s[index+1])

                slate.append(s[index:id + 1])
                helper(slate, id + 1)
                slate.pop()

            else:
                # slate.append(s[index+1])
                slate.append("*")
                slate.append(s[index:id + 1])
                helper(slate, id + 1)
                slate.pop()
                slate.pop()

                slate.append("+")
                slate.append(s[index:id + 1])
                helper(slate, id + 1)
                slate.pop()
                slate.pop()

            # slate.append(s[index:id+1])
            # if id+1 < len(s):
            #     slate.append("+")
            # else:
            #     slate.append("")
            # # slate.append(s[index:id+1])
            # # slate.append(s[index+1])
            # helper(slate, id+1)
            # slate.pop()
            # slate.pop()

        return

    helper([], 0)
    return result if result else []

# Not working completely in case of below
# many timeout
# {
# "s": "1234567890123",
# "target": 1234567890123
# }
def generate_all_expressions(s, target):
    """
    Args:
     s(str)
     target(int64)
    Returns:
     list_str
    """
    # Write your code here.
    result = []

    def helper(slate, index):

        # print(f"slate: {slate}, index:{index}")
        if index == len(s):
            # expres = "".join(str(int(x)) if x.isdigit() else x for x in slate)
            expres = ""
            for index in range(len(slate)):
                if slate[index].isdigit() and index - 1 >= 0 and slate[index - 1] == '0':
                    expres = expres[:-1] + slate[index]
                else:
                    expres += slate[index]

            actual_expres = "".join(slate)
            # print(f"expres: {expres}, actual_expres: {actual_expres}")
            if eval(expres) == target:
                result.append(actual_expres)

            return

        # print(f"slate JS: {slate}, index:{index}")
        # eval does not allow numbers atrting with 0
        # if slate and slate[-1] == "0":
        #     slate.pop()
        slate.append(s[index])
        helper(slate, index + 1)
        slate.pop()
        # print(f"slate JE: {slate}, index:{index}")

        if index > 0:
            slate.append("*")
            slate.append(s[index])
            helper(slate, index + 1)
            slate.pop()
            slate.pop()

            slate.append("+")
            slate.append(s[index])
            helper(slate, index + 1)
            slate.pop()
            slate.pop()

        return

    helper([], 0)
    return result if result else []
