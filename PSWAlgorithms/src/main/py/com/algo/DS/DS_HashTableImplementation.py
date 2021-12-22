'''
Created on Feb 8, 2020

@author: goyalpushkar
'''

from DS_HashTable import HashTable

if __name__ == '__main__':
    pass

def main():
    h = HashTable()
    h[54] = "cat"
    h[26] = "dog"
    h[93] = "lion" 
    h[17] = "tiger"
    h[77] = "bird"
    h[31] = "cow"
    h[44] = "goat"
    h[55] = "pig"
    h[20] = "chicken"
    
    print(h.slots)
    print(h.data)
    
    print(h[20])
    h[20] = 'duck'
    
    print(h.data)


main()
    