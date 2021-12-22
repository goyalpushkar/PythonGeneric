'''
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1′ into ‘str2′.

Insert
Remove
Replace
All of the above operations are of cost=1.
Both the strings are of lowercase.

Input:
The First line of the input contains an integer T denoting the number of test cases. Then T test cases follow. Each tese case consists of two lines. The first line of each test case consists of two space separated integers P and Q denoting the length of the strings str1 and str2 respectively. The second line of each test case coantains two space separated strings str1 and str2 in order.

Output:
Corresponding to each test case, pirnt in a new line, the minimum number of operations required.

Constraints:
1 <= T <= 50
1 <= P <= 100
1 <= Q <= 100

Example:
Input:
1
4 5
geek gesek

Output:
1

Explanation:
Testcase 1: One operation is required to make 2 strings same i.e. removing 's' from str2.

f(Xi, Yj)  =  { ins,  if y = "" for 0 < i < len(x)
                del,  if i = "" for 0 < j < len(y)
                Xi-1, Yj-1,  if X[i] = Y[j]
                min( (Xi-1, Yj) * Del,
                     (Xi, Yj-1) * Ins,
                     (Xi-1, Yj-1) * Replace
                }
'''

#84 87
#lrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmcoq hnwnkuewhsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcaceh

def edit_distance(str1, str2):
    #print(str1 + " " + str2)
    table_values = [ [ 0 for j in range(len(str2)+1)] for i in range(len(str1)+1) ]

    for i in range(len(str1)+1):
        table_values[i][0] = i

    for j in range(len(str2)+1):
        table_values[0][j] = j

    #print(table_values)
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1] == str2[j-1]:
                table_values[i][j] = table_values[i-1][j-1]
            else:
                table_values[i][j] = min( table_values[i - 1][j]
                                         ,table_values[i][j - 1]
                                         ,table_values[i - 1][j - 1] ) + 1

    print(table_values)
    return table_values[len(str1)][len(str2)]

if __name__ == '__main__':
    test_cases = int(input("No of Test Cases: "))
    for index in range(test_cases):
        string_lengths = map(int, input("String Length: ").rstrip().split())
        strs = input("Strings: ").rstrip().split()

        return_elem = edit_distance(strs[0], strs[1])

        print(return_elem)

