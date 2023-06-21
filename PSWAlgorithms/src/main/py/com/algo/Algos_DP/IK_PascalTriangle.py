'''
Pascal’s triangle is a triangular array of the binomial coefficients. Write a function that takes an integer value n as input and returns a two-dimensional array representing pascal’s triangle.

pascalTriangleArray is a two-dimensional array of size n * n, where
pascalTriangleArray[i][j] = BinomialCoefficient(i, j); if j <= i,
pascalTriangleArray[i][j] = 0; if j > i

Example
{
"n": 4
}

Output:
[
[1],
[1, 1],
[1, 2, 1],
[1, 3, 3, 1]
]
Notes
All values in the 2D output array result must be modulo with (109 + 7) and size of result[i] for 0 <= i < n should be (i + 1) i.e. 0s for pascalTriangleArray[i][j] = 0; if j > i, should be ignored.

Constraints:
1 <= n <= 1700
'''


def find_pascal_triangle(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    if n == 0:
        return []

    tab = [[] for _ in range(n)]

    for row in range(n):
        for col in range(row + 1):
            if col == 0 or col == row:
                tab[row].append(1)
            else:
                tab[row].append((tab[row - 1][col] + tab[row - 1][col - 1]) % (10 ** 9 + 7))

    return tab