'''
Created on Jan 29, 2020

@author: goyalpushkar
'''

class Deque:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.items = []
        
    def add_front(self, value):
        #self.items.append(value)     #O(1)
        self.items.insert(0, value)  #O(n)
        
    def add_rear(self, value):  
        #self.items.insert(0, value)  #O(n)
        self.items.append(value)     #O(1)
        
    def remove_front(self):
        #return self.items.pop()     #O(1)
        return self.items.pop(0)    #O(n)
    
    def remove_rear(self):
        #return self.items.pop(0)    #O(n)
        return self.items.pop()     #O(1)
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return "".join(self.items)