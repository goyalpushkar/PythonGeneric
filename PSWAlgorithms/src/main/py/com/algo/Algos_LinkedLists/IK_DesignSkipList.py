'''
Skip List is a probabilistic data structure that allows O (log(n)) search complexity
 as well as O (log(n)) insertion complexity within an ordered sequence of n elements.

Implement it using only linked lists.

Skip list has three operations:

insert(value) inserts a value in a skip list, does not return anything.
is_present(value) returns true if given value is present in the skip list and false otherwise.
remove(value) removes a value from a skip list, does not return anything.
Execute the given sequence of operations and return values returned by is_present operations.

Each operation will be given as two numbers:

[0, value] means insert(value),
[1, value] means is_present(value), and
[2, value] means remove(value).
Example
{
"operations": [
[0, 5],
[0, 10],
[0, 1],
[1, 0],
[2, 0],
[1, 1],
[2, 1],
[2, 10],
[0, 10],
[1, 10]
]
}
Output:

[0, 1, 1]
First 3 operations are to insert 5, 10 and 1 in the skip list. So the skip list contains values [1, 5, 10].

4th operation is to search for 0. As 0 is not present in the skip list, the return value will be false.

5th operation is to remove value 0. Now skip list contains [1, 5, 10].

6th operation is to search for 1. As 1 is present in the skip list, the return value will be true.

7th operation is to remove value 1. Now skip list contains [5, 10].

8th operation is to remove value 10. Now skip list contains [5].

9th operation is to insert value 10. Now skip list contains [5, 10].

10th operation is to search for 10. As 10 is present in the skip list, the return value will be true.

Notes
There can be duplicate instructions in the input.
In case of the remove operation, if given value is not present in the skip list, ignore it.
It is a good idea to implement skip list as a class (or object or struct - depending on
the language you use). In function implement_skip_list you would then create an instance of that
 class/object/struct and call its methods/functions to execute the operations.
Structure of the class may look like this:
class SkipList {
    SkipList() {
        // This is a constructor.
        // Initialize required data structures.
    }

    void insert(int value) {
        // ...
    }

    bool is_present(int value) {
        // ...
    }

    void remove(int value) {
        // ...
    }
}
Constraints:

1 <= number of operations <= 100000
-109 <= value in an operation <= 109
'''
def implement_skip_list(operations):
    """
    Args:
    operations(list_list_int32)
    Returns:
    list_bool
    """
    # Write your code here.
    def implement_skip_list(operations):
    """
    Args:
     operations(list_list_int32)
    Returns:
     list_bool
    """
    # Write your code here.
    import random
    class skipListNode:
        def __init__(self, value):
            self.value = value
            self.next = {}

    class skipList:
        def __init__(self, maxLevels):
            self.root = skipListNode(None)
            self.max_level = maxLevels
            
        def get_random_level(self):
            ''' get random level till what node will be copied 
            it will extend node until it gets 1 out of 0 and 1
            '''
            level = 0
            while level < self.max_level-1 and random.randint(0, 1) != 0:
                level += 1
            
            return level
            
        def insert(self, value):
            ''' inserts a new node in the skip list'''
            new_node = skipListNode(value)
            
            # get till what level this node need to be inserted
            # not sure but in this if every node comes till the next level
            # if root is None:
            #     insert_till_level = self.max_level
            # else:
            #     insert_till_level = get_random_level(0, self.max_level)
            
            curr = self.root
            insert_till_level = self.get_random_level()
            level = self.max_level-1
            # print(f"insert_till_level: {insert_till_level}")
            while level >= 0:
                # print(f"level: {level}, curr: {curr.value}-{curr.next}, value: {value}")
                # move to the position less than value to be inserted
                while level in curr.next and curr.next[level].value < value:
                    curr = curr.next[level]
                
                # if value already exists
                if level in curr.next and curr.next[level].value == value:
                    return

                # Check if current level is less than insert level
                if level <= insert_till_level:
                    if level in curr.next:
                        new_node.next[level] = curr.next[level]
                    curr.next[level] = new_node
                
                level -= 1
        
        def is_present(self, value):
            ''' searches a node in the skip list'''
            curr = self.root
            # if curr.value is None:
            #     return False
                
            # start at max level and proceed till lower level
            level = self.max_level-1
            while level >= 0:
                # print(f"level: {level}, curr: {curr.value}-{curr.next}")
                # if next value is same as passed value then return True
                if level in curr.next and curr.next[level].value == value:
                    return True
                # if next value is less than the passed value then move forward
                elif level in curr.next and curr.next[level].value < value:
                    curr = curr.next[level]
                # if next value is greater than the passed value then move to next level
                else:
                    level -= 1
                    
            return False
            
        def remove(self, value):
            ''' removes a node from the skip list'''
            # start from top level and remove till last level
            curr = self.root
            level = self.max_level-1
            while level >= 0:
                # print(f"level: {level}, curr: {curr.value}-{curr.next}")
                # move to the position less than value to be inserted
                while level in curr.next and curr.next[level].value < value:
                    curr = curr.next[level]
                
                # Check if current level is less than insert level
                if level in curr.next and curr.next[level].value == value:
                    # print(f"value found")
                    # temp = curr.next[level]
                    if level in curr.next[level].next:
                        curr.next[level] = curr.next[level].next[level]
                    else:
                        del curr.next[level]
                    # if level == 0:
                    # del temp
                
                level -= 1
    
    ret_arr = []
    def get_max_levels(no_of_queries):
        ''' get maximum number of levels 
        as levels should be log n so divide the number of queries by 2 and increase the level by 1'''
        level = 0
        while no_of_queries > 0:
            level += 1
            no_of_queries //= 2
        
        return level
    
    head = skipList(get_max_levels(len(operations)))
    for operation in operations:
        if operation[0] == 0:
            # print(f"Insert {operation[1]}")
            head.insert(operation[1])
        elif operation[0] == 1:
            # print(f"Search {operation[1]}")
            ret_arr.append(head.is_present(operation[1]))
        if operation[0] == 2:
            # print(f"Remove {operation[1]}")
            head.remove(operation[1])
            
    return ret_arr