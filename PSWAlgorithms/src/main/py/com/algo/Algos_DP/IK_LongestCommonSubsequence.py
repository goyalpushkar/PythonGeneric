'''
Find the longest common subsequence of two strings.

A subsequence is a sequence that can be derived from another sequence by deleting zero or more 
elements without changing the order of the remaining elements.

Example
{
"a": "ABCDE",
"b": "AECBD"
}
Output:

"ABD"
Subsequence "ABD" can be derived from the first string by deleting characters "C" and "E". From the 
second string it can be derived by deleting "E" and "C". No common subsequence longer than three characters 
exists in the two given strings. "ACD" is another common subsequence of length three; it is also a correct answer.

Notes
If a nonempty common subsequence cannot be found, return "-1".
Constraints:

1 <= length of each of the input strings <= 400
Input strings consist of the alphanumeric characters

ABDEF
BEFDA
'''
def lcs(a, b):
    """
    Args:
    a(str)
    b(str)
    Returns:
    str
    """
    # Write your code here.
    len_a = len(a)
    len_b = len(b)

    tab = [ ["" for j in range(len_b+1)] for i in range(len_a+1)]

    for i in range(1, len_a+1):
        for j in range(1, len_b+1):
            if a[i-1] == b[j-1]:
                tab[i][j] = tab[i-1][j-1] + a[i-1] 
            else:
                tab[i][j] = tab[i-1][j] if len(tab[i-1][j]) > len(tab[i][j-1]) else tab[i][j-1]
                
    return tab[len_a][len_b] if tab[len_a][len_b] != "" else "-1"






# 3 time limit exceeded
def lcs(a, b):
    """
    Args:
    a(str)
    b(str)
    Returns:
    str
    """
    # Write your code here.
    import math
    max_length = 0
    final_string = ""

    mem = {}
    def dfs(i, j, string_so_far):
        nonlocal max_length, final_string
        # print(f"i: {i}, j: {j}, string_so_far: {string_so_far}")
        if i == len(a) or j == len(b):
            if len(string_so_far) > max_length:
                max_length = max(max_length, len(string_so_far))
                final_string = string_so_far
            return
        
        if (i, j) in mem:
            return mem[(i, j)]
            
        if a[i] == b[j]:
            dfs(i+1, j+1, string_so_far+a[i])
        
        else:
            # dfs(i+1, j+1, string_so_far)
            dfs(i, j+1, string_so_far)
            dfs(i+1, j, string_so_far)
            
        return
    
    dfs(0, 0, "")
    
    return "-1" if final_string == "" else final_string

def lcs(a, b):
    """
    Args:
    a(str)
    b(str)
    Returns:
    str
    """
    # Write your code here.
    import math
    final_string = ""

    mem = {}
    def dfs(i, j, string_so_far, final_string):
        # nonlocal max_length
        # print(f"mem: {mem}, i: {i}, j: {j}, string_so_far: {string_so_far}, final_string: {final_string}")
            
        if i == len(a) or j == len(b):
            if len(string_so_far) > len(final_string):
                final_string = string_so_far
            
            mem[(i, j)] = final_string
            return mem[(i, j)]
        
        # if (i, j) in mem:
        #     return mem[(i, j)]
            
        if a[i] == b[j]:
            final_string = dfs(i+1, j+1, string_so_far+a[i], final_string)
        
        else:
            # dfs(i+1, j+1, string_so_far)
            final_string_1 = dfs(i, j+1, string_so_far, final_string)
            final_string_2 = dfs(i+1, j, string_so_far, final_string)
            
            if len(final_string_1) > len(final_string_2):
                final_string = final_string_1
            else:
                final_string = final_string_2
            
        mem[(i, j)] = final_string
        return mem[(i, j)]
    
    final_string = dfs(0, 0, "", "")
    
    return "-1" if final_string == "" else final_string