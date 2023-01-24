'''
Given a matrix of characters a-z and a word, return a boolean as to whether the word can be found within the matrix.
Words can only be built from adjacent letters (up, down, left, right), but not diagonals.
Same elements cannot be used multiple times in the same word.

Input: Matrix of characters from a-z, String word
Output: Boolean as to whether word can be found in matrix

Example
Input:
[['a', 'b', 'c', 'd'],
 ['e', 'f', 'g', 'h'],
 ['i', 'd', 'o', 'j'],
 ['k', 'l', 'm', 'n']]

'dog'
Output: true

Constraints
Where M = matrix height, N = matrix width, L = length of word

Time Complexity: O(MN * 3^L)
Auxiliary Space Complexity: O(MN)

Notes (Only give if asked; or as tools to help guide interviewee if he/she is stuck)
There'll be at least one character inside the matrix
All elements of the matrix will be single characters of lowercase a-z; no capitalized to worry about. Can assume valid input
Second argument will be at least one character long (can assume valid input here as well)
Duplicates can exist inside matrix; duplicates can exist inside target word

https://leetcode.com/problems/word-search/

'''
class Solution:
    def exist(self, board, word):

        max_rows = len(board)
        max_cols = len(board[0])

        # All Passed
        def helper(row, col, index, word_found):
            print(f"row: {row}\tcol:{col}\tindex:{index}\t\n"
                      f"{visited_nodes}"
                      )
            if len(word) == index:
                value_found.append(True)
                word_found = True
                return

            if row < 0 or row >= max_rows or col < 0 or col >= max_cols:
                return

            if visited_nodes[row][col] == 1:
                return

            if len(word) - 1 >= index and board[row][col] != word[index]:
                return

                # If I remove this then Time Limit Exceeded happens
            if word_found:
                return

            visited_nodes[row][col] = 1
            up = helper(row - 1, col, index+1, word_found)
            down = helper(row+1, col, index+1, word_found)
            left = helper(row, col-1, index+1, word_found)
            right = helper(row, col+1, index+1, word_found)

            visited_nodes[row][col] = 0

        # 46/85 passed  Time Limit Exceeded
        def helper_orig(row, col, word, parent_word_length, path):

            print(f"------\n"
                  f"row: {row}\tcol:{col}\tword:{word}\tparent_word_length:{parent_word_length}\n"
                  f"{visited_nodes}\n"
                  f"path: {path}"
                  f"------"
                  )
            print(f"Check Range")
            if row < 0 or row >= max_rows or col < 0 or col >= max_cols:
                return word, parent_word_length, path[:-1]

            print(f"Check if unMatch word")
            # if parent_word_length > len(word[1:]) and board[row][col] != word[1]:
            if parent_word_length and len(word) != 0 and board[row][col] != word[0]:
                # parent_word_length = False
                return word, parent_word_length, path[:-1]

            print(f"Check already visited")
            if visited_nodes[row][col] == 1:
                return word, parent_word_length, path[:-1]

            print(f"Check if match word")
            if len(word) != 0 and board[row][col] == word[0]:
                parent_word_length = True
                word = word[1:]

            print(f"Check if word found")
            if len(word) == 0:
                print(f"Value Found\n"
                      f"row: {row}\tcol:{col}\tword:{word}\tparent_word_length:{parent_word_length}\n\n")
                value_found.append(True)
                complete_path.append(path)
                # parent_word_length = False
                return word, parent_word_length, path[:-1]   #

            if True in value_found:
                return word, parent_word_length, path[:-1]  #

            visited_nodes[row][col] = 1

            # Up
            print(f"UP")
            path.append("U")
            up = helper_orig(row-1, col, word, parent_word_length, path)

            # Down
            print(f"DOWN")
            path.append("D")
            down = helper_orig(row+1, col, word, parent_word_length, path) # up[0], up[1], up[2])  # [0] up[1]

            # Left
            print(f"LEFT")
            path.append("L")
            left = helper_orig(row, col-1, word, parent_word_length, path)  # down[0], down[1], down[2])   # [0] down[1]

            # Right
            print(f"RIGHT")
            path.append("R")
            right = helper_orig(row, col+1, word, parent_word_length, path)  # left[0], left[1], left[2])   # [0] left[1]

            visited_nodes[row][col] = 0

            return right[0], right[1], right[2][:-1]   #[0], parent_word_length # right[1]

        value_found = []
        path = []
        complete_path = []
        word_found = False

        for row in range(max_rows):
            for col in range(max_cols):
                visited_nodes = [[0 for _ in range(max_cols)] for _ in range(max_rows)]
                print(f"****************************\n"
                      f"row: {row}\tcol:{col}\n"
                      f"visited_nodes: {visited_nodes}")
                # helper_orig(row, col, word, False, path)
                # print(f"complete_path:{complete_path}")
                helper(row, col, 0, word_found)   # word, False
                if True in value_found:
                    return True

        return False

if __name__ == '__main__':
    mat = [["a"]]
        # [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        # [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],
         #  ["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]  # AAAAAAAAAAAAAAB
        # [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]  # ABCESEEEFS
        # [["a","b"],["c","d"]]  # cdba
        # [["a","b"]] # ba - True
        # [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] # ABCB
        # [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] ABCCED True
    '''
            0   1   2   3
        0[["A","B","C","E"],
        1 ["S","F","C","S"],
        2 ["A","D","E","E"]]
         ABCB

    '''
    target = input("Enter word to be searched: ")
    solution = Solution()
    result = solution.exist(mat, target)

    print(f"result: {result}")