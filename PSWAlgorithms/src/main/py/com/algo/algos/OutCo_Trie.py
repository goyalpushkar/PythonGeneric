'''
Trie DS

'''

class TrieNode:
    def __init__(self, value):
        self.val = value
        self.isWord = False
        self.descendants = {}   # hash table with letter as key and node as value

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def add_word(self, word):
        current = self.root
        index = 0
        # notFound = True
        while index <= len(word)-1:
            # current letter of word is already present then follow that path
            # else add letter
            current_letter = word[index]
            # Loop can be avoided if letters are stored in key value pair
            # for descendant_node in current.descendants:
            if current_letter in current.descendants:
                # if word[index] == descendant_node.val:
                 current = current.descendants[current_letter]
            else:
                # After checking all descendants if letter not found then add the letter
                # if notFound:
                new_node = TrieNode(word[index])
                current.descendants[current_letter] = new_node
                current = new_node

            index += 1

        new_node.isWord = True
        # return self.root

    def isWord(self, str):
        current = self.root
        index = 0
        while index <= len(str)-1:
            current_letter = str[index]
            if current_letter in current.descendants:
                current = current.descendants[current_letter]
            else:
                return False

            index += 1

        return current.isWord

if __name__ == '__main__':
    root = Trie()
    root.add_word("DOG")
    root.add_word("ELEPHANT")
    root.add_word("BIRD")
    root.add_word("BEE")
    root.add_word("BEA")
    root.add_word("COW")

    print(f"BE: {root.isWord('BE')}")
    print(f"COW: {root.isWord('COW')}")
    print(f"COW: {root.isWord('BEA')}")

