'''
Created on Jan 27, 2020

@author: goyalpushkar
'''
#from Carbon.Aliases import false

if __name__ == '__main__':
    pass

class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
        '''
        if self.items.__len__() > 0:
            return False
        else:
            return True
        '''
    
    def push(self, value):
        self.items.append(value)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        if self.items == []:
            return None
        else:
            return self.items[ len(self.items) - 1 ]
        
    def size(self):
        return self.items.__len__()
    
    def __str__(self):
        returnStr = ""
        for item in self.items:
            returnStr = returnStr + str(item)
          
        return returnStr  
'''    
s = Stack()
print( s.is_empty() )
s.push(4)
s.push("Tiger")
print( s.size() )
print( s.peek() )
print( s.is_empty() )
print( s.pop() )
print( s.size() )
'''