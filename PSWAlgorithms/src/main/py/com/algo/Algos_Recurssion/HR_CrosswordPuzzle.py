'''
A  Crossword grid is provided to you, along with a set of words (or names of places) which need to be filled into the grid. Cells are marked either + or -. Cells marked with a - are to be filled with the word list.

The following shows an example crossword from the input  grid and the list of words to fit, :

Input 	   		Output

++++++++++ 		++++++++++
+------+++ 		+POLAND+++
+++-++++++ 		+++H++++++
+++-++++++ 		+++A++++++
+++-----++ 		+++SPAIN++
+++-++-+++ 		+++A++N+++
++++++-+++ 		++++++D+++
++++++-+++ 		++++++I+++
++++++-+++ 		++++++A+++
++++++++++ 		++++++++++
POLAND;LHASA;SPAIN;INDIA
Function Description

Complete the crosswordPuzzle function in the editor below. It should return an array of strings, each representing a row of the finished puzzle.

crosswordPuzzle has the following parameter(s):

crossword: an array of  strings of length  representing the empty grid
words: a string consisting of semicolon delimited strings to fit into
Input Format

Each of the first  lines represents , each of which has  characters, .

The last line contains a string consisting of semicolon delimited  to fit.

Constraints




Output Format

Position the words appropriately in the  grid, then return your array of strings for printing.

Sample Input 0

+-++++++++
+-++++++++
+-++++++++
+-----++++
+-+++-++++
+-+++-++++
+++++-++++
++------++
+++++-++++
+++++-++++
LONDON;DELHI;ICELAND;ANKARA
Sample Output 0

+L++++++++
+O++++++++
+N++++++++
+DELHI++++
+O+++C++++
+N+++E++++
+++++L++++
++ANKARA++
+++++N++++
+++++D++++
Sample Input 1

+-++++++++
+-++++++++
+-------++
+-++++++++
+-++++++++
+------+++
+-+++-++++
+++++-++++
+++++-++++
++++++++++
AGRA;NORWAY;ENGLAND;GWALIOR
Sample Output 1

+E++++++++
+N++++++++
+GWALIOR++
+L++++++++
+A++++++++
+NORWAY+++
+D+++G++++
+++++R++++
+++++A++++
++++++++++
Sample Input 2

XXXXXX-XXX
XX------XX
XXXXXX-XXX
XXXXXX-XXX
XXX------X
XXXXXX-X-X
XXXXXX-X-X
XXXXXXXX-X
XXXXXXXX-X
XXXXXXXX-X
ICELAND;MEXICO;PANAMA;ALMATY
Sample Output 2

XXXXXXIXXX
XXMEXICOXX
XXXXXXEXXX
XXXXXXLXXX
XXXPANAMAX
XXXXXXNXLX
XXXXXXDXMX
XXXXXXXXAX
XXXXXXXXTX
XXXXXXXXYX
'''

#!/bin/python3

import math
import os
import random
import re
import sys


'''
#!/bin/python3
import sys


# print board
def print_board(board):
	for row in board:
		print(''.join(row))


# get possible locations
def get_poss_locs(board, word):
	poss_locs = []
	length = len(word)
    # horizontal possible location
	for i in range(10):
		for j in range(10 - length + 1):
			good = True
			for k in range(len(word)):
				if board[i][j + k] not in ['-', word[k]]:
					good = False
					break
			if good:
				yield (i, j, 0) # 0 is axis indicator
    # vertical possible location
	for i in range(10 - length + 1):
		for j in range(10):
			good = True
			for k in range(len(word)):
				if board[i + k][j] not in ['-', word[k]]:
					good = False
					break
			if good:
				yield (i, j, 1) # 1 is axis indicator


# revert move
def revert(board, word, loc):
	i, j, axis = loc
	if axis == 0: # axis 0 is horizontal
		for k in range(len(word)):
			board[i][j + k] = '-'
	else: # axis 1 is vertical
		for k in range(len(word)):
			board[i + k][j] = '-'

# write the word on board at specified loc
def move(board, word, loc):
	i, j, axis = loc
	if axis == 0:
		for k in range(len(word)):
			board[i][j + k] = word[k]
	else:
		for k in range(len(word)):
			board[i + k][j] = word[k]


def solve(board, words):
	global solved

	if len(words) == 0:
		if not solved:
			print_board(board)
		solved = True
		return

	word = words.pop()
	pos_locs = [loc for loc in get_poss_locs(board, word)]

	for loc in pos_locs:
		move(board, word, loc)
		solve(board, words)
		revert(board, word, loc)

	words.append(word)


if __name__ == "__main__":
    board = []
    for _ in range(10):
        board.append(list(input()))
    words = str(input()).split(";")

    solved = False
    solve(board, words)
'''


# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):

    #return 0

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []
    for _ in range(10):
        crossword_item = input("Line for crossword: ")
        crossword.append(crossword_item)

    words = input("Words: ")

    result = crosswordPuzzle(crossword, words)
    print('\n'.join(result))
    print('\n')
    #fptr.write('\n'.join(result))
    #fptr.write('\n')

    #fptr.close()
