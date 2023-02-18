'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 104 calls will be made to addWord and search.
'''


class WordDictionary:

    # beats 86.32%
    def __init__(self):
        self.root = {}

    def addWord(self, word):
        traverse_node = self.root
        for c in word:
            if c not in traverse_node:
                traverse_node[c] = {}

            traverse_node = traverse_node[c]

        traverse_node['$'] = {word: {}}

    # self done 6915 ms
    def search(self, word):
        print(f"search: {word}\n\n")

        def helper(index, traverse_node):
            print(f"index: {index} traverse_node: {traverse_node}")

            # If index is beyond len of word
            if index > len(word)-1:
                return False

            # if we reached at last character
            print(f"character :{word[index]}")
            # if index == len(word)-1:
            #     if word[index] == ".":
            #         check_len = len(traverse_node) - (1 if '$' in traverse_node else 0)
            #         print(f"check_len: {check_len}")
            #         end_word = False
            #         for key in traverse_node.keys():
            #             if '$' in traverse_node[key]:
            #                 end_word = True
            #
            #         return True if check_len > 0 and end_word else False
            #     else:
            #         return True if '$' in traverse_node.get(word[index], {}) else False

            if word[index] == ".":
                # if it is the last character
                if index == len(word) - 1:
                    for key in traverse_node.keys():
                        if '$' in traverse_node[key]:
                            return True

                    return False

                for key in traverse_node.keys():
                    if helper(index+1, traverse_node[key]):
                        return True
            else:
                if word[index] not in traverse_node:
                    return False
                else:
                    traverse_node = traverse_node[word[index]]
                    # if it is the last character
                    if index == len(word) - 1:
                        return True if '$' in traverse_node else False
                    else:
                        return helper(index + 1, traverse_node)

        traverse_node = self.root
        return helper(0, traverse_node)

    # efficient 2783 ms
    def addWord_eff(self, word: str) -> None:
        temp = self.root
        if len(word) > self.size:
            self.size = len(word)
        for i in word:
            if i not in temp.children:
                temp.children[i] = TrieNode()
            temp = temp.children[i]
        temp.end = True

    def search_eff(self, word):
        if len(word) > self.size:
            return False
        temp = self.root

        def recur(temp, i, word):
            for j in range(i, len(word)):
                if word[j] == '.':
                    for k in temp.children:
                        if recur(temp.children[k], j + 1, word):
                            return True
                    return False

                elif word[j] not in temp.children:
                    return False
                temp = temp.children[word[j]]
            return temp.end

        return recur(temp, 0, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
