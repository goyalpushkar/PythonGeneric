'''
Given a string, return the shortest substring that has at least 3 unique characters, or false if there is no such string

Input: String
Output: String or Boolean
Example
Input: aabaca => Output: bac
Input: abaacc => Output: baac
Input: abc => Output: abc
Input: aabb => Output: False
Constraints
N ~ Length of input string
K ~ Number of unique characters in input string

Time Complexity: O(N)
Auxiliary Space Complexity: O(K)
s consists of English letters
'''
import math

class Solution(object):
    def shortest_with_3_unique(self, s):
        start = 0
        result = math.inf
        return_str = False
        unique_chars = 0
        freq_map = {}

        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1
            if freq_map[s[end]] == 1:
                unique_chars += 1

            if unique_chars >= 3:
                # Once 3 unique chars are received reset start
                while start <= end:
                    if freq_map.get(s[start], 0) - 1 == 0:
                        break

                    freq_map[s[start]] = freq_map.get(s[start], 0) - 1
                    start += 1

                # print(f"Result: {result}\t Start: {start}\t End: {end}")
                if result > end-start+1:
                    result = end-start+1
                    return_str = s[start:end+1]

        return return_str


if __name__ == '__main__':
    no_of_tests = int(input("No of tests: "))
    # PUSHKKRKPDGGGDGG, 1 - 6
    # ABBB, 2 - 4
    # AABABBA, 1 - 4
    # ABAB, 2 - 4
    for i in range(no_of_tests):
        input_string = input("Enter String: ")
        solution = Solution()
        result = solution.shortest_with_3_unique(input_string)
        print(f"result: {result}")