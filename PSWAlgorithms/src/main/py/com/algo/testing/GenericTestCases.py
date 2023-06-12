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
from Algos_SlidingWindow.NeetCode_LongestRepCharReplacement import Solution
from Algos_GreedyAlgorithms.NeetCode_JumpGame import Solution
from Algos_GreedyAlgorithms.NeetCode_GasStation import Solution
from Algos_HeapPriorityQueue.NeetCode_KClosesPointsToOrigin import Solution
from Algos_HeapPriorityQueue.NeetCode_TaskScheduler import Solution
from Algos_BitManipulation.NeetCode_SingleNumber import Solution
from Algos_MathGeometry.NeetCode_HappyNumber import Solution
from Algos_TwoPointers.NeetCode_3Sum import Solution
from Algos_StacksAndQueues.NeetCode_ValidParantheses import Solution
from Algos_Sorting.InterviewCake_MergeSortedArrays import Solution
from Algos_Sorting.IK_SegregateEvenAndOddNum import Solution
from Algos_Sorting.IK_4Sum import Solution
from Algos_Recurssion.IK_TimedTest_PossibleToTargetSum import Solution

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

# 2 Strings test case
def two_lists():
    array_type = input("Enter 1 for int values or 2 for String values: ")
    if array_type == "1":
        s = list(map(int, input("Enter array as comma-separated values: ").split(",")))
    else:
        s = list(input("Enter array as comma-separated values: ").split(","))

    array_type = input("Enter 1 for int values or 2 for String values: ")
    if array_type == "1":
        t = list(map(int, input("Enter array as comma-separated values: ").split(",")))
    else:
        t = list(input("Enter array as comma-separated values: ").split(","))

    sol = Solution()
    final_result = sol.merge_sorted_array(s, t)
    print(f"final_result: {final_result}\n")


# Array and number test case
def array_number():
    array_type = input("Enter 1 for int values or 2 for String values: ")
    if array_type == "1":
        s = list(map(int, input("Enter array as comma-separated values: ").split(",")))
    else:
        s = list(input("Enter array as comma-separated values: ").split(","))

    t = int(input("Enter target: "))
    print(f"s: {s} \t t: {t}")
    sol = Solution()
    final_result = sol.check_if_sum_possible(s, t)
        #sol.search(s, t)
    print(f"final_result: {final_result}\n")

# Array and array test case
def array_array():
    s = list(map(int, input("Enter array as comma-separated values: ").split(",")))
    t = list(map(int, input("Enter array as comma-separated values: ").split(",")))
    print(f"s: {s} \t t: {t}")
    sol = Solution()
    final_result = sol.canCompleteCircuit(s, t)
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
    final_matrix = [[0,1],[1,0]]
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
    final_result = sol.kClosest(final_matrix, numOfCourses)
        #sol.search(s, t)
    print(f"final_result: {final_result}\n")

# String and number test case
def string_number():
    s = input("Enter string: ")
    t = int(input("Enter number: "))
    print(f"s: {s} \t t: {t}")
    sol = Solution()
    final_result = sol.characterReplacement(t, s)
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
    array_type = input("Enter 1 for int values or 2 for String values: ")
    if array_type == "1":
        s = list(map(int, input("Enter array as comma-separated values: ").split(",")))
    else:
        s = list(input("Enter array as comma-separated values: ").split(","))

    print(f"s: {s}")
    sol = Solution()
    final_result = sol.segregate_evens_and_odds(s)
        #sol.search(s, t)
    print(f"final_result: {final_result}\n")


# String only test case
def string_only():
    s = input("Enter string value: ")
    print(f"s: {s}")
    sol = Solution()
    final_result = sol.isValid(s)
        #sol.search(s, t)
    print(f"final_result: {final_result}\n")

# number only test case
def number_only():
    s = int(input("Enter number value: "))
    print(f"s: {s}")
    sol = Solution()
    final_result = sol.isHappy(s)
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
        test_type = input("Enter Test Type: \n"
                          "1. STR_ONLY: string_only\n"
                          "2. NUM_ONLY: number_only\n"
                          "3. ARR_ONLY: array_only\n"
                          "4. MAT_2D: matrix_2d \n"
                          "5. MAT_NUM: matrix_2d_number\n"
                          "6. ARR_NUM: array_number\n"
                          "7. STR_NUM: string_number\n"
                          "8. STR_DICT: string_dict\n"
                          "9. ARR_ARR: array_array\n"
                          "10. TREE_FRM_LST: tree_from_List\n"
                          "11. 2_STRINGS: 2_strings\n"
                          "12. 2_LISTS: 2_LISTS\n"
                          "")
        if test_type == "STR_ONLY" or int(test_type) == 1:
            string_only()
        elif test_type == "NUM_ONLY" or int(test_type) == 2:
            number_only()
        elif test_type == "ARR_ONLY" or int(test_type) == 3:
            array_only()
        elif test_type == "MAT_2D" or int(test_type) == 4:
            matrix_2d()
        elif test_type == "MAT_NUM" or int(test_type) == 5:
            matrix_2d_number()
        elif test_type == "ARR_NUM" or int(test_type) == 6:
            array_number()
        elif test_type == "STR_NUM" or int(test_type) == 7:
            string_number()
        elif test_type == "STR_DICT" or int(test_type) == 8:
            string_dict()
        elif test_type == "ARR_ARR" or int(test_type) == 9:
            array_array()
        elif test_type == "TREE_FRM_LST" or int(test_type) == 10:
            tree_from_List()
        elif test_type == "2_STRINGS" or int(test_type) == 11:
            two_strings()
        elif test_type == "2_LISTS" or int(test_type) == 12:
            two_lists()