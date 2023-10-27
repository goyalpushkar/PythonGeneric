'''
You are given a dictionary called words and two string arguments called start and stop. All given strings 
have equal length.

Transform string start to string stop one character per step using words from the dictionary. For example,
"abc" → "abd" is a valid transformation step because only one character is changed
("c" → "d"), but "abc" → "axy" is not a valid one because two characters are changed ("b" → "x" and "c" → "y").

You need to find the shortest possible sequence of strings (two or more) such that:

First string is start.
Last string is stop.
Every string (except the first one) differs from the previous one by exactly one character.
Every string (except, possibly, first and last ones) are in the dictionary of words.
Example One
{
"words": ["cat", "hat", "bad", "had"],
"start": "bat",
"stop": "had"
}
Output:

["bat", "bad", "had"]
OR

["bat", "hat", "had"]
In "bat", change "t" → "d" to get "bad".
In "bad", change "b" → "h"to get "had".

OR

In "bat", change "b" → "h" to get "hat".
In "hat", change "t" → "d" to get "had".

Example Two
{
"words": [],
"start": bbb,
"stop": bbc
}
Output:

["bbb", "bbc"]
In "bbb", the last character to "b" and get "bbc".

Example Three
{
"words": [],
"start": "zzzzzz",
"stop": "zzzzzz"
}
Output:

["-1"]
No sequence of strings exists that would satisfy all requirements. For example, ["zzzzzz", "zzzzzz"] does
 not satisfy requirement #3. In such situations, ["-1"] is the correct answer.

Notes
If two or more such sequences exist, return any.
If no such sequence is there to be found, ["-1"] (a sequence of one string, "-1") is the correct answer.
Constraints:

All input strings consist of lowercase English letters.
0 <= total number of characters in all dictionary words combined <= 105
Strings in words are not in any particular order.
There may be duplicates in words.
'''

'''
{
"words": ["hot", "dot", "dog", "lot", "log", "cog", "fox"],
"start": "hit",
"stop": "cog"
}  - ["hit", "hot", "dot", "dog", "cog"]

{
"words": ["poon", "plee", "same", "poie", "plie", "poin"],
"start": "toon",
"stop": "plea"
} - ["toon", "poon", "poin", "poie", "plie", "plee", "plea"]
'''
def string_transformation(words, start, stop):
    """
    Args:
    words(list_str)
    start(str)
    stop(str)
    Returns:
    list_str
    """
    # Write your code here.


# below approach is wrong as words from dictionary are not even considered to perform change
# 16/30 passed
def string_transformation(words, start, stop):
    """
    Args:
    words(list_str)
    start(str)
    stop(str)
    Returns:
    list_str
    """
    # Write your code here.
    import math
    
    def dfs(path, exclude):
        nonlocal min_length, final_result
            
        print(f"path: {path} exclude: {exclude}")
        if path[-1] == stop:
            return 0, path
            
        if len(exclude) == len(start):
            return -1, ["-1"] 
            
        local_length = math.inf
        local_path = ["-1"]
        curr_path = ["-1"]
        # curr_word = path[-1]
        for i in range(len(start)):
            curr_word = path[-1]
            
            # print(f"i: {i}")
            # exclude the change of character
            if i in exclude:
                continue
            
            # if letter is same return
            if curr_word[i] == stop[i]:
                continue
            
            # Change character at ith position to same as Stop
            curr_word = curr_word[:i] + stop[i] + curr_word[i+1:]
            print(f"curr_word: {curr_word}")
            
            # if changed word is matching with stop and only second word in the path 
            # no need to check in dictionary and return
            # if len(path) == 1 and curr_word == stop:
            #     path.append(curr_word)
            #     final_result = path
            #     return len(path), final_result
            
            # else check in dictionary the validity of word
            if curr_word == stop or curr_word in words:
                path.append(curr_word)
                exclude.add(i)
                print(f"modified path: {path}, exclude: {exclude}")
                status, curr_path = dfs(path, exclude)
                
                print(f"status: {status}, curr_path: {curr_path}")
                if status == 0 and len(curr_path) < local_length:
                    local_length = len(curr_path)
                    local_path = curr_path
                else:
                    local_length = math.inf
                    local_path = ["-1"]
                    
        
        if local_length < min_length:
            min_length = local_length
            final_result = local_path
                
        return min_length, final_result
        
        
    final_result = []
    min_length = math.inf
    
    if start == stop:
        return ["-1"]

    dfs([start], set())
    
    return final_result