'''
There are n courses to take, they are referred to by numbers from 0 to n - 1. Some of them have prerequisites, 
e.g., courses A and B must be completed before course C can be taken (in other words, course C depends on A and B).

Find and return an ordering in which all the given courses can be taken while satisfying all the prerequisites. 
If there exists more than one such ordering, any one of them would be a correct answer. If no such ordering exists,
 return a special value: [-1].

Example
{
"n": 4,
"prerequisites": [
[1, 0],
[2, 0],
[3, 1],
[3, 2]
]
}
Output:

[0, 2, 1, 3]
According to the input,

course 0 must be done before both 1 and 2,
courses 1 and 2 must be done before course 3.
There are two orderings in which one can take all four courses: [0, 2, 1, 3] and [0, 1, 2, 3]. Either is a 
correct answers.

Notes
Prerequisites are given as a list of pairs: a list of lists where each inner list has exactly two elements. 
Each pair [X, Y] represents one prerequisite: course Y has to be completed before X can be taken (X depends on Y, 
in other words).
Function must return a list of integers. If all given courses can be taken while satisfying all given prerequisites,
 the returned array must contain any of the possible orderings. Otherwise, the function must return [-1].
Constraints:

1 <= n <= 10000
0 <= number of prerequisites <= 10000
'''
def course_schedule(n, prerequisites):
    """
    Args:
     n(int32)
     prerequisites(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    adj_list = [[] for i in range(n)]
    for course in prerequisites:
        adj_list[course[1]].append(course[0])
        
    def dfs(node, time_stamp):
        arrival[node] = time_stamp
        visited[node] = 1
        time_stamp += 1
        
        for neigh in adj_list[node]:
            if visited[neigh] == -1:
                if dfs(neigh, time_stamp):
                    return True
            else:
                # Back edge detected
                if departure[neigh] is None and arrival[neigh] < arrival[node]:
                    return True
        
        departure[node] = time_stamp
        time_stamp += 1
        final_result.append(node)
        
    arrival = [0 for i in range(n) ]  
    departure = [None for i in range(n) ]  
    visited = [-1 for i in range(n) ]  
    final_result = []
    
    for i in range(n):
        if visited[i] == -1:
            # if cycle is detected
            if dfs(i, 0):
                return [-1]
    
    final_result = list(reversed(final_result))
    return final_result
