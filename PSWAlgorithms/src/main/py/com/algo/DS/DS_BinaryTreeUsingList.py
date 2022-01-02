'''
Created on Feb 11, 2020

@author: goyalpushkar
'''

if __name__ == '__main__':
    pass

def binary_tree(r):
    return [r, [], []]

def insert_left_child(root, key):
    t = root[1] 
    if len(t) > 1:
        newTree = binary_tree(key) 
        newTree[1] = t
        root[1] = newTree
    else:
        root[1] = binary_tree(key)
    
    return root

'''
def insert_left_child(root, key):
    t = root.pop(1) 
    if len(t) > 1:
        newTree = [key, t, []]
        root.insert(1, newTree)
    else:
        root.insert(1, binary_tree(key) )
    
    return root
'''

def insert_right_child(root, key):
    t = root[2]
    if len(t) > 1:
        newTree = binary_tree(key) 
        newTree[2] = t
        root[2] = newTree
    else:
        root[2] = binary_tree(key)
    
    return root   

'''
def insert_right_child(root, key):
    t = root.pop(2) 
    if len(t) > 1:
        newTree = [key, [], t]
        root.insert(2, newTree)
    else:
        root.insert(2, binary_tree(key) )
    
    return root
'''

def set_root_val(root, value):
    root[0] = value
    
def get_root_val(root):
    return root[0]

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]


def main_testing():
    r = binary_tree(3) 
    print(r)
    insert_left_child(r, 4) 
    print(r)
    insert_left_child(r, 5) 
    print(r)
    insert_right_child(r, 6) 
    print(r)
    insert_right_child(r, 7)
    l = get_left_child(r) 
    print(l)
    print(r)
    set_root_val(l, 9) 
    print(r) 
    insert_left_child(l, 11) 
    print(r)
    print(get_right_child(get_right_child(r)))

def self_check():
    x = binary_tree('a')
    print(x)
    insert_left_child(x,'b')
    print(x)
    insert_right_child(x,'c')
    print(x)
    insert_right_child(get_right_child(x), 'd') 
    print(x)
    insert_left_child(get_right_child(get_right_child(x)), 'e')
    print(x)
    
def build_tree():
    x = binary_tree('a')
    print( x[0] )
    
    insert_left_child(x, 'b')
    print( x[1] )
    
    insert_right_child(x, 'c')
    print( x[2] )
    
    print(x)
    insert_right_child(get_left_child(x), 'd')
    print( x[1] )

    insert_left_child(get_right_child(x), 'e')
    insert_right_child(get_right_child(x), 'f')
    print( x[2] )
    
    print(x)
    
def main():
    print("Enter choice to run the program")
    print( "\t 1. Main Testing")
    print( "\t 2. Self Check")
    print( "\t 3. Build Tree")
    value = 'P'
    while value.upper() != 'Q':
        value = raw_input("Enter choice: " )
        
        if value.upper() == 'Q':
            break
        
        if value == "1":
            main_testing()
        elif value == "2":
            self_check()
        elif value == "3":
            build_tree()

#main()
