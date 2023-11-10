'''
Given a set of words, find all word squares which can be built using them.

A sequence of words forms a valid word square if the kth row and kth column read the exact
same string, where 0 ≤ k < max(number of rows, number of columns).

For example, the word sequence ["area", "card", "cart", "dart", "rear", "tart"] forms a word 
square because each word reads the same both horizontally and vertically.

c a r d
a r e a
r e a r
d a r t
Example
{
"words": ["area", "card", "cart", "dart", "rear", "tart"]
}
Output:

[
["card", "area", "rear", "dart"],
["cart", "area", "rear", "tart"],
["dart", "area", "rear", "tart"],
["tart", "area", "rear", "tart"]
]
Notes
Constraints:

1 <= Length of the set of words <= 1000
1 <= Length of any element in the set of words <= 5
Every element of the set will have the same length.
Each element of the set contains only lowercase English alphabet a - z.
There are no duplicate elements in the set of words.
'''
def find_word_squares(words):
    """
    Args:
    words(list_str)
    Returns:
    list_list_str
    """
    # Write your code here.
    # Trie class
    class Trie:
        def __init__(self):
            self.root = {'': {}}
            
        def insert(self, value):
            curr = self.root['']
            for chr in value:
                if chr in curr:
                    curr = curr[chr]
                    continue
                
                curr[chr] = {}
                curr = curr[chr]
            
            curr['$'] = value
            # return self.root
            
        def search(self, value):
            curr = self.root['']
            # print(f"curr: {curr}")
            for chr in value:
                if chr in curr:
                    curr = curr[chr]
                    continue
                else:
                    return []
            
            words = []
            def rec(curr):
                if '$' in curr:
                    words.append(curr['$'])
                    return words
                        
                for letter in curr:
                    rec(curr[letter])
            
            # print(f"curr: {curr}")
            rec(curr)
            return words
        
        def print_root(self):
            print(self.root)
            
            
    def square(curr_words, level):
        nonlocal final_list
        # print(f"level: {level}, curr_words: {curr_words}")
        
        if level == total_len:
            final_list.append(curr_words.copy())
            return
            
        curr_string = ""
        for word in curr_words:
            curr_string += word[level]
        
        # print(f"curr_string: {curr_string}")
        pref_words = root.search(curr_string)
        # print(f"pref_words {pref_words}")
        for word in pref_words:
            curr_words.append(word)
            square(curr_words, level+1)
            curr_words.pop()
            
        return 
        
    total_len = len(words[0])
    root = Trie()
    final_list = []
    
    # Prepare Trie of words
    for word in words:
        root.insert(word)
        # print(word, root)
    
    # root.print_root()
    # start with each word to prepare square matrix
    for word in words:
        # print(f"start with word: {word}")
        square([word], 1)
        

    return final_list