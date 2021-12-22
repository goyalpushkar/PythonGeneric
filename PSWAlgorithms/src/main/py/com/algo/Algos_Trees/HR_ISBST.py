'''

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
                if val <= current.info:
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

def in_order_traversal(root):
    if root.left:
        in_order_traversal(root.left)

    print(root.info, end=" ")

    if root.right:
        in_order_traversal(root.right)


node_values = []
def checkBST(root):
    if root:
        checkBST(root.left)
        node_values.append(root.info)
        checkBST(root.right)

    if sorted(set(node_values)) == node_values:
        return True
    else:
        return False

# Enter your code here
tree = BinarySearchTree()
t = int(input("No of Nodes: "))
arr = list(map(int, input("Tree Nodes: ").split()))
for i in range(t):
    tree.create(arr[i])

in_order_traversal(tree.root)
print()
ans = checkBST(tree.root)
print(ans)
