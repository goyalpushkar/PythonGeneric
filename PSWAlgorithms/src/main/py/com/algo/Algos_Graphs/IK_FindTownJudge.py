'''
Find the judge among a group of people in a town.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
Example One
{
"n": 4,
"trust": [
[1, 4],
[2, 4],
[3, 4]
]
}
Output:

4
Person-1 trusts person-4.
Person-2 trusts person-4.
Person-3 trusts person-4.
Everyone trusts the person-4 and the person-4 trusts no one.

Example Two
{
"n": 3,
"trust": [
[1, 2],
[2, 3],
[3, 1],
[3, 2]
]
}
Output:

-1
Notes
There are n persons in the town, and each person is represented by a unique number from 1 to n.
Trust among the people is represented in a two-dimensional list where each inner list consists of two values
 [u, v]. This represents that the person numbered u trusts the person numbered v.
If the town judge doesn't exist, return -1.
Constraints:

1 <= n <= 10^4
0 <= size of the input list <= 10^5
1 <= value of each element of the input list <= n
The input list won't contain duplicate pairs.
The values in individual pairs won't be equal.
'''
def find_town_judge(n, trust):
    """
    Args:
     n(int32)
     trust(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    
    adj_list = [[] for i in range(n)]
    in_degree = [0 for i in range(n)]
    
    for rel in trust:
        adj_list[rel[0]-1].append(rel[1]-1)
        in_degree[rel[1]-1] += 1
    
    town_judge = -1
    for index in range(n):
        # town judge trusts nobody and everybody trusts town judge
        if len(adj_list[index]) == 0 and in_degree[index] == n-1:
            town_judge = index + 1
            
    return town_judge
