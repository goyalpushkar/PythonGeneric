'''
Find all palindromic decompositions of a given string s.

A palindromic decomposition of string is a decomposition of the string into substrings, such that all 
those substrings are valid palindromes.

Example
{
"s": "abracadabra"
}
Output:

["a|b|r|a|c|ada|b|r|a", "a|b|r|aca|d|a|b|r|a", "a|b|r|a|c|a|d|a|b|r|a"]
Notes
Any string is its own substring.
Output should include ALL possible palindromic decompositions of the given string.
Order of decompositions in the output does not matter.
To separate substrings in the decomposed string, use | as a separator.
Order of characters in a decomposition must remain the same as in the given string. For example, 
for s = "ab", return ["a|b"] and not ["b|a"].
Strings in the output must not contain whitespace. For example, ["a |b"] or ["a| b"] is incorrect.
Constraints:

1 <= length of s <= 20
s only contains lowercase English letters.
'''
def generate_palindromic_decompositions(s):
    """
    Args:
    s(str)
    Returns:
    list_str
    """
    # Write your code here.
    if s is None:
        return None
    
    def check_palindrome(word):
        # print(f"pailindrome: {word}")
        reverse_word = "".join(list(reversed(word)))
        return True if word == reverse_word else False

    
    def get_word_wopipe(path, pipe_index):
        if path[pipe_index] == "|":
            word = path[pipe_index+1:]
        elif pipe_index < 0:
            word = path
        else:
            word = path[pipe_index:]
            
        return word
                
    final_return = []
    def helper(path, index, pipe_index):
        # print(f"path: {path}, index: {index}, pipe_index: {pipe_index}")
        if index == len(s):
            word = get_word_wopipe(path, pipe_index)
            # print(f"word: {word}")
            if check_palindrome("".join(word)):
                final_return.append("".join(path))
            
            return
            
        # left branch
        path.append(s[index])
        helper(path, index+1, pipe_index)
        path.pop()
        # print(f"after left branch: {path}")
        
        # right branch
        word = get_word_wopipe(path, pipe_index)
        # print(f"word: {word}")
        if check_palindrome("".join(word)):
            path.append("|")
            path.append(s[index])
            # print(f"after pipe: {path}")
            helper(path, index+1, len(path)-2)
            path.pop()
            path.pop()
        
        # print(f"after right branch: {path}")
        
        return
    
    helper([s[0]], 1, 0)
    
    return final_return