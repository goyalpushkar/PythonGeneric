'''

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, 6 and 8 have common ancestors of 4 and 14.

         14  13
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

parent_child_pairs_1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

Sample input and output:

has_common_ancestor(parent_child_pairs_1, 3, 8) => false
has_common_ancestor(parent_child_pairs_1, 5, 8) => true
has_common_ancestor(parent_child_pairs_1, 6, 8) => true
has_common_ancestor(parent_child_pairs_1, 6, 9) => true
has_common_ancestor(parent_child_pairs_1, 1, 3) => false
has_common_ancestor(parent_child_pairs_1, 3, 1) => false
has_common_ancestor(parent_child_pairs_1, 7, 11) => true
has_common_ancestor(parent_child_pairs_1, 6, 5) => true
has_common_ancestor(parent_child_pairs_1, 5, 6) => true

Additional example: In this diagram, 4 and 12 have a common ancestor of 11.

        11
       /  \
      10   12
     /  \
1   2    5
 \ /    / \
  3    6   7
   \        \
    4        8

parent_child_pairs_2 = [
    (1, 3), (11, 10), (11, 12), (2, 3), (10, 2),
    (10, 5), (3, 4), (5, 6), (5, 7), (7, 8),
]

has_common_ancestor(parent_child_pairs_2, 4, 12) => true
has_common_ancestor(parent_child_pairs_2, 1, 6) => false
has_common_ancestor(parent_child_pairs_2, 1, 12) => false

n: number of pairs in the input

'''

parent_child_pairs_1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

parent_child_pairs_2 = [
    (1, 3), (11, 10), (11, 12), (2, 3), (10, 2),
    (10, 5), (3, 4), (5, 6), (5, 7), (7, 8)
]

def get_all_ancestors(array_pairs, child, ancestors):  #elem_index
    #ancestors.add(child)
    for elem_index in range(len(array_pairs)):
    #while ( elem_index < len(array_pairs) ):
        #if first child is same as child in the array elements get its parent
        if child == array_pairs[elem_index][1]:
            ancestors.add(array_pairs[elem_index][0])
            get_all_ancestors(array_pairs, array_pairs[elem_index][0], ancestors)


def verify_all_ancestors(array_pairs, child, ancestors):  #elem_index
    #Find all ancestors for second child and verify in the set
    #print("Child - ", child)
    for elem_index in range(len(array_pairs)):
        #if second_child child is same as child in the array elements get its parent
        #print(array_pairs[elem_index][1])
        if child == array_pairs[elem_index][1]:
            #print("Found Child")
            if array_pairs[elem_index][0] in ancestors:
                return "true"
            else:
                #print("continue")
                if verify_all_ancestors(array_pairs, array_pairs[elem_index][0], ancestors) == "true":
                    return "true"

    return "false"

def has_common_ancestor(array_pairs, first_child, second_child):

    first_ancestors = set()
    #Save all ancestors for first child in a set
    '''for elem_index in range(len(array_pairs)):
        #if first child is same as child in the array elements get its parent
        if first_child == array_pairs[elem_index][1]:
            first_ancestors.add(array_pairs[elem_index][0])
    '''
    get_all_ancestors(array_pairs, first_child, first_ancestors)

    #print(first_ancestors)

    #Find all ancestors for second child and verify in the set
    '''
    for elem_index in range(len(array_pairs)):
        #if second_child child is same as child in the array elements get its parent
        if second_child == array_pairs[elem_index][1]:
            if array_pairs[elem_index][0] in first_ancestors:
               return "true"
    '''
    return verify_all_ancestors(array_pairs, second_child, first_ancestors) == "true"
    '''if verify_all_ancestors(array_pairs, second_child, first_ancestors) == "true":
        return "true"
    else:
        return "false"
    '''

    #return "false"


'''
has_common_ancestor(parent_child_pairs_1, 3, 8) => false
has_common_ancestor(parent_child_pairs_1, 5, 8) => true
has_common_ancestor(parent_child_pairs_1, 6, 8) => true
has_common_ancestor(parent_child_pairs_1, 6, 9) => true
has_common_ancestor(parent_child_pairs_1, 1, 3) => false
has_common_ancestor(parent_child_pairs_1, 3, 1) => false
has_common_ancestor(parent_child_pairs_1, 7, 11) => true
has_common_ancestor(parent_child_pairs_1, 6, 5) => true
has_common_ancestor(parent_child_pairs_1, 5, 6) => true
'''
parent_child_pairs_1 = [
(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
(4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)]

print(has_common_ancestor(parent_child_pairs_1, 3, 8))
print(has_common_ancestor(parent_child_pairs_1, 5, 8))
print(has_common_ancestor(parent_child_pairs_1, 6, 8))
print(has_common_ancestor(parent_child_pairs_1, 6, 9))
print(has_common_ancestor(parent_child_pairs_1, 1, 3))
print(has_common_ancestor(parent_child_pairs_1, 3, 1))
print(has_common_ancestor(parent_child_pairs_1, 7, 11))
print(has_common_ancestor(parent_child_pairs_1, 6, 5))
print(has_common_ancestor(parent_child_pairs_1, 5, 6))

print("Test Case 2")
'''
has_common_ancestor(parent_child_pairs_2, 4, 12) => true
has_common_ancestor(parent_child_pairs_2, 1, 6) => false
has_common_ancestor(parent_child_pairs_2, 1, 12) => false
'''

parent_child_pairs_2 = [
    (1, 3), (11, 10), (11, 12), (2, 3), (10, 2),
    (10, 5), (3, 4), (5, 6), (5, 7), (7, 8)
]

print(has_common_ancestor(parent_child_pairs_2, 4, 12))
print(has_common_ancestor(parent_child_pairs_2, 1, 6 ))
print(has_common_ancestor(parent_child_pairs_2, 1, 12))

