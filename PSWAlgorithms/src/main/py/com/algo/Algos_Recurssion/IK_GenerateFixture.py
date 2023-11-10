'''
Several teams are participating in a yearly tournament. To make the contest interesting, in each game, the strongest team competes with the weakest team. The n teams are labeled from 1 to n, representing their initial rank. Rank 1 is the strongest, and Rank n is the weakest team.

Given n teams, return their final contest matches in the form of a string.

We use the parentheses ((, )) for pairing and the commas (,) for partition. During the pairing process, in each round, the strategy is needed to make the rather strong one pair with the relatively weak one.

Example One
{
"n": 4
}
Output:

"((1,4),(2,3))"
Explanation: Team 1 will compete with the weakest team 4, and the other two teams will compete with each other. So, we got (1,4),(2,3). After that, the winning team from the 1st match (represented by (1,4)) will compete with the winning team (represented by (2,3)) from the 2nd match.

Example Two
{
"n": 2
}
Output:

"(1,2)"
Explanation: There are only two teams and only one match. So, they will end up competing with each other.

Notes
Constraints:

n == 2x where x is in the range [1, 20].
'''

def generate_fixture(n):
    """
    Args:
    n(int32)
    Returns:
    str
    """
    # Write your code here.
    from collections import deque
    
    traverse_queue = deque()
    
    for i in range(n):
        traverse_queue.append(i+1)
    
    while len(traverse_queue) > 1:
        
        temp = deque()
        for index in range(len(traverse_queue)//2):
            first = traverse_queue.popleft()
            second = traverse_queue.pop()
            # print(first, second)
            pair = "("+str(first)+","+str(second)+")"
            temp.append(pair)
        
        traverse_queue = temp
    
    return traverse_queue[0]


'''
    queue = 1,2,3,4,5,6,7,8

'''