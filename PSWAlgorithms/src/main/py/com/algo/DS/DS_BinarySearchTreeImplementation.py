'''
Created on Feb 18, 2020

@author: goyalpushkar
'''

if __name__ == '__main__':
    pass

from DS_BinarySearchTree import *
from DS_Queue import *
from DS_Stack import *

#level-order traversal - breadth first search  BFS
def levelorder(tree):
    nodeQueue = Queue()
    
    nodeQueue.enqueue(tree.root)
    while not nodeQueue.is_empty():
        popedValue = nodeQueue.dequeue()
        if popedValue:
            print( str(popedValue.key) + ' - ' + popedValue.payload )
        
        if popedValue.has_left_child():
            nodeQueue.enqueue( popedValue.left_child )
        if popedValue.has_right_child():
            nodeQueue.enqueue( popedValue.right_child )
        
def zigzagTraversing(tree):
    nodeStack = Stack()
    nodeStack2 = Stack()
    nodeStack.push(tree.root)
    level = 0
    stackUsed = 0
    while not nodeStack.is_empty() or not nodeStack2.is_empty():
        if level % 2 == 0:
            popedValue = nodeStack.pop()
            stackUsed = 0
            if nodeStack.is_empty():
                level = level + 1
        else:    
            popedValue = nodeStack2.pop()
            stackUsed = 1
            if nodeStack2.is_empty():
                level = level + 1
            
        if popedValue:
            print( str(popedValue.key) + ' - ' + popedValue.payload )
        
        if stackUsed == 1:
            if popedValue.has_right_child():
                nodeStack.push(popedValue.right_child)
            if popedValue.has_left_child():
                nodeStack.push(popedValue.left_child)
        else:
            if popedValue.has_left_child():
                nodeStack2.push(popedValue.left_child)
            if popedValue.has_right_child():
                nodeStack2.push(popedValue.right_child)

'''
Depth First Search/Traversals: DFS
(a) Inorder (Left, Root, Right)
(b) Preorder (Root, Left, Right)
(c) Postorder (Left, Right, Root) 
'''
def preorder(rootNode):
    if rootNode.key:
        print(str(rootNode.key) + ' - ' + rootNode.payload )
        if rootNode.has_left_child():
            preorder(rootNode.left_child)
        if rootNode.has_right_child():
            preorder(rootNode.right_child)
        
def postorder(rootNode):
    if rootNode.key:
        if rootNode.has_left_child():
            postorder(rootNode.left_child)
        if rootNode.has_right_child():
            postorder(rootNode.right_child)
        print(str(rootNode.key) + ' - ' + rootNode.payload)
        
def inorder(rootNode):
    if rootNode.key:
        if rootNode.has_left_child():
            inorder(rootNode.left_child)
        print(str(rootNode.key) + ' - ' + rootNode.payload)
        if rootNode.has_right_child():
            inorder(rootNode.right_child)
        
def buildTree(redBlackYN):
    if redBlackYN.upper() == 'Y':
        return RedBlackBST()
    else:
        return BinarySearchTree()
    
def insertValue(tree, key, val):
    tree.put(key, val)
  
def getValue(tree, key):
    tree.get(key)

def deleteValue(tree, key):
    tree.deleteNode(key)
    
def getNodeSize(tree, key):
    print( tree.getSize(key) )
    
def getRank(tree, key):
    print( tree.getRank(key) )

def getFloorNode(tree, key):
    return tree.floorNode(key)
   
def getCeilNode(tree, key):
    return tree.ceilNode(key)
       
def main():
    
    userInput = 'P'
    while userInput != 'Q':
        print("Enter number for below programs")
        print("\t 1. Build Binary Tree")
        print("\t 2. Put Value in Tree")
        print("\t 3. Get Value from Tree")
        print("\t 4. Delete Value from Tree")
        print("\t 5. PreOrder Tree")
        print("\t 6. Post Order Tree")
        print("\t 7. In Order Tree")
        print("\t 8. Level Order Tree")
        print("\t 9. ZigZag Order Tree")
        print("\t 10. In Order Expression")
        print("\t 11. Post Order Evaluation") 
        print("\t 12. Get Tree Size")   
        print("\t 13. Get Tree Rank")    
        print("\t 14. Get Min Node")    
        print("\t 15. Get Max Node")    
        print("\t 16. Get Floor for a node")    
        print("\t 17. Get Ceil for a node")  
        userInput = raw_input("Enter number corresponding to above function or Q to quit: ")
        
        if userInput.upper() == 'Q':
            break
        
        if userInput == '1':
            redBlack = raw_input("Enter Y for Red Black BST or N for normal BST: ")
            tree = buildTree(redBlack)
        elif userInput == '2':
            keyValue = 'P'
            while keyValue.upper() != 'Q':
                keyValue = raw_input("Enter key, value to be inserted into Tree or Q to quit: ")
                if keyValue.upper() == 'Q':
                    break
                
                if keyValue.isdigit():
                    insertValue(tree, int(keyValue.split(",")[0].strip()), keyValue.split(",")[1].strip() )
                else:
                    insertValue(tree, keyValue.split(",")[0].strip(), keyValue.split(",")[1].strip() )
                    
                print( tree.size )
                print( str(tree.root.key) + ' - ' + tree.root.payload )
                
        elif userInput == '3':
            keyValue = raw_input('Get Value for a key: ')
            if keyValue.isdigit():
                print( "Value - " + getValue(tree, int(keyValue) ) )
            else:
                print( "Value - " + getValue(tree, keyValue ) )
                
        elif userInput == '4':
            keyValue = raw_input('Delete key to be deleted: ')
            if keyValue.isdigit():
                deleteValue(int(keyValue)) 
            else:
                deleteValue(keyValue)
                
        elif userInput == '5':
            if tree.root:
                preorder(tree.root)
        elif userInput == '6':
            if tree.root:
                postorder(tree.root)
        elif userInput == '7':
            if tree.root:
                inorder(tree.root)
        elif userInput == '8':
            levelorder(tree)
        elif userInput == '9':
            zigzagTraversing(tree)
        elif userInput == '10':
            print( "Not Implemented Yet")   
        elif userInput == '11':
            print( "Not Implemented Yet")
        elif userInput == '12':
            keyValue = raw_input('Enter node key to get size: ')
            if keyValue.isdigit():
                getNodeSize( tree, int(keyValue) )
            else:
                getNodeSize( tree, keyValue )
                
        elif userInput == '13':
            keyValue = raw_input('Enter node key to get rank: ')
            if keyValue.isdigit():
                getRank( tree, int(keyValue) )  
            else:
                getRank( tree, keyValue ) 
                
        elif userInput == '14':
            minNode = tree.minNode()
            print( str(minNode.key) + ' - ' + minNode.payload )
        elif userInput == '15':
            maxNode = tree.maxNode()
            print( str(maxNode.key) + ' - ' + maxNode.payload )
        elif userInput == '16':
            keyValue = raw_input('Enter node key to get floor Node: ')
            if keyValue.isdigit():
                floorNode = getFloorNode( tree, int(keyValue) )
            else:
                floorNode = getFloorNode( tree, keyValue )
                
            print( str(floorNode.key) + ' - ' + floorNode.payload  )
        elif userInput == '17':
            keyValue = raw_input('Enter node key to get Ceil Node: ')
            if keyValue.isdigit():
                ceilNode = getCeilNode( tree, int(keyValue) )
            else:
                ceilNode = getCeilNode( tree, keyValue )
                
            print( str(ceilNode.key) + ' - ' + ceilNode.payload )           
main() 