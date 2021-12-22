'''
You are given a square grid with some cells open (.) and some blocked (X). Your playing piece can move along any row or column until it reaches the edge of the grid or a blocked cell. Given a grid, a start and an end position, determine the number of moves it will take to get to the end position.
For example, you are given a grid with sides  described as follows:
...
.X.
...
Your starting position  so you start in the top left corner. The ending position is . The path is . It takes  moves to get to the goal.
Function Description
Complete the minimumMoves function in the editor. It must print an integer denoting the minimum moves required to get from the starting position to the goal.
minimumMoves has the following parameter(s):
grid: an array of strings representing the rows of the grid
startX: an integer
startY: an integer
goalX: an integer
goalY: an integer
Input Format
The first line contains an integer , the size of the array grid.
Each of the next  lines contains a string of length .
The last line contains four space-separated integers,
Constraints


Output Format
Print an integer denoting the minimum number of steps required to move the castle to the goal position.
Sample Input
3
.X.
.X.
...
0 0 0 2
Sample Output
3
Explanation
Here is a path that one could follow in order to reach the destination in  steps:
.
'''

import math
import os
import random
import re
import sys

from collections import deque

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    print(grid)
    minimumMoves.color = [['W' for i in range(len(grid[i]))] for i in range(len(grid))]
    minimumMoves.predecessor = [[(-1,-1) for i in range(len(grid[i]))] for i in range(len(grid))]

    rowSize = len(grid)
    colSize = len(grid[0])
    print(str(rowSize) + " " + str(colSize))

    found = False
    minimumMoves.visited_deque = deque()
    minimumMoves.visited_deque.append((startX, startY))

    #Traverse the grid starting from start position and append in deque
    while len(minimumMoves.visited_deque) > 0 and not found:
        (startPosX, startPosY) = minimumMoves.visited_deque.popleft()
        minimumMoves.color[startX][startY] = 'R'
        print(str(startPosX) + "  " + str(startPosY))
        rowTraversal = traverseRow(grid, startPosY, colSize, startPosX, goalX, goalY)
        print(rowTraversal)
        if rowTraversal:
            found = True
            break

        colTraversal = traverseCol(grid, startPosX, rowSize, startPosY, goalX, goalY)
        print(colTraversal)
        if colTraversal:
            found = True
            break

        print(minimumMoves.predecessor)

    #Take Stack to get the path
    path_deque = deque()
    predecessorX, predecessorY = goalX, goalY
    path_deque.append((predecessorX, predecessorY))
    while predecessorX != -1:
        (predecessorX, predecessorY) = minimumMoves.predecessor[predecessorX][predecessorY]
        path_deque.append((predecessorX, predecessorY))
        if predecessorX == startX and predecessorY == startY:
            break

    print(minimumMoves.color)
    print(minimumMoves.predecessor)
    print(path_deque)
    return len(path_deque) - 1

def traverseRow(grid, col, limit, row, goalX, goalY):
    #Traverse forward
    print("Traverse Row - " + str(col) + " " + str(limit) + " " + str(row))
    for index in range(col+1, limit, 1):
        print("Forward Row: " + str(row) + " " + str(index) + " Value - " + grid[row][index:index+1])
        if grid[row][index:index+1] == 'X':
            break
        else:
            if not checkVisited(minimumMoves.color[row][index]): #grid[row][index:index+1]):
                minimumMoves.visited_deque.append((row, index))
                minimumMoves.color[row][index] = 'G'
                minimumMoves.predecessor[row][index] = (row, col)
                #Check if we reached the destination
                if row == goalX and index == goalY:
                    print("Reached Destination")
                    return True

    # Traverse backward
    for index in range(col-1, -1, -1):
        print("Backward Row: " + str(row) + " " + str(index) +  " Value - " + grid[row][index:index+1])
        if grid[row][index:index+1] == 'X':
            break
        else:
            if not checkVisited(minimumMoves.color[row][index]): #grid[row][index:index+1]):
                minimumMoves.visited_deque.append((row, index))
                minimumMoves.color[row][index] = 'G'
                minimumMoves.predecessor[row][index] = (row, col)
                # Check if we reached the destination
                if row == goalX and index == goalY:
                    print("Reached Destination")
                    return True

    return False

def traverseCol(grid, row, limit, col, goalX, goalY):
    #Traverse forward
    print("Traverse Col - " + str(row) + " " + str(limit) + " " + str(col))
    for index in range(row+1, limit):
        print("Forward Col: "+str(index) + " " + str(col) + " Value - " + grid[index][col:col+1])
        if grid[index][col:col+1] == 'X':
            break
        else:
            if not checkVisited(minimumMoves.color[index][col]): #grid[index][col:col+1]):
                minimumMoves.visited_deque.append((index,col))
                minimumMoves.color[index][col] = 'G'
                minimumMoves.predecessor[index][col] = (row, col)
                # Check if we reached the destination
                if index == goalX and col == goalY:
                    print("Reached Destination")
                    return True

    # Traverse backward
    for index in range(row-1, -1, -1):
        print("Backward Col: "+ str(index) + " " + str(col) + " Value - " + grid[index][col:col+1])
        if grid[index][col:col+1] == 'X':
            break
        else:
            if not checkVisited(minimumMoves.color[index][col]): #grid[index][col:col+1]):
                minimumMoves.visited_deque.append((index, col))
                minimumMoves.color[index][col] = 'G'
                minimumMoves.predecessor[index][col] = (row, col)
                # Check if we reached the destination
                if index == goalX and col == goalY:
                    print("Reached Destination")
                    return True

    return False

def checkVisited(value):
    return value != 'W'


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("Size of Grid: "))

    grid = []
    for _ in range(n):
        grid_item = input()#"Enter Line: "
        grid.append(grid_item)

    startXStartY = input("Enter Start and Destination: ").split()
    startX = int(startXStartY[0])
    startY = int(startXStartY[1])
    goalX = int(startXStartY[2])
    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    print(str(result) + '\n')
    #fptr.write(str(result) + '\n')
    #fptr.close()
