'''
Huffman coding assigns variable length codewords to fixed length input characters based on their frequencies. More frequent characters are assigned shorter codewords and less frequent characters are assigned longer codewords. All edges along the path to a character contain a code digit. If they are on the left side of the tree, they will be a 0 (zero). If on the right, they'll be a 1 (one). Only the leaves will contain a letter and its frequency count. All other nodes will contain a null instead of a character, and the count of the frequency of all of it and its descendant characters.

For instance, consider the string ABRACADABRA. There are a total of  characters in the string. This number should match the count in the ultimately determined root of the tree. Our frequencies are  and . The two smallest frequencies are for  and , both equal to , so we'll create a tree with them. The root node will contain the sum of the counts of its descendants, in this case . The left node will be the first character encountered, , and the right will contain . Next we have  items with a character count of : the tree we just created, the character  and the character . The tree came first, so it will go on the left of our new root node.  will go on the right. Repeat until the tree is complete, then fill in the 's and 's for the edges. The finished graph looks like:

image

Input characters are only present in the leaves. Internal nodes have a character value of ϕ (NULL). We can determine that our values for characters are:

A - 0
B - 111
C - 1100
D - 1101
R - 10
Our Huffman encoded string is:

A B    R  A C     A D     A B    R  A
0 111 10 0 1100 0 1101 0 111 10 0
or
01111001100011010111100
To avoid ambiguity, Huffman encoding is a prefix free encoding technique. No codeword appears as a prefix of any other codeword.

To decode the encoded string, follow the zeros and ones to a leaf and return the character there.

You are given pointer to the root of the Huffman tree and a binary coded string to decode. You need to print the decoded string.

Function Description

Complete the function decode_huff in the editor below. It must return the decoded string.

decode_huff has the following parameters:

root: a reference to the root node of the Huffman tree
s: a Huffman encoded string
Input Format

There is one line of input containing the plain string, . Background code creates the Huffman tree then passes the head node and the encoded string to the function.

Constraints


Output Format

Output the decoded string on a single line.

Sample Input

image

s="1001011"
Sample Output

ABACA
Explanation

S="1001011"
Processing the string from left to right.
S[0]='1' : we move to the right child of the root. We encounter a leaf node with value 'A'. We add 'A' to the decoded string.
We move back to the root.

S[1]='0' : we move to the left child.
S[2]='0' : we move to the left child. We encounter a leaf node with value 'B'. We add 'B' to the decoded string.
We move back to the root.

S[3] = '1' : we move to the right child of the root. We encounter a leaf node with value 'A'. We add 'A' to the decoded string.
We move back to the root.

S[4]='0' : we move to the left child.
S[5]='1' : we move to the right child. We encounter a leaf node with value C'. We add 'C' to the decoded string.
We move back to the root.

 S[6] = '1' : we move to the right child of the root. We encounter a leaf node with value 'A'. We add 'A' to the decoded string.
We move back to the root.

Decoded String = "ABACA"
'''

import queue as Queue

cntr = 0


class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count


def huffman_hidden():  # builds the tree and returns root
    q = Queue.PriorityQueue()

    for key in freq:
        q.put((freq[key], key, Node(freq[key], key)))

    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))

    root = q.get()
    root = root[2]  # contains root object
    return root


def dfs_hidden(obj, already):
    if (obj == None):
        return
    elif (obj.data != '\0'):
        code_hidden[obj.data] = already

    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")


"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    #print(root.data, " ", s)
    decodeHuff.index = 0
    decodeHuff.final_string = ""
    decodeHuff.root = root
    '''
    while decodeHuff.index < len(s):
        #(value, new_index) = get_data(index, root, s)
        value = str(get_data(root, s))
        print(value)
        #print("Returned Value: " + value[0], value[1])
        decodeHuff.final_string += value  #value[0]
        #index = new_index  #value[1] #+=
    '''
    get_data(root, s)
    print("Before Return: ", decodeHuff.final_string)
    print(decodeHuff.final_string)

def get_data(node, s):
    print("Get Data: ", decodeHuff.index, node.data, s)
    if node.left is None and node.right is None:
        print("in if: ", node.data, " ", decodeHuff.index)
        decodeHuff.final_string += str(node.data)
        print("Final String: ", decodeHuff.final_string)
        node = decodeHuff.root
        if decodeHuff.index >= len(s):
            return decodeHuff.final_string
            #return node.data
    #else:
    chr = s[decodeHuff.index]
    decodeHuff.index += 1

    #print(chr)
    if chr == '0':
        get_data(node.left, s)
    else:
        get_data(node.right, s)

    return decodeHuff.final_string

'''        
def get_data(index, node, s):
    print(index, node.data, s)
    if node.left is None and node.right is None:
        print("in if: ", node.data, " ", index)
        return (node.data, index)
    else:
        chr = s[index]
        index += 1

    print(chr)
    if chr == '0':
        get_data(index, node.left, s)
    else:
        get_data(index, node.right, s)
'''
# Enter Your Code Here

ip = input("Enter String: ")
freq = {}  # maps each character to its frequency

cntr = 0

for ch in ip:
    if (freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch] += 1

root = huffman_hidden()  # contains root of huffman tree
code_hidden = {}  # contains code for each object
dfs_hidden(root, "")

if len(code_hidden) == 1:  # if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
    toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)
