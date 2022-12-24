'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

2 - abc
3 - def
4 - ghi
5 - jkl
6 - mno
7 - pqrs
8 - tuv
9 - wxyz

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def rec_call(set1, set2):
            # print(f"Sets: set1-{set1}, set2-{set2}")
            return_result = []
            for elem in set1:
                for elem2 in set2:
                    return_result.append(elem+elem2)

            return return_result

        index = len(digits)-1
        final_result = []
        # print(f"index: {index}")
        while (index >= 0):
            # print(f"index: {index}\n"
            #       f"digit_dict[digits[index]]: {digit_dict[digits[index]]}")
            if not final_result and index == 0:
                for elem in digit_dict[digits[index]]:
                    final_result.append(elem)
                index -= 1
            elif not final_result:
                final_result = rec_call(digit_dict[digits[index-1]], digit_dict[digits[index]])
                index -= 2
            else:
                set2 = final_result
                final_result = rec_call(digit_dict[digits[index]], set2)
                index -= 1

        return final_result


if __name__ == '__main__':
    digits = "239"
    solution = Solution()
    result = solution.letterCombinations(digits)
    print(f"result: {result}")

# digit_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
# final_string = ""
# for digit in digits:
#     final_string += digit_dict[digit]
#
# print(f"final_string: {final_string}")
# if final_string == "":
#     return []
#
# final_result = []

# def rec_call(build, height, result):
#
#     if height == len(final_string):
#         result.append(build)
#         return result
#
#     # left call
#     result = rec_call(build, height+1, result)
#
#     # Right call
#     result = rec_call(build+final_string[height], height + 1, result)
#
#     return result
#
# final_result = rec_call("", 0, final_result)

# return final_result