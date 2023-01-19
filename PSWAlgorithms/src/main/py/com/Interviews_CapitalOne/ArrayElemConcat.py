# Given an array of integers calculate all possible a[i] * a[j] where it represents concatenation of values
# at index i and j. Take Sum of all such concats and return as output


def solution(a):
    sum = 0
    total_length = len(a)
    for row_index in range(0, len(a)):
        for col_index in range(row_index, total_length):
            if col_index == row_index:
                sum += int(str(a[row_index]) + str(a[col_index]))
            else:
                sum += int(str(a[row_index]) + str(a[col_index])) + int(str(a[col_index]) + str(a[row_index]))
            print('col', col_index, sum)
        # total_length = total_length - 1
        print(row_index, sum)

    return sum


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    # [1, 2, 3]
    # [10, 2] ->  1344
    # [10, 2] -> [10, 2
    #              2, 10]  -> 1010 + 102 + 22 + 210 = 1344
    # [1, 2, 3] = 198
    # [1, 2, 3, 4]
    # [1, 2, 3, 4] -> [1, 2, 3, 4
    #                  2, 3, 4, 1
    #                  3, 4, 1, 2
    #                  4, 1, 2, 3] = 11 + 12 + 13 + 14 + 23 + 24 + 21 + 34 + 32 + 31 + 43 + 42 + 41

    output = solution(a)
    print(output)