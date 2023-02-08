import os
import sys

abspath = os.path.abspath(__file__)
realpath = os.path.realpath(__file__)
basename = os.path.basename(__file__)
dirname = os.path.dirname(__file__)
parentdir = os.path.dirname(dirname)
# grandparentdir = os.path.dirname(parentdir)
# print(f"abspath: {abspath}\nrealpath: {realpath}\ndirname: {dirname}\nbasename: {basename}\n"
#       f"parentdir: {parentdir}\ngrandparentdir: {grandparentdir}")
sys.path.append(parentdir)
# sys.path.append(grandparentdir)

# from LeetCode_BullsAndCows import Solution
from algos.LeetCode_Search_FinMin_inRotatedSearchArray import Solution
from Algos_Strings.HR_SpecialStringAgain import Solution
from Algos_GreedyAlgorithms.HR_MinAbsDiffInArray import Solution
from Algos_GreedyAlgorithms.HR_ReverseShuffleMerge import Solution

# 2 Strings test case
def two_strings():
    s = int(input("Enter Secret: "))
    t = int(input("Enter Guess: "))

    sol = Solution()
    final_result = sol.getHint(s, t)
    print(f"final_result: {final_result}\n")


# Array and number test case
def array_number():
    s = list(map(int, input("Enter array as space-separated values: ").split(",")))
    t = int(input("Enter target: "))
    print(f"s: {s} \t t: {t}")
    sol = Solution()
    final_result = sol.find_min_1st(s)
        #sol.search(s, t)
    print(f"final_result: {final_result}\n")


# String and number test case
def string_number():
    s = input("Enter string: ")
    t = int(input("Enter number: "))
    print(f"s: {s} \t t: {t}")
    sol = Solution()
    final_result = sol.substrCount(t, s)
        #sol.search(s, t)
    print(f"final_result: {final_result}\n")


# Array only test case
def array_only():
    s = list(map(int, input("Enter array as space-separated values: ").split(",")))
    print(f"s: {s}")
    sol = Solution()
    final_result = sol.minimumAbsoluteDifference(s)
        #sol.search(s, t)
    print(f"final_result: {final_result}\n")

# String only test case
def string_only():
    s = input("Enter string value: ")
    print(f"s: {s}")
    sol = Solution()
    final_result = sol.reverseShuffleMerge(s)
        #sol.search(s, t)
    print(f"final_result: {final_result}\n")


if __name__ == '__main__':
    n = int(input("Enter no of test cases: "))

    for i in range(n):
        # string_number()
        # array_only()
        string_only()

