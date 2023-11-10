'''
Design and implement an iterator for the in-order traversal of a binary tree.

Given the root node of a tree of positive numbers, and a sequence of operations on the iterator, calculate
return values of all those operations.

Iterator has two operations:

has_next() should return 1 if one or more elements remain in the in-order traversal of the tree, otherwise
it should return 0.
next() should return the next value in the in-order traversal of the tree if it exists, otherwise a special value of 0.
Execute operations one by one and return all their return values in a list.

Both operations must take constant time on average and use O(height of the tree) of extra memory.

Example
Example

"operations": ["next", "has_next", "next", "next", "has_next", "has_next", "next"]
Output:

[100, 1, 200, 300, 0, 0, 0]
In-order traversal for the given tree is [100, 200, 300].

1st operation next() returns the first element, 100.

2nd operation has_next() returns 1 because traversal isn't over and there are more elements.

3rd operation, next() returns the second element, 200.

4th operation, next() returns the last element, 300.

5th operation has_next() returns 0; the in-order traversal is over.

6th operation has_next() returns 0; it's still over.

7th operation next() return 0, since there is no next element.

Notes
It is a good idea to implement the iterator as a class (or object or struct - depending on the language you use).
 In function implement_tree_iterator you would then create an instance of that class/object/struct and call 
 its methods/functions to execute the operations.
Structure of the class may look like this:
class TreeIterator {
    TreeIterator() {
        // This is a constructor.
        // Initialize required data structures.
    }

    int next() {
        // ...
    }

    int has_next() {
        // Or you can return bool here and convert it
        // to int in function implement_tree_iterator.
    }
}
Constraints:

1 <= number of nodes in the tree <= 100000
1 <= node value <= 109
0 <= number of operations <= 300000
'''
"""
For your reference:
"""
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# IK approach
# write a method to push all left children to stack
# has next will check if stack is not empty then return 1 else 0
# next will check if has next then pop from stack and return + push all left children to stack for right node
def implement_tree_iterator(root, operations):
    """
    Args:
    root(BinaryTreeNode_int32)
    operations(list_str)
    Returns:
    list_int32
    """
    # Write your code here.
    class treeIterator:
        def __init__(self, root):
            self.iterator = root
            self.yet_to_return = []
            self.returned = set()
        
        def verify_next(self):
            # print(f"self.iterator: {self.iterator}, {self.yet_to_return}, {self.returned}")
            if not self.iterator:
                return None
                
            while self.iterator.left and self.iterator.left not in self.returned:
                self.yet_to_return.append(self.iterator)
                self.iterator = self.iterator.left
                
            if self.iterator in self.returned:
                if self.iterator.right:
                    self.iterator = self.iterator.right
                    while self.iterator.left and self.iterator.left not in self.returned:
                        self.yet_to_return.append(self.iterator)
                        self.iterator = self.iterator.left
                elif  len(self.yet_to_return) > 0:
                    self.iterator = self.yet_to_return.pop()
                else:
                    self.iterator = None

            # print(f"self.iterator 1: {self.iterator.value}")
            # print(f"self.iterator 2: {self.iterator.value}")
            
            self.returned.add(self.iterator)
            return self.iterator
            
        def next(self):
            val = self.verify_next()
            # print(f"val:  {val}")
            if val is not None:
                return val.value
            else:
                return 0
            
        def has_next(self):
            # val = self.verify_next()
            # # print(f"val:  {val}")
            # if val is not None:
            if ( len(self.yet_to_return) > 0 or (self.iterator is not None and self.iterator.right is not None) or (self.iterator is not None and self.iterator not in self.returned)):
                return True
            else:
                return False
        
    
    iterator = treeIterator(root)
    final_result = []
    for oper in operations:
        # print(f"oper:  {oper}")
        if oper == "next":
            # print(f"iterator: {iterator.iterator.value}")
            val = iterator.next()
            final_result.append(val)
        elif oper == "has_next":
            # print(f"iterator: {iterator.iterator.value}")
            if iterator.has_next():
                final_result.append(1)
            else:
                final_result.append(0)
            
    return final_result