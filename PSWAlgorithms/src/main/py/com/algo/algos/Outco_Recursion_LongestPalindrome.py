'''
Given a string of lowercase characters (a-z), return the length of the longest palindromic subsequence.

Subsequence: a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

For example, the sequence ⟨A, B, D⟩ is a subsequence of ⟨A, B, C, D, E, F⟩ obtained after removal of elements C, E, and F.

https://en.m.wikipedia.org/wiki/Subsequence

Input: {String}
Output: {Integer}
Example
Input:  "vtvvv"
Output: 4

Longest palindromic subsequence here is "vvvv"


Input:  "pwnnb"
Output: 2

Longest palindromic subsequence here is "nn"


Input:  "ttbtctcbt"
Output: 7

Longest palindromic subsequence here is "tbtctbt"
Constraints
Time Complexity:			        O(N^2)
Auxiliary Space Complexity: 		O(N^2)
'''

# 5/30 passed, others failed due to time constraint
# def longest_palindrome(input_string):
#
#     height = len(input_string)
#     final_result = []
#     def check_palindrome(value):
#         start = 0
#         end = len(value)-1
#         while start <= end:
#             if value[start] == value[end]:
#                 start += 1
#                 end -= 1
#             else:
#                 return False
#
#         return True
#
#     def create_all_strings(build, level, result):
#         if level == height:
#             if build not in result:
#                 result.append(build)
#             return result
#
#         # left call
#         result = create_all_strings(build, level+1, result)
#
#         # right call
#         result = create_all_strings(build+input_string[level], level+1, result)
#
#         return result
#
#     final_result = create_all_strings("", 0, final_result)
#
#     print(final_result)
#     max_length = 0
#     max_value = ""
#     for elem in final_result:
#         if check_palindrome(elem):
#             if len(elem) > max_length:
#                 max_length = len(elem)
#                 max_value = elem
#
#     print(f"max_length: {max_length}\tmax_value: {max_value}")
#     return max_length

# didnt work in case palindrome is on the left or right side of the middle char and middle char is not part of palindrome
# class Solution:
#
#     def longestPalinSubseq(self, S):
#
#         def check_palindrome(value):
#             start = 0
#             end = len(value)-1
#             while start <= end:
#                 if value[start] == value[end]:
#                     start += 1
#                     end -= 1
#                 else:
#                     return False
#
#             return True
#
#         mid = len(S) // 2
#         ret_string = S[mid]
#         L = mid - 1
#         R = mid + 1
#         print(f"Start - L: {L}\tR:{R}\t\t\n"
#               f"ret_string: {ret_string}")
#         while L > 0 or R < len(S):
#             print(f"L: {L}\tR:{R}\t\t{S[L]}-{S[R]}\n"
#                   f"ret_string: {ret_string}")
#             if L >=0:
#                 new_string = S[L] + ret_string + S[R]
#             else:
#                 new_string = ret_string + S[R]
#
#             if R <= len(S)-1:
#                 new_string = S[L] + ret_string + S[R]
#             else:
#                 new_string = S[L] + ret_string
#
#             print(f"base- new_string: {new_string}\n\n")
#             if check_palindrome(new_string):
#                 ret_string = new_string
#                 L -= 1
#                 R += 1
#             else:
#                 traverse_R = R+1
#                 traverse_found = 0
#                 while traverse_R < len(S):
#                     new_string = S[L] + ret_string + S[traverse_R]
#                     print(f"Right traverse- new_string: {new_string}")
#                     if check_palindrome(new_string):
#                         traverse_found = 1
#                         ret_string = new_string
#                         L -= 1
#                         R = traverse_R+1
#                         break
#
#                     traverse_R += 1
#
#                 print(f"After Right traverse L: {L}\tR:{R}\t\t{S[L]}-{S[R]}\ttraverse_found:{traverse_found}\n"
#                       f"ret_string: {ret_string}")
#                 traverse_L = L-1
#                 while traverse_L >= 0:
#                     new_string = S[traverse_L] + ret_string + S[R]
#                     print(f"Left traverse- new_string: {new_string}")
#                     if check_palindrome(new_string):
#                         traverse_found = 1
#                         ret_string = new_string
#                         L = traverse_L-1
#                         R += 1
#                         break
#
#                     traverse_L -= 1
#
#                 print(f"After Left traverse L: {L}\tR:{R}\t\t{S[L]}-{S[R]}\ttraverse_found:{traverse_found}\n"
#                       f"ret_string: {ret_string}\n\n")
#
#                 if traverse_found == 0:
#                     L -= 1
#                     R += 1
#
#         # if only one character in the ret string then check the mid+1 and mid-1 as palindrome
#         if len(ret_string) == 1:
#             if mid+1 < len(S):
#                 new_string = ret_string + S[mid+1]
#                 print(f"Right to Mid- new_string: {new_string}")
#                 if check_palindrome(new_string):
#                     ret_string = new_string
#                     print(ret_string)
#                     return len(ret_string)
#
#             if mid-1 > 0:
#                 new_string = S[mid-1] + ret_string
#                 print(f"Left to Mid- new_string: {new_string}")
#                 if check_palindrome(new_string):
#                     ret_string = new_string
#                     print(ret_string)
#                     return len(ret_string)
#
#         print(ret_string)
#         return len(ret_string)

