'''
Created on Jan 29, 2020

@author: goyalpushkar
'''

class Node():
    '''
    classdocs
    '''

    def __init__(self, init_data):
        '''
        Constructor
        '''
        self.data = init_data
        self.next = None        
    
    def set_data(self, data):
        self.data = data    
        
    def get_data(self):
        return self.data
    
    def set_next(self, new_node):
        self.next = new_node
        
    def get_next(self):
        return self.next
    
class UnOrderedList():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.head = None
        self.last = None
        
    def is_empty(self):
        return self.head == None
    
    def add(self, data):
        newNode = Node(data)
        newNode.set_next(self.head)
        if self.head == None:
            self.last = newNode
            
        self.head = newNode
        
    def size(self):
        count = 0 
        startTraverse = self.head
        while startTraverse != None:
            startTraverse = startTraverse.get_next()
            count = count + 1
        
        return count
     
    def search(self, itemData):
        startTraverse = self.head
        found = False
        while startTraverse != None and not found:
            if ( startTraverse.get_data() == itemData ):
                found = True
            else:
                startTraverse = startTraverse.get_next()
            
        return found
    
    def remove(self, data):
        previousNode = None
        startTraverse = self.head  
        removed = False  
        while startTraverse != None and not removed:
            if ( startTraverse.get_data() == data ):
                if previousNode == None: #If head Node is removed
                    self.head = startTraverse.get_next()
                    self.last = startTraverse.get_next()
                elif startTraverse.get_next() == None: #if last node is removed
                    self.last = previousNode
                    previousNode.set_next( startTraverse.get_next() )
                else: 
                    previousNode.set_next( startTraverse.get_next() )
                
                removed = True
                
            previousNode = startTraverse
            startTraverse = startTraverse.get_next()
            
    def append( self, itemData):
        newNode = Node(itemData)
        newNode.set_next(None)
        
        startTraverse = self.head
        
        #BigO(N)
        '''
        if startTraverse == None: #If List is empty
            self.head = newNode
        else:
            while startTraverse.get_next() != None:
                startTraverse = startTraverse.get_next( )
        
            startTraverse.set_next(newNode)
        '''
            
        #BigO(1)
        if startTraverse == None: #If List is empty
            self.head = newNode
            self.last = newNode
        else:
            self.last.set_next(newNode)
            self.last = newNode
            
            
class OrderedList():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.head = None
        self.last = None
        
    def is_empty(self):
        return self.head == None
    
    def add(self, itemData):
        newNode = Node(itemData)
        
        previousNode = None
        startTraverse = self.head
        if startTraverse ==  None:  #If List is empty
            self.head = newNode
            self.last = newNode
        else:    
            while startTraverse != None:
                if startTraverse.data > itemData:
                    if previousNode == None:  #If New Node has to be added on Head
                        self.last = startTraverse 
                        newNode.set_next(startTraverse)
                        self.head = newNode
                    elif startTraverse.get_next() == None:  # If New Node has to be added as last Node 
                        startTraverse.set_next(newNode)
                        self.last = newNode
                    else:
                        previousNode.set_next( newNode ) 
                        newNode.set_next(startTraverse)
                    
                    break
                
                previousNode = startTraverse
                startTraverse = startTraverse.get_next()
        
    def size(self):
        count = 0 
        startTraverse = self.head
        while startTraverse != None:
            startTraverse = startTraverse.get_next()
            count = count + 1
        
        return count
    
    def search(self, item):
        startTraverse = self.head
        found = False
        while startTraverse != None and not found:
            if startTraverse.get_data() == item:
                found = True
            else:
                if startTraverse.get_data() > item:
                    break
                else:
                    startTraverse = startTraverse.get_next()
        
        return found
    
    def remove(self, data):
        previousNode = None
        startTraverse = self.head  
        removed = False  
        while startTraverse != None and not removed:
            if ( startTraverse.get_data() == data ):
                if previousNode == None: #If head Node is removed
                    self.head = startTraverse.get_next()
                    self.last = startTraverse.get_next()
                elif startTraverse.get_next() == None: #if last node is removed
                    self.last = previousNode
                    previousNode.set_next( startTraverse.get_next() )
                else: 
                    previousNode.set_next( startTraverse.get_next() )
                
                removed = True
                
            previousNode = startTraverse
            startTraverse = startTraverse.get_next()
           
    def append( self, itemData):
        newNode = Node(itemData)
        newNode.set_next(None)
        
        startTraverse = self.head
        
        #BigO(N)
        '''
        if startTraverse == None: #If List is empty
            self.head = newNode
        else:
            while startTraverse.get_next() != None:
                startTraverse = startTraverse.get_next( )
        
            startTraverse.set_next(newNode)
        '''
            
        #BigO(1)
        if startTraverse == None: #If List is empty
            self.head = newNode
            self.last = newNode
        else:
            self.last.set_next(newNode)
            self.last = newNode
            