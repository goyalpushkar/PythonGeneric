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

Notes
If two or more such sequences exist, return any.
If no such sequence is there to be found, ["-1"] (a sequence of one string, "-1") is the correct answer.
Constraints:

All input strings consist of lowercase English letters.
0 <= total number of characters in all dictionary words combined <= 105
Strings in words are not in any particular order.
There may be duplicates in words.
'''


## Always ue BFS for shortest possible path/ sequence of srings (Dijkstra's)
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
    import string
    from collections import deque

    alphabets = list(string.ascii_lowercase)
    visited = {}
    parent = {}
    node_track = deque()

    # prepare words dictionary to improve word search
    if len(words) > 26*len(start):
        word_dict = set(words)
    else:
        words.append(stop)
    # print(word_dict)

    # get distance i.e. length of diferent characters between words
    # length
    def get_diff(word1, word2):
        count = 0
        for idx, chr in enumerate(word1):
            if chr != word2[idx]:
                count += 1
            
            if count > 1:
                return False
        
        return True if count == 1 else False

    # 26 * length (* length - to check for word existence)
    def neighbors_usingallchr(curr_node):   # , parent, visited
        found = False
        for i, _ in enumerate(curr_node):
            for chr in alphabets:
                if curr_node[i] != chr:
                    new_word = curr_node[:i] + chr + curr_node[i+1:]
                    if new_word == stop:
                        # print(f"stop found new_word:{new_word}")
                        visited[new_word] = True
                        parent[new_word] = curr_node
                        found = True
                        break
                    
                    if new_word not in visited and new_word in word_dict:
                        # print(f"new_word:{new_word}")
                        visited[new_word] = True
                        parent[new_word] = curr_node
                        node_track.append(new_word)

        return found
    
    # no_of_words (* length - for get_diff) 
    def neighbors_usingdict(curr_node):  # , parent, visited
        # print(f"curr_node: {curr_node}")
        found= False
        
        for new_word in words:
            if new_word == stop and get_diff(curr_node, new_word): 
                # print(f"stop found curr_node:{curr_node}")
                visited[new_word] = True
                parent[new_word] = curr_node
                found = True
                break
            
            if new_word not in visited and get_diff(curr_node, new_word):
                # print(f"new_word:{new_word}")
                visited[new_word] = True
                parent[new_word] = curr_node
                node_track.append(new_word)

        return found
    
    # no_of_words
    # Total O (no_of_words * min(no_of_words * length, 26 * length * length)) = O(no_of_words * length * min(no_of_words, 26 * length))
    def bfs(start):
        node_track.append(start)
        visited[start] = True
        parent[start] = -1
        found = False
        while node_track:
            curr_node = node_track.popleft()
            # print(f"curr_node:{curr_node}")
            
            if len(words) > 26*len(start):
                found = neighbors_usingallchr(curr_node)
            else:
                found = neighbors_usingdict(curr_node)
                            
            if found:
                break
    
    def get_result():
        # if stop word found
        if stop in parent and parent[stop] != -1:
            result = []
    
            result.append(stop)
            new_key = parent[stop]
            # for key, val in sorted(parent.iteritems(), key=lambda x: x[0], reverse=True): # type: ignore
            while new_key != start:
                result.append(new_key)
                new_key = parent[new_key]
        
            result.append(start)  
            # result = result[:-1]
            # print(f"result: {result}")
            return list(reversed(result))
        else:
            return ["-1"]
        
    bfs(start)
    print(f"parent: {parent}, visited: {visited}")
    return get_result()


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

# Wrong not working at all
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
    import string
    import math

    alphabets = list(string.ascii_lowercase)
    min_list = []
    min_length = math.inf
    def verify_word(word, current_list):
        nonlocal min_list, min_length

        if word in current_list:
            return 0
        
        if word == stop:
            return 1
        
        result = set()
        local_min = math.inf
        local_path = []
        for i, _ in enumerate(word):
            for chr in alphabets:
                new_word = word[:i] + chr + word[i+1:]
                if new_word in words:
                    result.add(new_word)
                    ret_result = verify_word(new_word, result)
                    if ret_result == 1:
                        if len(result) < local_min:
                            local_min = len(result)
                            local_path = list(result)

        if len(local_path) < min_length:
            min_length = len(local_path)
            min_list = local_path
            
        return 0

    verify_word(start, set())
    return min_list if min_list: else ["-1"]