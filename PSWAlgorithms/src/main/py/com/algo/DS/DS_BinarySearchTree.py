'''
Created on Feb 16, 2020

@author: goyalpushkar
'''
from idlelib.TreeWidget import TreeNode
from Foundation._nsindexset import __getitem__
from platform import node

class TreeNode:
    '''
    classdocs
    '''


    def __init__(self, key, val, left = None, right = None, parent = None, color = 'RED'):
        '''
        Constructor
        '''
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.count = 1
        self.color = color
        
    def has_left_child(self):
        return self.left_child
    
    def has_right_child(self):
        return self.right_child
    
    def is_left_child(self):
        return self.parent and self.parent.left_child == self
    
    def is_right_child(self):
        return self.parent and self.parent.right_child == self
    
    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return not ( self.left_child or self.right_child )
    
    def is_red(self):
        return self.color == 'RED'
        
    def has_any_children(self):
        return self.left_child or self.right_child
    
    def has_both_children(self):
        return self.left_child and self.right_child
    
    def getSize(self):
        if self:
            return self.count
        else:
            return 0
        
    def __iter__(self):
        if self:
            if self.has_left_child():
                for node in self.left_child:
                    yield node
            
            yield self.key
            
            if self.has_right_child():
                for node in self.right_child:
                    yield node
                    
    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self
            
    def findMin(self):
        if self.has_left_child():
            return self.left_child().findMin()
        else:
            return self
        
    def findSuccessor(self): 
        succ = None
        if self.has_right_child():   # If node has right node then Find minimum on the right tree
            succ = self.right_child().findMin()
        else:                        # If node does not have right node then 
            if self.parent:
                if self.is_left_child():    # either node is on the left side of the tree
                    succ = self.parent
                else:                       # or node is on the right side of the tree
                    self.parent.right_child = None
                    succ = self.parent.findSuccessor()
                    self.parent.right_child = self
        
        return succ
    
    def spliceOut(self):    #Set links for Successor Node
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else :
                self.parent.right_child = None
        else:
            if self.has_right_child():
                if self.is_left_child():
                    self.parent.left_child = self.right_child()
                else:
                    self.parent.right_child = self.right_child()
            
                self.right_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.left_child()
                else:
                    self.parent.right_child = self.left_child()            
             
                self.left_child.parent = self.parent
                
    #Below operations are required for Red black BST
    def rotateLeft(self):
        if self.has_right_child():
            newNode = self.right_child
            self.right_child = newNode.left_child
            
            newNode.parent = self.parent
            newNode.left_child = self
            newNode.color = self.color
            self.color = 'RED'
            
            return newNode
            
    def rotateRight(self):
        if self.has_left_child():
            newNode = self.left_child
            self.left_child = newNode.right_child
            
            newNode.parent = self.parent
            newNode.right_child = self
            newNode.color = self.color
            self.color = 'RED'
            
            return newNode
        
    def flipColors(self):
        if self.color == 'BLACK':
            self.color = 'RED'
            self.right_child.color = 'BLACK'
            self.left_child.color = 'BLACK'
            
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            
        self.size = self.size + 1
        
    def _put(self, key, val, currentNode):
        if key >= currentNode.key:
            if currentNode.has_right_child():
                self._put( key, val, currentNode.right_child)
            else:
                currentNode.right_child = TreeNode(key, val, None, None, currentNode)
        else: #if key < currentNode.key:
            if currentNode.has_left_child():
                self._put( key, val, currentNode.left_child )
            else:
                currentNode.left_child = TreeNode(key, val, None, None, currentNode)
                
        if currentNode.left_child and currentNode.right_child:
            currentNode.count = 1 + currentNode.left_child.getSize() + currentNode.right_child.getSize()
        elif currentNode.left_child:
            currentNode.count = 1 + currentNode.left_child.getSize()
        elif currentNode.right_child:
            currentNode.count = 1 + currentNode.right_child.getSize()
        else:
            currentNode.count = 1
       
        #print( currentNode.count )     
                            #( if currentNode.left_child: currentNode.left_child.getSize() ) + 
                            #( if currentNode.right_child: currentNode.right_child.getSize() )
        '''
        if not currentNode:
            return TreeNode(key, val, None, None, currentNode)
        elif key >= currentNode.key:
            currentNode.right_child = self._put( key, val, currentNode.right_child)
        else:
            currentNode.left_child = self._put( key, val, currentNode.left_child ) 
        
        if key >= currentNode.key:
            if currentNode.has_right_child():
                self._put( key, val, currentNode.right_child)
            else:
                currentNode.right_child = TreeNode(key, val, None, None, currentNode)
        else: #if key < currentNode.key:
            if currentNode.has_left_child():
                self._put( key, val, currentNode.left_child )
            else:
                currentNode.left_child = TreeNode(key, val, None, None, currentNode)
        '''
            
    def __setitem__(self, k, v):
        self.put(k, v)
        
    def get(self, key):
        if self.root:
            findNode = self._get( key, self.root )
            if findNode:
                return findNode.payload
            else:
                return None
        else:
            return None
    
    def _get(self, key, currentNode):
        #print(currentNode.key)
        if not currentNode:
            return None
        elif key == currentNode.key:
            return currentNode
        elif key > currentNode.key:
            return self._get( key, currentNode.right_child )
        else:
            return self._get( key, currentNode.left_child )
            
    def __getitem__(self, key):
        return self.get(key)
   
    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False
          
    def getSize(self, key):
        #print(key)
        if self.root:
            return self._size(key, self.root)
        else:
            return 0
        
    def _size(self, key, currentNode):
        if not currentNode:
            return 0
        elif key == currentNode.key:
            #print(currentNode.key)
            return currentNode.getSize()
        elif key > currentNode.key:
            #print(currentNode.key)
            return self._size( key, currentNode.right_child)
        elif key < currentNode.key:
            #print(currentNode.key)
            return self._size( key, currentNode.left_child)
        
    def getRank(self, key):
        if self.root:
            return self._rank(key, self.root)
        else:
            return None
        
    def _rank(self, key, currentNode):
        if not currentNode:
            return None
        elif key == currentNode.key:
            return self.getSize( currentNode.left_child)
        elif key > currentNode.key:
            return 1 + self.getSize(currentNode.left_child) + self._rank( key, currentNode.right_child)
        elif key < currentNode.key:
            self._rank( key, currentNode.left_child)
        
    def minNode(self):
        currentNode = self.root
        while currentNode.has_left_child():
            currentNode = currentNode.left_child
            
        return currentNode
    
    def maxNode(self):
        currentNode = self.root
        while currentNode.has_right_child():
            currentNode = currentNode.right_child
            
        return currentNode
    
    def floorNode(self, key):
        if self.root:
            return self._floorNode(key, self.root, None)
        else:
            return None
        
    def _floorNode(self, key, currentNode, floorKey):
        if not currentNode:
            return floorKey
        if key == currentNode.key:
            return currentNode
        elif key > currentNode.key:
            return self._floorNode( key, currentNode.right_child, currentNode )
        elif key < currentNode.key:
            return self._floorNode( key, currentNode.left_child, floorKey )
            
        return floorKey
    
    def ceilNode(self, key):
        if self.root:
            return self._ceilNode(key, self.root, None)
        else:
            return None
        
    def _ceilNode(self, key, currentNode, ceilKey):
        if not currentNode:
            return ceilKey
        if key == currentNode.key:
            return currentNode
        elif key > currentNode.key:
            return self._ceilNode( key, currentNode.right_child, ceilKey )
        elif key < currentNode.key:
            return self._ceilNode( key, currentNode.left_child, currentNode )
            
        return ceilKey
        
    def __delitem__(self, key):
        self.deleteNode(key)
    
    def deleteNode(self, key):
        nodeToBeDeleted = self._get(key, self.root)
        
        if not nodeToBeDeleted:   
            raise("Error, Key not in Tree")
        
        if self.size == 1 and self.root.key == key:   #If root Node
            self.root = None
        else:   
            if nodeToBeDeleted.is_leaf():          #else if deleted node is leaf Node 
                if nodeToBeDeleted.is_right_child():
                    nodeToBeDeleted.parent.right_child = None
                elif nodeToBeDeleted.is_left_child():
                    nodeToBeDeleted.parent.left_child = None
            
            ##Just Try if below elif and else can be replaced with just one else
            elif nodeToBeDeleted.has_both_children():
                nodeToBeReplaced = self.findSuccessor(nodeToBeDeleted)
                nodeToBeReplaced.spliceOut()
                nodeToBeDeleted.key = nodeToBeReplaced.key
                nodeToBeDeleted.payload = nodeToBeReplaced.paylod
            else:
                #Set Parent for Child Nodes
                if nodeToBeDeleted.has_left_child():
                    if nodeToBeDeleted.is_left_child():
                        nodeToBeDeleted.left_child.parent = nodeToBeDeleted.parent
                        nodeToBeDeleted.parent.left_child = nodeToBeDeleted.left_child
                    elif nodeToBeDeleted.is_right_child():
                        nodeToBeDeleted.left_child.parent = nodeToBeDeleted.parent
                        nodeToBeDeleted.parent.right_child = nodeToBeDeleted.left_child
                    else:
                        nodeToBeDeleted.replace_node_data( nodeToBeDeleted.left_child.key
                                                          ,nodeToBeDeleted.left_child.payload
                                                          ,nodeToBeDeleted.left_child.left_child
                                                          ,nodeToBeDeleted.left_child.right_child )
                else:
                    if nodeToBeDeleted.is_left_child():
                        nodeToBeDeleted.right_child.parent = nodeToBeDeleted.parent
                        nodeToBeDeleted.parent.left_child = nodeToBeDeleted.left_child
                    elif nodeToBeDeleted.is_right_child():
                        nodeToBeDeleted.right_child.parent = nodeToBeDeleted.parent
                        nodeToBeDeleted.parent.right_child = nodeToBeDeleted.left_child
                    else:
                        nodeToBeDeleted.replace_node_data( nodeToBeDeleted.right_child.key
                                                          ,nodeToBeDeleted.right_child.payload
                                                          ,nodeToBeDeleted.right_child.left_child
                                                          ,nodeToBeDeleted.right_child.right_child )
                
                    
            '''
            #Replace the Nodes
            if nodeToBeReplaced:  # If deleted node is not leaf node
                #Set Parent Connection
                if nodeToBeDeleted.is_right_child():
                    nodeToBeDeleted.parent.right_child = nodeToBeReplaced
                    nodeToBeReplaced.parent = nodeToBeDeleted.parent 
                elif nodeToBeDeleted.is_left_child():
                    nodeToBeDeleted.parent.left_child = nodeToBeReplaced
                    nodeToBeReplaced.parent = nodeToBeDeleted.parent 
                    
                #Set Child Connection
                nodeToBeReplaced.left_child = nodeToBeDeleted.left_child
                nodeToBeReplaced.right_child = nodeToBeDeleted.right_child
                
                
            else:   #else if deleted node is leaf Node 
                if nodeToBeDeleted.is_right_child():
                    nodeToBeDeleted.parent.right_child = None
                elif nodeToBeDeleted.is_left_child():
                    nodeToBeDeleted.parent.left_child = None
            '''
                
        nodeToBeDeleted.parent = None
        self.size = self.size - 1
        
