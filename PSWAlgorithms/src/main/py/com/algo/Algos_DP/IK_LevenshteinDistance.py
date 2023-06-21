'''
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
The minimum number of steps required to convert word1 to word2 with the given set of allowed operations is
 called edit distance. e.g. Minimum edit distance between the words 'kitten' and 'sitting', is 3.

kitten → sitten (substitution of "s" for "k")
sitten → sittin (substitution of "i" for "e")
sittin → sitting (insertion of "g" at the end)
Read more about edit distance here.

Example One
{
"word1": "cat",
"word2": "bat"
}
Output:
1

Example Two
{
"word1": "qwe",
"word2": "q"
}
Output:
2
Notes
Constraints:

1 <= length of the strings word1 and word2 <= 105
word1 and word2 contains lower case alphabets from 'a' to 'z'.
'''


def levenshtein_distance(word1, word2):
    """
    Args:
     word1(str)
     word2(str)
    Returns:
     int32
    """
    # Write your code here.
    rows = len(word1) + 1
    cols = len(word2) + 1
    tab = [[0 for _ in range(cols)] for _ in range(rows)]

    # print(tab)
    for row_index in range(rows):
        for col_index in range(cols):
            if row_index == 0:
                tab[row_index][col_index] = col_index
                continue

            if col_index == 0:
                tab[row_index][col_index] = row_index
                continue

            if word1[row_index - 1] == word2[col_index - 1]:
                cost = 0
            else:
                cost = 1

            # print(row_index, col_index, cost, tab)
            tab[row_index][col_index] = min(tab[row_index - 1][col_index] + 1  # Insert
                                            , tab[row_index][col_index - 1] + 1  # Delete
                                            , tab[row_index - 1][col_index - 1] + cost)  # Replace

    return tab[-1][-1]

# it didnt work not sure where is it wrong
import math
def levenshtein_distance_rec(word1, word2):
    """
    Args:
     word1(str)
     word2(str)
    Returns:
     int32
    """
    rows = len(word1)
    cols = len(word2)
    memo = {}
    def editdistance_rec(first_idx, second_idx):
        key = str(first_idx)+"_"+str(second_idx)

        if key in memo:
            return memo[key]

        if first_idx > rows or second_idx > cols:
            return math.inf

        if first_idx == rows or second_idx == cols:
            return 0

        if word1[first_idx] == word2[second_idx]:
            cost = 0
        else:
            cost = 1

        distance = min( 1+editdistance_rec(first_idx+1, second_idx)  # Delete
                       ,1+editdistance_rec(first_idx, second_idx+1)  # Insert
                       ,cost+editdistance_rec(first_idx+1, second_idx+1)   # Replace
                        )

        memo[key] = distance

        return memo[key]

    return editdistance_rec(0, 0)