'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
'''


class Trie:

    # Trie Node -> {key(node letter) -> value as descendent node}
    def __init__(self):
        self.root = {}  # "": []   dict of dict

    def insert(self, word: str) -> None:
        traverse_node = self.root
        for i in range(len(word)):
            if word[i] in traverse_node:
                if i == len(word) - 1:
                    traverse_node[word[i]] = (traverse_node[word[i]][0], True)
                else:
                    traverse_node = traverse_node[word[i]][0]
            else:
                # new_node = {c: []}
                if i == len(word)-1:
                    traverse_node[word[i]] = ({}, True)
                else:
                    traverse_node[word[i]] = ({}, False)
                # traverse_node[""] = traverse_node.get("", []).append(new_node)
                traverse_node = traverse_node[word[i]][0]  # new_node

    def search(self, word: str) -> bool:
        traverse_node = self.root
        for i in range(len(word)):
            if word[i] in traverse_node:
                if i == len(word) - 1:
                    return traverse_node[word[i]][1]
                else:
                    traverse_node = traverse_node[word[i]][0]
            else:
                return False

    def startsWith(self, prefix: str) -> bool:
        traverse_node = self.root
        for c in prefix:
            if c in traverse_node:
                traverse_node = traverse_node[c][0]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)