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
from Algos_Trees.GFG_DiameterTree import Solution
from Algos_DictionariesHashMaps.HR_IceCreamParlor import Solution
from Algos_Search.HR_MaximumSubArraySum import Solution
from Algos_Backtracking.NeetCode_Subsets import Solution

# Node class for a binary tree node
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

# generate tree from list
def deserialize(lst):
    if len(lst) == 0:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] != -1 or lst[i] != 'null':
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        if i + 1 < len(lst) and ( lst[i + 1] != -1 and lst[i+1] != 'null'):
            current.right = TreeNode(lst[i + 1])
            queue.append(current.right)
        i += 2
    return root


# 2 Strings test case
def two_strings():
    s = int(input("Enter Secret: "))
    t = int(input("Enter Guess: "))

    sol = Solution()
    final_result = sol.getHint(s, t)
    print(f"final_result: {final_result}\n")


# Array and number test case
def array_number():
    s = list(map(int, input("Enter array as space-separated values: ").split()))
    t = int(input("Enter target: "))
    print(f"s: {s} \t t: {t}")
    sol = Solution()
    final_result = sol.maximumSum(s, t)
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
    final_result = sol.subsets(s)
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


def tree_from_List():
    compressed_tree = input("Enter List as comma-separated values: ").split(",")
    # compressed_tree = []
    #
    # for _ in range(compressed_tree_count):
    #     compressed_tree_item = int(input().strip())
    #     compressed_tree.append(compressed_tree_item)

    root = deserialize(compressed_tree)
    sol = Solution()
    final_result = sol.diameterOfBinaryTree(root)
    print(f"final_result: {final_result}\n")


if __name__ == '__main__':
    n = int(input("Enter no of test cases: "))

    for i in range(n):
        # array_number()
        # string_number()
        array_only()
        # string_only()
        # tree_from_List()
