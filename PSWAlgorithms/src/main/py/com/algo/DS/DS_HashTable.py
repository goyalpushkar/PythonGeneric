'''
Created on Feb 8, 2020

@author: goyalpushkar
'''
from test.test_iterlen import NoneLengthHint

class HashTable(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def hash_function(self, key, size):
        return key % size 
    
    #Linear Probing
    def rehash(self, old_hash, size):
        return (old_hash + 1) % size
    
    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots) )
        
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                rehash_value = self.rehash(hash_value, len(self.slots) )
                while self.slots[rehash_value] != None and self.slots[rehash_value] != key:
                    rehash_value = self.rehash(rehash_value, len(self.slots) )
                
                if self.slots[rehash_value] == None:
                    self.slots[rehash_value] = key
                    self.data[rehash_value] = data
                else:    
                    self.data[rehash_value] = data
                    
    def get(self, key):
        start_value = self.hash_function(key, len(self.slots) )
        
        data= None
        stop = False
        found = False
        position = start_value
        while self.slots[position] != None and not stop and not found:
            if self.slots[position] == key: 
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots) )
                if position == start_value:
                    stop = True
                    
        return data
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)