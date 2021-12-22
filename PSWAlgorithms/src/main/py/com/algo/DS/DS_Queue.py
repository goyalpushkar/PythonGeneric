'''
Created on Jan 28, 2020

@author: goyalpushkar
'''

if __name__ == '__main__':
    pass

class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, value):
        #self.items.insert(0, value)   #O(n)
        self.items.append(value)     #O(1)
    
    def dequeue(self):
        #return self.items.pop()   #O(1)
        return self.items.pop(0) #O(n)
    
    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len( self.items )
    
    def __str__(self):
        return "".join(self.items)
