'''

'''

import sys
from _collections import deque

sys.setrecursionlimit(100000)
def min_matrix_multiplication(arr):
    print("DP")
    #print(arr)
    matrix_table = [[sys.maxsize for col in range(len(arr))] for row in range(len(arr))]
    cost_table = [[sys.maxsize for col in range(len(arr))] for row in range(len(arr))]
    #min_matrix_multiplication.passed_arr = arr

    for row in range(len(arr)):
        for col in range(len(arr)):
            if row == 0:
                matrix_table[row][col] = 0
                cost_table[row][col] = 0

            if col == 0:
                matrix_table[row][col] = 0
                cost_table[row][col] = 0

            if row == col:
                matrix_table[row][col] = 0
                cost_table[row][col] = 0

    #print(matrix_table)
    #print(cost_table)
    for diagonal in range(1, len(arr)-1):
        for i in range(1, len(arr)-diagonal):
            j = i + diagonal
            #print("diagonal - " + str(diagonal) + " :i - " + str(i) + " :j - " + str(j))
            matrix_table[i][j] = sys.maxsize
            for k in range(i, j):
                #print("k - " + str(k))
                total_cost = matrix_table[i][k] + matrix_table[k+1][j] + (arr[i-1] * arr[k] * arr[j])

                if matrix_table[i][j] > total_cost:
                    #min_cost = total_cost
                    matrix_table[i][j] = total_cost
                    cost_table[i][j] = k

                #print("total_cost - " + str(total_cost))

    print(matrix_table)
    print(cost_table)
    print(cost_table[1][len(arr)-1])
    return matrix_table[1][len(arr)-1]

#Recursive Way
def min_matrix_multiplication_rec(arr, i, j):
    print("Recursive")
    print(arr)
    #print("i - " + str(i) + " :j - " + str(j))
    if i >= j:
        return 0

    min_cost = sys.maxsize
    #print("min_cost: " + str(min_cost))
    for k in range(i, j):
        #print("k: " + str(k))
        total_cost = min_matrix_multiplication_rec(arr, i, k) + min_matrix_multiplication_rec(arr, k + 1, j) + (arr[i-1] * arr[k] * arr[j])

        if min_cost > total_cost:
            # min_cost = total_cost
            min_cost = total_cost

    return min_cost

if __name__ == '__main__':
    test_Cases = int(input("No of test cases: "))
    for index in range(test_Cases):
        arr = list(map(int, input("Matrix Sizes: ").strip().split()))
        result = min_matrix_multiplication_rec(arr, 1, len(arr)-1)
        print(result)

        result = min_matrix_multiplication(arr)
        print(result)