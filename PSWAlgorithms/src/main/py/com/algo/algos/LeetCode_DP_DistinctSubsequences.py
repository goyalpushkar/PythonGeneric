'''
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Input: 	 String, String
Output:  Int
Example
Input 1:  "rabbbit", "rabbit"
Output 1: 3

"rabbbit" --> "rabbit"
 ^^^^ ^^
"rabbbit" --> "rabbit"
 ^^ ^^^^
"rabbbit" --> "rabbit"
 ^^^ ^^^

Input 2:  "a", ""
Output 2: 1

Subsequences:
"a" --> ""
 ^

Input 3: "abbc", "abc"
Output 3: 2

Subsequences:

"abbc" --> "abc"
^^ ^
"abbc" --> "abc"
^ ^^

Constraints
Time Complexity: O(N * M) with N being the length of string, and M being the length of the subsequence.
Auxiliary Space Complexity: O(N)

'''
class Solution(object):
    def numDistinct(self, s, t):

        s_len = len(s)
        t_len = len(t)
        cache = {}

        # def distinct_ways_helper(s_index, t_index):
        #     key = (s_index, t_index)
        #     # source is finished/empty and target is still left return 0 else if target is finished return 1
        #     # i.e. target is found in source
        #     if s_index == s_len:
        #         if t_index == t_len:
        #             return 1
        #         else:
        #             return 0
        #
        #     # if target is finished then return 1
        #     if t_index == t_len:
        #         return 1
        #
        #     if key in cache:
        #         return cache[key]
        #
        #     # if both values are same call recursively for rest of the characters in both source and target
        #     if s[s_index] == t[t_index]:
        #         answer = distinct_ways_helper(s_index+1, t_index+1) + distinct_ways_helper(s_index+1, t_index)
        #     else:
        #         answer = distinct_ways_helper(s_index+1, t_index)
        #
        #     cache[key] = answer
        #
        #     return answer
        #
        # final_value = distinct_ways_helper(0, 0)
        # return final_value

        # 50/65 test cases passed # rest Time limit Exceeded
        def distinctways_helper(source, target, total_ways):  # index   index_list

            print(f"source: {source}\t target: {target} \t total_ways: {total_ways}")
            # if len(source) < len(target):
            if len(source) == 0:
                if len(target) == 0:
                    total_ways = 1
                    # final_index_list.append(",".join(str(elem) for elem in index_list))
                    return total_ways  # , index_list[:-1]  # , index - 1
                else:
                    total_ways = 0
                    return total_ways  # , index_list[:-1]    # , index - 1

            if len(target) == 0:
                total_ways = 1
                # final_index_list.append(",".join(str(elem) for elem in index_list))
                return total_ways  # , index_list[:-1]    # , index-1

            # Left branch
            if source[0] == target[0]:
                # index_list.append(index)
                # index += 1
                # source = source[1:]
                # target = target[1:]
                total_ways = distinctways_helper(source[1:], target[1:], total_ways) \
                             + distinctways_helper(source[1:], target, total_ways)  # , index_list)
            else:
                total_ways = distinctways_helper(source[1:], target, total_ways)   # , index_list)

            # Right Branch
            # Keep searching same string in source removing first element
            # total_ways_r = distinctways_helper(source[1:], target, total_ways)  # , index_list)


            # left_values[0] + right_values[0]
            # left_values[0] if left_values[0] >= right_values[0] else right_values[0]
            # total_ways_l + total_ways_r
            return total_ways    # left_values[0] + right_values[0]   # , index_list[:-1]

        total_ways = 0
        index = 0
        final_index_list = []
        final_value = distinctways_helper(s, t, total_ways)  # , index  , []
        print(f"final_value 0: {final_value}")   # [0]
        # print(f"final_value 1: {final_value[1]}")
        # print(f"final_value 2: {final_value[2]}")
        print(f"final_index_list: {final_index_list}")

        return final_value  # [0]


if __name__ == '__main__':
    n = int(input("Enter no of test cases: "))

    for i in range(n):
        s = input("Enter String 1: ")
        t = input("Enter String 2: ")

        sol = Solution()
        final_result = sol.numDistinct(s, t)
        print(f"final_result: {final_result}")