#Binary Search tree can be non symmetric if
#Trees not random (!) ⇒ sqrt (N) per op
# Resolution is 2-3 Tree/Red black Tree
class RedBlackBST():
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            
        self.size = self.size + 1
        
    def _put(self, key, val, currentNode):
        if key >= currentNode.key:
            if currentNode.has_right_child():
                self._put( key, val, currentNode.right_child)
            else:
                currentNode.right_child = TreeNode(key, val, None, None, currentNode)
        else: #if key < currentNode.key:
            if currentNode.has_left_child():
                self._put( key, val, currentNode.left_child )
            else:
                currentNode.left_child = TreeNode(key, val, None, None, currentNode)
                
        #if currentNode.has_left_child() and currentNode.has_right_child():
        if ( not currentNode.left_child and currentNode.right_child.color == 'RED' ) or ( currentNode.left_child.color == 'BLACK' and currentNode.right_child.color == 'RED' ):
            currentNode = currentNode.rotateLeft()
        
        if currentNode.has_left_child():
            if currentNode.left_child.has_left_child():
                if currentNode.left_child.color == 'RED' and currentNode.left_child.left_child.color == 'RED':
                    currentNode = currentNode.rotateRight()
    
        if currentNode.has_left_child() and currentNode.has_right_child():
            if currentNode.left_child.color == 'RED' and currentNode.right_child.color == 'RED':
                currentNode.flipColors()
        
        if currentNode.left_child and currentNode.right_child:
            currentNode.count = 1 + currentNode.left_child.getSize() + currentNode.right_child.getSize()
        elif currentNode.left_child:
            currentNode.count = 1 + currentNode.left_child.getSize()
        elif currentNode.right_child:
            currentNode.count = 1 + currentNode.right_child.getSize()
        else:
            currentNode.count = 1
       
        #print( currentNode.count )     
                            #( if currentNode.left_child: currentNode.left_child.getSize() ) + 
                            #( if currentNode.right_child: currentNode.right_child.getSize() )
        '''
        if not currentNode:
            return TreeNode(key, val, None, None, currentNode)
        elif key >= currentNode.key:
            currentNode.right_child = self._put( key, val, currentNode.right_child)
        else:
            currentNode.left_child = self._put( key, val, currentNode.left_child ) 
        
        if key >= currentNode.key:
            if currentNode.has_right_child():
                self._put( key, val, currentNode.right_child)
            else:
                currentNode.right_child = TreeNode(key, val, None, None, currentNode)
        else: #if key < currentNode.key:
            if currentNode.has_left_child():
                self._put( key, val, currentNode.left_child )
            else:
                currentNode.left_child = TreeNode(key, val, None, None, currentNode)
        '''
            
    def __setitem__(self, k, v):
        self.put(k, v)
        
    def get(self, key):
        if self.root:
            findNode = self._get( key, self.root )
            if findNode:
                return findNode.payload
            else:
                return None
        else:
            return None
    
    def _get(self, key, currentNode):
        #print(currentNode.key)
        if not currentNode:
            return None
        elif key == currentNode.key:
            return currentNode
        elif key > currentNode.key:
            return self._get( key, currentNode.right_child )
        else:
            return self._get( key, currentNode.left_child )
            
    def __getitem__(self, key):
        return self.get(key)
   
    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False
          
    def getSize(self, key):
        #print(key)
        if self.root:
            return self._size(key, self.root)
        else:
            return 0
        
    def _size(self, key, currentNode):
        if not currentNode:
            return 0
        elif key == currentNode.key:
            #print(currentNode.key)
            return currentNode.getSize()
        elif key > currentNode.key:
            #print(currentNode.key)
            return self._size( key, currentNode.right_child)
        elif key < currentNode.key:
            #print(currentNode.key)
            return self._size( key, currentNode.left_child)
        
    def getRank(self, key):
        if self.root:
            return self._rank(key, self.root)
        else:
            return None
        
    def _rank(self, key, currentNode):
        if not currentNode:
            return None
        elif key == currentNode.key:
            return self.getSize( currentNode.left_child)
        elif key > currentNode.key:
            return 1 + self.getSize(currentNode.left_child) + self._rank( key, currentNode.right_child)
        elif key < currentNode.key:
            self._rank( key, currentNode.left_child)
        
    def minNode(self):
        currentNode = self.root
        while currentNode.has_left_child():
            currentNode = currentNode.left_child
            
        return currentNode
    
    def maxNode(self):
        currentNode = self.root
        while currentNode.has_right_child():
            currentNode = currentNode.right_child
            
        return currentNode
    
    def floorNode(self, key):
        if self.root:
            return self._floorNode(key, self.root, None)
        else:
            return None
        
    def _floorNode(self, key, currentNode, floorKey):
        if not currentNode:
            return floorKey
        if key == currentNode.key:
            return currentNode
        elif key > currentNode.key:
            return self._floorNode( key, currentNode.right_child, currentNode )
        elif key < currentNode.key:
            return self._floorNode( key, currentNode.left_child, floorKey )
            
        return floorKey
    
    def ceilNode(self, key):
        if self.root:
            return self._ceilNode(key, self.root, None)
        else:
            return None
        
    def _ceilNode(self, key, currentNode, ceilKey):
        if not currentNode:
            return ceilKey
        if key == currentNode.key:
            return currentNode
        elif key > currentNode.key:
            return self._ceilNode( key, currentNode.right_child, ceilKey )
        elif key < currentNode.key:
            return self._ceilNode( key, currentNode.left_child, currentNode )
            
        return ceilKey
    