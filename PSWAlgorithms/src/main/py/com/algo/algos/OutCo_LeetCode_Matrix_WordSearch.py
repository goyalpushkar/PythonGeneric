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

        def helper(row, col, word, parent_word_length):

            print(f"row: {row}\tcol:{col}\tword:{word}\tparent_word_length:{parent_word_length}")
            if row < 0 or row >= max_rows or col < 0 or col >= max_cols or visited_nodes[row][col] == 1:
                return word, parent_word_length

            visited_nodes[row][col] = 1

            # print(f"Check if unMatch word")
            if parent_word_length > len(word[1:]) and board[row][col] != word[1]:
                return word, parent_word_length

            print(f"Match word")
            if len(word) != 0 and board[row][col] == word[0]:
                word = word[1:]

            print(f"Check if word found")
            if len(word) == 0:
                print(f"Value Found\n"
                      f"row: {row}\tcol:{col}\tword:{word}\tparent_word_length:{parent_word_length}\n\n")
                value_found.append(True)
                return word, parent_word_length

            # Up
            print(f"UP")
            up = helper(row-1, col, word, parent_word_length)

            # Down
            print(f"DOWN")
            down = helper(row+1, col, up[0], up[1])

            # Left
            print(f"LEFT")
            left = helper(row, col-1, down[0], down[1])

            # Right
            print(f"RIGHT")
            right = helper(row, col+1, left[0], left[1])

            visited_nodes[row][col] = 0

            return right[0], right[1]

        visited_nodes = [[0 for _ in range(max_cols)] for _ in range(max_rows)]
        value_found = []
        helper(0, 0, word, len(word))
        if True in value_found:
            return True

        return False

if __name__ == '__main__':
    mat = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] # ABCB
        # [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] ABCCED True
    target = input("Enter word to be searched: ")
    solution = Solution()
    result = solution.exist(mat, target)

    print(f"result: {result}")