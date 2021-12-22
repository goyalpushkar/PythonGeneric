'''
Longest subsequence between 2 strings

f( xi, yj) = {
                0                               for i = 0 & j 0 to len, j = 0 & i = 0 to len
                (xi-1, yj-1) ^ xi               if xi = yj
                max( f(xi-1, yj), f(xi, yj-1)   if xi <> yj
            }
'''

def longest_subsequence_size(str1, str2):
    print("Get Length")
    table_values = [ [0 for j in range(len(str2)+1)]  for i in range(len(str1)+1)]

    for i in range(len(str1)+1):
        table_values[i][0] = 0

    for j in range(len(str2)+1):
        table_values[0][j] = 0

    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1] == str2[j-1]:
                table_values[i][j] = table_values[i-1][j-1] + 1
            else:
                table_values[i][j] = max( table_values[i - 1][j], table_values[i][j - 1] )

    return ( table_values[len(str1)][len(str2)], table_values )

def longest_subsequence(str1, str2):
    print("Get Sequences")
    table_values = [["" for j in range(len(str2)+1)] for i in range(len(str1)+1)]

    for i in range(len(str1)+1):
        table_values[i][0] = ""

    for j in range(len(str2)+1):
        table_values[0][j] = ""

    #print(table_values)
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1] == str2[j-1]:
                table_values[i][j] = table_values[i-1][j-1] + str1[i]
            elif len(table_values[i - 1][j]) >= len(table_values[i][j - 1]):
                table_values[i][j] = table_values[i - 1][j]
            elif len(table_values[i - 1][j]) <= len(table_values[i][j - 1]):
                table_values[i][j] = table_values[i][j - 1]

    #print(table_values)
    return table_values[len(str1)][len(str2)]

def longest_subsequence_all(table_values, str1, str2, i, j, return_arr):
    print("Get All Sequences - " + str(i) + ":" + str(j))

    if i==0 or j==0:
        return ""

    if str1[i] == str2[j]:
        return [values + str1[i] for values in longest_subsequence_all(table_values, str1, str2, i-1, j-1, return_arr)]

    #return_arr = []
    print(return_arr)
    if table_values[i - 1][j] >= table_values[i][j - 1]:
        return_arr.append(longest_subsequence_all(table_values, str1, str2, i-1, j, return_arr))

    if table_values[i - 1][j] <= table_values[i][j - 1]:
        return_arr.append(longest_subsequence_all(table_values, str1, str2, i, j-1, return_arr))

    return return_arr

if __name__ == '__main__':
    test_cases = int(input("No of test cases: "))
    for index in range(test_cases):
        (str1, str2) = input("Enter comma seperated sequences: ").rstrip().split()

        (longest_length, matrix) = longest_subsequence_size(str1, str2)
        longest_sub = longest_subsequence(str1, str2)
        print("Longest Common subsequence length: " + str(longest_length)   + " : " + longest_sub )

        print(matrix)

        return_arr = []
        all_subsequences = longest_subsequence_all( matrix, str1, str2, len(str1), len(str2), return_arr)
        print("Longest Common subsequences: " + all_subsequences)