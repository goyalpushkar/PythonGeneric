'''
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate the span of stock’s price for all n days.
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, N is the size of the array. The second line of each test case contains N input C[i].

Output:
For each testcase, print the span values for all days.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 200
1 ≤ C[i] ≤ 800

Example:
Input:
2
7
100 80 60 70 60 75 85
6
10 4 5 90 120 80

Output:
1 1 1 2 1 4 6
1 1 2 4 5 1
'''


def stock_span(array_size, array):

    window_size = {}
    return_array = [1]
    for index in range(1, array_size):
        window_size = 1
        for prev in range(index - 1, -1, -1):
            if array[prev] <= array[index]:
                window_size += 1
            else:
                break

        return_array.append(window_size)

    return " ".join(map(str, return_array))


if __name__ == '__main__':
    t = int(input("No of test case: "))
    for index in range(t):
        array_size = int(input("Array Size: "))
        array = list(map(int, input("Values: ").strip().split()))

        output_result = stock_span(array_size, array)
        print(output_result)
