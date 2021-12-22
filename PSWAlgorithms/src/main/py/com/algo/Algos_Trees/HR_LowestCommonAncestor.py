'''
You are given pointer to the root of the binary search tree and two values  and . You need to return the lowest common ancestor (LCA) of  and  in the binary search tree.

image
In the diagram above, the lowest common ancestor of the nodes  and  is the node . Node  is the lowest node which has nodes  and  as descendants.

Function Description

Complete the function lca in the editor below. It should return a pointer to the lowest common ancestor node of the two values given.

lca has the following parameters:
- root: a pointer to the root node of a binary search tree
- v1: a node.data value
- v2: a node.data value

Input Format

The first line contains an integer, , the number of nodes in the tree.
The second line contains  space-separated integers representing  values.
The third line contains two space-separated integers,  and .

To use the test data, you will have to create the binary search tree yourself. Here on the platform, the tree will be created for you.

Constraints




The tree will contain nodes with data equal to  and .

Output Format

Return the a pointer to the node that is the lowest common ancestor of  and .

Sample Input

6
4 2 3 1 7 6
1 7
image
 and .

Sample Output

[reference to node 4]

Explanation

LCA of  and  is , the root in this case.
Return a pointer to the node.
'''


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''
def in_order_traversal(root):
    if root.left:
        in_order_traversal(root.left)

    print(root.info, end=" ")

    if root.right:
        in_order_traversal(root.right)

def lca(root, v1, v2):
    print(root.info)
    if v1 <= root.info and v2 >= root.info\
            or v1 >= root.info and v2 <= root.info:
        return root
    elif v1 < root.info and v2 < root.info:
        return lca(root.left, v1, v2)
    elif v1 > root.info and v2 > root.info:
        return lca(root.right, v1, v2)

# Enter your code here
tree = BinarySearchTree()
t = int(input("No of Nodes: "))
arr = list(map(int, input("Tree Nodes: ").split()))
for i in range(t):
    tree.create(arr[i])

in_order_traversal(tree.root)
print()
v = list(map(int, input("Nodes for which LCA is required: ").split()))
ans = lca(tree.root, v[0], v[1])
print(ans.info)
