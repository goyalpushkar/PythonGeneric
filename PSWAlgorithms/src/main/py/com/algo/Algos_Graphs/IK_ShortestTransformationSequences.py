'''
If the two words differ by a single letter, it is possible to transform one word into another. Given a start word, a target word, and a list of words, return all possible shortest transformations of the start word to the target word. Each subsequent word of the transformation must exist in the given list of words.

Example One
{
"start_word": "hot",
"target_word": "dog",
"words": ["cat", "dog", "hat", "dot", "cot", "hog"]
}
Output:

[
["hot", "hog", "dog"],
["hot", "dot", "dog"]
]
"hot" -> "hat" -> "cat" -> "cot" -> "dot" -> "dog" or "hot" -> "cot" -> "dot" -> "dog" are also two valid transformation sequences but they are not shortest.

Example Two
{
"start_word": "hot",
"target_word": "dog",
"words": ["cat", "hat", "dot", "cot", "hog"]
}
Output:

[
]

{
"start_word": "abc",
"target_word": "zzz",
"words": ["abz", "zbc", "zbz", "zcz", "zzz"]
}

[
["abc", "abz", "zbz", "zzz"],
["abc", "zbc", "zbz", "zzz"]
]

Notes
Constraints:

The length of all the words, including the start and target words, is the same.
1 <= length of any word <= 5
All the words consist of only lowercase English letters.
1 <= size of the word list <= 2 * 104
All the words from the word list are unique.
The start word and the target word will always be different.
'''
def get_all_shortest_transformation_sequences(start_word, target_word, words):
    """
    Args:
    start_word(str)
    target_word(str)
    words(list_str)
    Returns:
    list_list_str
    """
    # Write your code here.
    import string, math
    
    alphabets = list(string.ascii_lowercase)
    visited = {}
    adj_list = {}
    # parent = {}
    node_traversal = deque()
    
    # if no of words in dictionary are greater than 26 then we will use all combination approach using 26 alphabets 
    # then we need word dictionary for quick lookup else we need to have stop work in the dictionary as we will be 
    # getting all words from dictionary itself
    if len(words) > 26*len(start_word):
        word_dict = set(words)  
    # else:
    #     if target_word not in set(words):
    #         words.append(target_word)
        
    def get_length_diff(word1, word2):
        count = 0
        for idx, word in enumerate(word1):
            if word != word2[idx]:
                count +=1 
            
            if count > 1:
                return False
        
        return True if count == 1 else False
    
    def get_allgeneratedneighbors(curr_node):
        neighbors = []
        for idx, _ in enumerate(curr_node):
            for chr in alphabets:
                new_word = curr_node[:idx] + chr + curr_node[idx+1:]
                
                if new_word in word_dict:
                    neighbors.append(new_word)
                    
        return neighbors
        
    def get_dictwordneighbors(curr_node):
        neighbors = []
        for new_word in words:
            if get_length_diff(curr_node, new_word):
                neighbors.append(new_word)
                    
        return neighbors
    
    def bfs(node):
        node_traversal.append((node, 0))

        visited[node] = True
        found = False
        found_level = math.inf
        
        prev_level = -1
        

        while node_traversal:
            # print(f"node_traversal: {node_traversal}")
            curr_node, curr_level = node_traversal.popleft()
            if prev_level != curr_level:
                level_visited = {}
    
            # print(f"curr_node: {curr_node}, curr_level: {curr_level}, adj_list:{adj_list}\n \t\tvisited:{visited} \t\tlevel_visited: {level_visited} \t\tfound:{found}")
            
            # if target is not found or if target is found but at the same level it should be traversed
            if (not found) or (found and curr_level <= found_level):
                if len(words) > 26*len(start_word):
                    neighbors = get_allgeneratedneighbors(curr_node)
                else:
                    neighbors = get_dictwordneighbors(curr_node)
                
                # print(f"neighbors: {neighbors}")
                for neighbor in neighbors:
                    
                    # add adjacent node only if it ia not visited or visisted in the same level
                    if neighbor not in visited or neighbor in level_visited:
                        adj_list.setdefault(curr_node, []).append(neighbor) 
                        
                    if neighbor == target_word or neighbor not in visited:
                        visited[neighbor] = True
                        level_visited[neighbor] = True
                        node_traversal.append((neighbor, curr_level+1))
                        # print(f"neighbor: {neighbor}, adj_list:{adj_list}")
                    
                    if neighbor == target_word:
                        found_level = curr_level
                        found = True
            
            else:
                if found:
                    break
            
            prev_level = curr_level

    # print(f"words: {words}")
    bfs(start_word)
    # print(f"visited: {visited}, \nadj_list: {adj_list}")
    
    final_paths = []
    def get_paths(node, path):
        if node == target_word:
            final_paths.append(path.copy())
            return
        
        if node in adj_list:
            for neighbor in adj_list[node]:
                path.append(neighbor)
                get_paths(neighbor, path)
                path.pop()

    get_paths(start_word, [start_word])
    return final_paths if final_paths else []

# Using DFS and maintaining parent list has problem if same node is visited in different paths then parent will be overwritten
def get_all_shortest_transformation_sequences(start_word, target_word, words):
    """
    Args:
    start_word(str)
    target_word(str)
    words(list_str)
    Returns:
    list_list_str
    """
    # Write your code here.
    import string, math
    
    alphabets = list(string.ascii_lowercase)
    visited = {}
    
    if len(words) > 26*len(start_word):
        word_dict = set(words)
        
    def get_length_diff(word1, word2):
        count = 0
        for idx, word in enumerate(word1):
            if word != word2[idx]:
                count +=1 
            
            if count > 1:
                return False
        
        return True if count == 1 else False
    
    final_result= {}
    def dfs(node, path):
        # print(f"node: {node}, path: {path}")
        visited[node] = True
        
        if node == target_word:
            no_of_nodes = len(path)
            # print(f"no_of_nodes: {no_of_nodes}")
            if no_of_nodes in final_result:
                final_result[no_of_nodes].append(path.copy())
            else:
                final_result[no_of_nodes] = [path.copy()]
            # final_result.get(no_of_nodes, []).append(path)
            # print(f"final_result: {final_result}")
            visited.popitem()
            return
            
        # get neighbors
        if len(words) > 26*len(start_word):
            for idx, _ in enumerate(node):
                for chr in alphabets:
                    new_word = node[:idx] + chr + node[idx+1:]
                    
                    if new_word not in visited and new_word in word_dict:
                        path.append(new_word)
                        dfs(new_word, path)
                        path.pop()
        
        else:
            for new_word in words:
                if new_word not in visited and get_length_diff(node, new_word):
                    path.append(new_word)
                    dfs(new_word, path)
                    path.pop()
            
        visited.popitem()
        # return
    
    dfs(start_word, [start_word])
    # print(f"final_resul: {final_result}")
    sorted_keys = sorted(final_result.keys())
    return final_result[sorted_keys[0]] if final_result else []