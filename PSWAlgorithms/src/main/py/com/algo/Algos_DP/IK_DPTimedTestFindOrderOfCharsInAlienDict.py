'''
Given a sorted dictionary of an alien language, find the order of characters in the alphabet.

Example One
{
"words": ["baa", "abcd", "abca", "cab", "cad"]
}
Output:

"bdac"
Example Two
{
"words": ["caa", "aaa", "aab"]
}
Output:

"cab"
Notes
Given dictionary is sorted in the lexicographical order of the alien language.
Output is a string consisting of all the characters of the alien alphabet, in order.
Constraints:

1 <= total length of all the words in the dictionary <= 105
Input will consist of lowercase latin characters only
Input will be such that it is possible to determine the alphabet order uniquely
The dictionary may contain duplicate words
'''
def find_order(words):
    """
    Args:
    words(list_str)
    Returns:
    str
    """
    # Write your code here.
    from collections import deque

    # Mine - 
    # Build a Trie or all the words - O (len Dict)
    # Perform BFS on the Trie to take children from each level with same root
    # perform dfs to get topolofical order of dependencies
    # these steps will not work so replaced them with topological traversing above
    # Go through all commulated nodes one by one and rank each alphabet in increasing order in dictionary
    # prepare an array using dictionary values - 0-25 
    # result will be generated from aray elements in the order


    # IK - 
    # Compare 2 words at a time. Compare their characters one by one. If any mismatch found then there is a dependency between those characters
    # perform dfs to get topolofical order of dependencies 

    
    class TrieNode:
        def __init__(self, value):
            self.val = value
            self.isEnd = False
            self.children = {}    # search by value in dictionary will be O(1) as compared to in array

    class Trie:
        ''' class for Trie build'''
        def __init__(self):
            self.root = {"": {}}
            #TrieNode(value) Using this children will be array and search will not be efficient by value

        # def searchNode(self, parent, value):
            
        #     # if there is no child
        #     if not parent.children:
        #         return parent
            
        #     for child in parent.children:
        #         if value == child.value:
        #             return child
        #         else:
        #             return parent

        # def insert_node(self, value):
        #     curr = self.root
        #     new_node = TrieNode(value)
        #     if new_node in curr.children:

        def insert_word(self, word):
            ''' method to insert a wrod in Trie'''
            curr = self.root[""]
            for alph in word:
                # if alphabet does not exist then add it to the curr level
                if alph not in curr:
                    curr[alph] = {}

                # traverse 
                curr = curr[alph]
            
            curr['$'] = word
        
        def search_word(self, word):
            ''' method to search a wrod in Trie'''
            curr = self.root[""]

            def dfs(curr_level, i):

                # if it reaches to the end of word
                if i >= len(word):
                    return True
                
                # if word char is not found in the curret level
                if word[i] not in curr_level:
                    return False

                if not dfs(curr_level[word[i]], i+1):
                    return False
                
                return True
            
            return dfs(curr, 0)

    # Build a Trie for the words
    base_trie = Trie()
    for word in words:
        base_trie.insert_word(word) # type: ignore

    # def print_trie():
        
    # Perform BFS on the Trie to take children from each level with same root
    child_level = []
    child_dependency = {}
    def bfs(root):
        traverse_deck = deque()
        traverse_deck.append(root[""])

        while traverse_deck:
            curr_level = traverse_deck.popleft()
            print(f"curr_level: {curr_level}")
            if "$" in curr_level.keys():
                continue

            if len(curr_level) > 1:
                insert_nodes = True
            else:
                insert_nodes = False

            inserted_link = ""
            prev = ""
            for child in curr_level.keys():
                traverse_deck.append(curr_level[child])
                if insert_nodes:
                    inserted_link += child
                    if prev != "":
                        if prev not in child_dependency:
                            child_dependency[prev] = set(child)
                        else:
                            child_dependency[prev].add(child)
                            # child_dependency.get(pre).add(child)

                prev = child
            
            if insert_nodes:
                child_level.append(inserted_link)
    bfs(base_trie.root)
    print(f"child_level: {child_level} \nchild_dependency: {child_dependency}")

    # perform dfs to get topolofical order of dependencies
    topological_order = []
    def dfs(node):
        
        visited[node] = -1
        if node in child_dependency:
            for child in child_dependency[node]:
                if child not in visited:
                    if not dfs(child):
                        return False
                else:
                    # it is already visited and status is still -1 i.e. cycle
                    if visited[child] == -1:
                        return False
        
        visited[node] = 1
        topological_order.append(node)

        return True
    
    visited = {}
    for child in child_dependency:
        if child not in visited:
            if not dfs(child):
                return ""

    return list(reversed(topological_order))

    # # Go through all commulated nodes one by one and rank each alphabet in increasing order in dictionary
    # # this is wrong it will not work 
    # # e.g.  - [bac, znb, bd, da] in this c's rank will never change after initial setting
    # alpha_dict = {}
    # for word in child_level:
    #     start = 0
    #     for alph in word:
    #         if start >= alpha_dict.get(alph, 0):
    #             alpha_dict[alph] = start
            
    #         start = alpha_dict[alph]
    #         start += 1
    
    # # prepare an array using dictionary values - 0-25 
    # # result will be generated from aray elements in the order

    return ''

words = ["baa", "abcd", "abca", "cab", "cad"]
result = find_order(words)
print(f"result: {result}")