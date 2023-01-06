'''
Given a string s, find the longest substring without repeating characters.

Input: String
Output: String
Example
Input: abcabcbb      =>	Output: abc
Input: bbbbb	 	=>	Output: b
Input: pwwkew		=>	Output: wke
Constraints
N ~ Length of input string
K ~ Number of unique characters in input string

Time Complexity: O(N)
Auxiliary Space Complexity: O(K)
s consists of English letters, digits, symbols and spaces.
'''
class Solution:
    def longest_substr(self, s):
        L = 0
        R = 0
        control_dict = {}
        curr_length = 0
        duplicate_char = 0
        max_length = 0
        start = 0
        end = 0

        while L < len(s) and R < len(s):
            print(f"{'-'*2}start:: L:{L}-{s[L]}\t R:{R}:{s[R]}\t curr_length:{curr_length}\n"
                  f"control_dict:{control_dict}\n"
                  f"max_length:{max_length}\tstart:{start}\t end: {end}\n")
            control_dict[s[R]] = control_dict.get(s[R], 0) + 1
            if control_dict[s[R]] > 1:
                duplicate_char += 1
            else:
                curr_length += 1

            print(f"{'-'*2}mid:: control_dict:{control_dict}\n")
            while duplicate_char == 1:
                if max_length < curr_length:
                    max_length = curr_length
                    start = L
                    end = R - 1

                if control_dict[s[L]] > 1:
                    duplicate_char -= 1
                else:
                    curr_length -= 1
                control_dict[s[L]] = control_dict.get(s[L], 0) - 1
                L += 1

            print(f"\n{'-'*2}end:: L:{L}-{s[L]}\t R:{R}:{s[R]}\t curr_length:{curr_length}\n"
                  f"control_dict:{control_dict}\n"
                  f"max_length:{max_length}\tstart:{start}\t end: {end}\n\n")
            R += 1

        print(f"control_dict:{control_dict}\n"
              f"curr_length:{curr_length}\n"
              f"max_length:{max_length}\tstart:{start}\t end: {end}\n\n")
        return s[start:end+1]


if __name__ == '__main__':
    no_of_tests = int(input("No of tests: "))
    # abcabcbb - 3 (abc)
    # bbbb - 1 (b)
    # pwwkew - 3 (wke)
    # ttbtctcbt - 3 (btc)
    for i in range(no_of_tests):
        input_string = input("Enter String: ")
        solution = Solution()
        result = solution.longest_substr(input_string)
        # longest_palindrome(input_string)
        print(f"result: {result}")