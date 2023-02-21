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
from Algos_Backtracking.NeetCode_Subsets2 import Solution
from Algos_Backtracking.NeetCode_CombinationSum import Solution
from Algos_Backtracking.NeetCode_CombinationSum2 import Solution
from Algos_Search.NeetCode_KokoEatingBananas import Solution
from Algos_Search.CCI_SearchinRotatedArray import Solution
from Algos_DP.NeetCode_1D_HouseRobber2 import Solution
from algos.NeetCode_DP_LongestPalindrome import Solution
from Algos_Graphs.NeetCode_MaxAreaOfIsland import Solution
from Algos_Graphs.NeetCode_SurroundedRegions import Solution
from Algos_Graphs.NeetCode_CourseSchedule import Solution
from algos.NeetCode_Recursion_WordBreak import Solution
from Algos_StacksAndQueues.NeetCode_GenerateParantheses import Solution

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
    s = list(map(int, input("Enter array as comma-separated values: ").split(",")))
    t = int(input("Enter target: "))
    print(f"s: {s} \t t: {t}")
    sol = Solution()
    final_result = sol.search(s, t)
        #sol.search(s, t)
    print(f"final_result: {final_result}\n")

# 2D Matrix test case
def matrix_2d():

    final_matrix = [["X","O","X"],["O","X","O"],["X","O","X"]]
        # [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
        # [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        # [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]
    # rows = int(input("Enter no of rows: "))
    # for row in range(rows):
    #     cols = list(map(int, input("Enter cols as comma-separated values: ").split(",")))
    #     final_matrix.append(cols)

    # final_matrix = input("Enter grid: ")
    print(f"final_matrix: {final_matrix} ")
    sol = Solution()
    final_result = sol.solve(final_matrix)
        #sol.search(s, t)
    print(f"final_result: {final_result}\n")

# 2D Matrix and number test case
def matrix_2d_number():

    numOfCourses = int(input("Enter number of courses: "))
    final_matrix = [[1,4],[2,4],[3,1],[3,2]]
        # [["X","O","X"],["O","X","O"],["X","O","X"]]
        # [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
        # [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        # [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]
    # rows = int(input("Enter no of rows: "))
    # for row in range(rows):
    #     cols = list(map(int, input("Enter cols as comma-separated values: ").split(",")))
    #     final_matrix.append(cols)

    # final_matrix = input("Enter grid: ")
    print(f"final_matrix: {final_matrix} ")
    sol = Solution()
    final_result = sol.canFinish(numOfCourses, final_matrix)
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


# String and number test case
def string_dict():
    s = input("Enter string: ")
    t = list(input("Enter comma-separated list of words: ").split(","))
    print(f"s: {s} \t t: {t}")
    sol = Solution()
    final_result = sol.wordBreak_trie(s, t)
        #sol.search(s, t)
    print(f"final_result: {final_result}\n")

# Array only test case
def array_only():
    s = list(map(int, input("Enter array as space-separated values: ").split(",")))
    print(f"s: {s}")
    sol = Solution()
    final_result = sol.rob(s)
        #sol.search(s, t)
    print(f"final_result: {final_result}\n")


# String only test case
def string_only():
    s = input("Enter string value: ")
    print(f"s: {s}")
    sol = Solution()
    final_result = sol.longestPalindrome(s)
        #sol.search(s, t)
    print(f"final_result: {final_result}\n")

# number only test case
def number_only():
    s = int(input("Enter number value: "))
    print(f"s: {s}")
    sol = Solution()
    final_result = sol.generateParenthesis(s)
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
        # matrix_2d_number()
        # matrix_2d()
        # array_number()
        # string_number()
        # string_dict()
        # array_only()
        # string_only()
        # tree_from_List()
        number_only()
