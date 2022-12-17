'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 1:


'''

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        total_rows = len(board)
        total_cols = len(board[0])
        path = set()

        def check_existence(row, col, index):
            # print(f"row: {row}-col: {col}\t"
            #       f"index: {index} \t len(word): {len(word)}\t"
            #       )

            if index == len(word):
                return True

            if (row < 0) or (col < 0) or (row >= total_rows) or (col >= total_cols) \
                    or (word[index] != board[row][col]) or ((row, col) in path):
                return False

            path.add((row, col))

            result = (check_existence(row+1, col, index+1) or check_existence(row-1, col, index+1) \
                     or check_existence(row, col+1, index+1) or check_existence(row, col-1, index+1))

            # # Right check
            # final_word_right = check_existence(row, col+1, index+1)
            # print(f"final_word_right: {final_word_right}")
            #
            # # Left check
            # final_word_left = check_existence(row, col-1, index+1)
            # print(f"final_word_left: {final_word_left}")
            #
            # # up check
            # final_word_up = check_existence(row-1, col, index+1)
            # print(f"final_word_up: {final_word_up}")
            #
            # # Down check
            # final_word_down = check_existence(row+1, col, index+1)
            # print(f"final_word_down: {final_word_down}")

            path.remove((row, col))
            return result
                       # (final_word_right) | (final_word_down) | (final_word_left) | (final_word_up)

        for row in range(total_rows):
            for col in range(total_cols):
                if check_existence(row, col, 0):
                    return True

        return False

if __name__ == '__main__':
    # rows = int(input("Enter rows: "))
    # cols = int(input("Enter cols: "))

    # matrix_board = [['' for col in range(cols)] for row in range(rows)]
    # for row in range(rows):
    #     for col in range(cols):
    #         matrix_board[row][col] = input(f"Enter Element for {row}-{col}: ")
    # word = input("Enter word: ")
    matrix_board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"

    solution = Solution()
    final_Result = solution.exist(matrix_board, word)
    print(f"final_Result: {final_Result}")