# if we take from first and last character it is not working
# class Solution:
#
#     def longestPalinSubseq(self, S):
#
#         def check_palindrome(value):
#             start = 0
#             end = len(value)-1
#             while start <= end:
#                 if value[start] == value[end]:
#                     start += 1
#                     end -= 1
#                 else:
#                     return False
#
#             return True
#
#         L = 0
#         R = len(S)-1
#         ret_string = ""
#         print(f"Start - L: {L}\tR:{R}\t\t\n"
#               f"ret_string: {ret_string}")
#         while L > 0 or R < len(S):
#             print(f"L: {L}\tR:{R}\t\t{S[L]}-{S[R]}\n"
#                   f"ret_string: {ret_string}")
#             if L >=0:
#                 new_string = ret_string[0:L] + S[L] + S[R] + ret_string[L:]
#             else:
#                 new_string = ret_string[:] + S[R]
#
#             if R <= len(S)-1:
#                 new_string = ret_string[0:L] + S[L] + S[R] + ret_string[L:]
#             else:
#                 new_string = S[L] + ret_string[:]
#
#             print(f"base- new_string: {new_string}\n\n")
#             if check_palindrome(new_string):
#                 ret_string = new_string
#                 L += 1
#                 R -= 1
#             else:
#                 traverse_R = R-1
#                 traverse_found = 0
#                 while traverse_R < len(S):
#                     new_string = ret_string[0:L] + S[L] + S[traverse_R] + ret_string[L:]
#                     print(f"Right traverse- new_string: {new_string}")
#                     if check_palindrome(new_string):
#                         traverse_found = 1
#                         ret_string = new_string
#                         L += 1
#                         R = traverse_R-1
#                         break
#
#                     traverse_R -= 1
#
#                 print(f"After Right traverse L: {L}\tR:{R}\t\t{S[L]}-{S[R]}\ttraverse_found:{traverse_found}\n"
#                       f"ret_string: {ret_string}")
#                 traverse_L = L+1
#                 while traverse_L >= 0:
#                     new_string = ret_string[0:traverse_L] + S[traverse_L] + S[traverse_R] + ret_string[L:]
#                     print(f"Left traverse- new_string: {new_string}")
#                     if check_palindrome(new_string):
#                         traverse_found = 1
#                         ret_string = new_string
#                         L = traverse_L+1
#                         R -= 1
#                         break
#
#                     traverse_L += 1
#
#                 print(f"After Left traverse L: {L}\tR:{R}\t\t{S[L]}-{S[R]}\ttraverse_found:{traverse_found}\n"
#                       f"ret_string: {ret_string}\n\n")
#
#                 if traverse_found == 0:
#                     L += 1
#                     R -= 1
#
#         print(ret_string)
#         return len(ret_string)

class Solution:

    def longestPalinSubseq(self, S):
        sum = 0
        dict_res = {}
        ret_string = ""
        def rec_helper(L, R, sum, ret_string):
            cur_key = str(L)+'-'+str(R)
            print(f"L: {L}, R:{R}, sum: {sum}\tret_string: {ret_string}")
            if cur_key in dict_res:
                return dict_res[cur_key]

            if L > R:
                dict_res[cur_key] = sum, ret_string
                return dict_res[cur_key]

            # base case when both indexes at same position
            if L == R:
                sum = 1
                ret_string = S[L]
                dict_res[cur_key] = sum, ret_string
                return dict_res[cur_key]

            if S[L] == S[R]:
                ret_string = S[L] + rec_helper(L+1, R-1, sum, ret_string)[1] + S[R]
                sum = 2 + rec_helper(L+1, R-1, sum, ret_string)[0]
                dict_res[cur_key] = sum, ret_string
                # return dict_res[cur_key]
            else:
                sum = max(rec_helper(L+1, R, sum, ret_string)[0], rec_helper(L, R-1, sum, ret_string)[0])
                ret_string = rec_helper(L+1, R, sum, ret_string)[1] if rec_helper(L+1, R, sum, ret_string)[0] > rec_helper(L, R-1, sum, ret_string)[0] else rec_helper(L, R-1, sum, ret_string)[1]
                dict_res[cur_key] = sum, ret_string
                # return dict_res[cur_key]

            return dict_res[cur_key]

        sum, ret_string = rec_helper(0, len(S)-1, sum, ret_string)
        print(f"sum: {sum}\tret_string: {ret_string}")
        return sum

'''
    pwnnb
                                                                     (0,4)
                                    (1,4)                                                           (0,3)
                (2,4)                               (1,3)                           (1,3)                               (0,2)
      (3,4)                  (2,3)           (2,3)           (1,2)            (2,3)           (1,2)              (1,2)             (0,1)
  (4,4)   (3,3)              (3,2)       (2,2)    (2,2)   (2,2)   (1,1)       (3,2)       (2,2)   (1,1)     (2,2)   (1,1)     (0,0)    (1,1)


'''

if __name__ == '__main__':
    no_of_tests = int(input("No of tests: "))
    # bbabcbcab - 7
    # vtvvv - 4
    # pwnnb - 2
    # ttbtctcbt - 7
    for i in range(no_of_tests):
        input_string = input("Enter String: ")
        solution = Solution()
        result = solution.longestPalinSubseq(input_string)
        # longest_palindrome(input_string)
        print(f"result: {result}")