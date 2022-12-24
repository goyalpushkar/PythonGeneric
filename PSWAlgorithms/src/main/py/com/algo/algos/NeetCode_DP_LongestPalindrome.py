'''
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

'''

def longest_palindrome(s):

    def check_palindrome(start_palin, end_palin):
        while (start_palin <= end_palin):
            if s[start_palin] == s[end_palin]:
                start_palin +=1
                end_palin -= 1
            else:
                return False

        return True

    max_length = 0
    start_index = -1
    end_index = -1

    if len(s) == 0 or len(s) == 1:
        return s

    for index in range(len(s)):
        end = len(s) - 1
        print(f"max_length: {max_length}\n"
              f"start_index: {start_index} -- end_index: {end_index}\n")
        while end >= index:
            print(f"index: {index} - end: {end}")
            # start_palin = index
            # end_palin = end
            if check_palindrome(index, end):
                print(f"Result: True")
                length = end-index
                if length > max_length:
                    max_length = length
                    start_index = index
                    end_index = end
                break
            else:
                print(f"Result: False")
                end -= 1
                # print(f"end: {end} - index: {index}")


    if start_index >= 0:
        return s[start_index:end_index+1]
    else:
        return s[0]


if __name__ == '__main__':
    passed_string = input("Enter String: ")

    final_result = longest_palindrome(passed_string)

    print(f"final_result: {final_result}")
