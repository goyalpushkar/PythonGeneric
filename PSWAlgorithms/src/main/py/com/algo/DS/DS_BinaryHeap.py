'''
Created on Feb 12, 2020

@author: goyalpushkar
'''

class BinaryHeap:
    '''
    classdocs
    '''
    
    def __init__(self, maxSize=20):
        '''
        Constructor
        '''
        self.heap_list = [0]
        self.current_size = 0
        self.max_size = maxSize   #Heap with limited heap size
        
    def perc_up(self, i):
        
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
            
            i = i // 2 
        
    def insert(self, element):
        self.heap_list.append(element)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)
        
        if self.current_size > self.max_size:
            self.heap_list.pop()
            self.current_size = self.current_size - 1
        
    def find_min(self):
        return self.heap_list[1]
    
    def find_max_size(self):
        return self.max_size
    
    def perc_down(self, index):
        while index*2 <= self.current_size:
            minChild = self.min_child(index)
            if self.heap_list[index] > self.heap_list[minChild]:
                self.heap_list[index], self.heap_list[minChild] = self.heap_list[minChild], self.heap_list[index]
        
            index = minChild
            
    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2 + 1]:
                return i*2
            else:
                return i*2 + 1
        
    def del_min(self):
        retValue = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return retValue 
    
    def is_empty(self):
        return self.current_size == 0
    
    def size(self):
        return self.current_size
         
    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1
        
    def build_sorted_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1
        
        ##Below code is to keep heap size within limits
        self.sort_heap_list()
        
        while self.current_size > self.max_size:
            self.heap_list.pop()
            self.current_size = self.current_size - 1
                    
    def sort_heap_list(self):
        while self.current_size > 1: 
            self.heap_list[1], self.heap_list[self.current_size] = self.heap_list[self.current_size], self.heap_list[1]
            self.current_size = self.current_size - 1
            self.perc_down(1)
            #listLength = listLength - 1
    
        self.current_size = len(self.heap_list) - 1 # 1 to consider default value of 0
      
    def print_heap(self):
        for elem in self.heap_list:
            print( elem )  # end=', '
        #for index in range(1, self.current_size):
        #    print( self.heap_list[index])