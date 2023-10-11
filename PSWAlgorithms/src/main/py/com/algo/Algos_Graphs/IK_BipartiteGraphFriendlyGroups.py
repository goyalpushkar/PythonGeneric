'''
There are n people living in a town. Some of them dislike each other. Given the value of n and two equal length
 integer arrays called dislike1 and dislike2. For each i in [0, dislike1_size - 1], the person dislike1[i] 
 dislikes the person dislike2[i]. Check if we can divide the people of the town into two sets such that 
 each person belongs to exactly one set and no two persons disliking each other belong to the same set.

Example One
{
"num_of_people": 5,
"dislike1": [0, 1, 1, 2, 3],
"dislike2": [2, 2, 4, 3, 4]
}
Output:
1
The people can be partitioned into two sets [0, 1, 3] and [2, 4].

Example Two
{
"num_of_people": 4,
"dislike1": [0, 0, 0, 1, 2],
"dislike2": [1, 2, 3, 2, 3]
}
Output:
0
Notes
People are numbered from 0 to n - 1.

Constraints:
1 <= n <= 2*103
0 <= number of disliking pairs <= min((n * (n - 1))/2, 104)
'''

# One approach is to do BFS and put nodes and its neighbors in alternate sets. Verify if node is visited then does it
# exists in alternate set
# Second approach is to check if there are cycles (using cross edges for BFS). If there is a cycle with odd number of
# nodes then it will not be bipartite but if cycle is with even number of nodes then it will be bipartite
# because if there are 5 nodes and 5 edges connect them all then it will not be bipartite but if there are 6 nodes
# and 6 edges then they will be bipartite
'''
            R                           R
        G       G                  G        G

        R       R                  R        R

                                        G
    Not bipartite as 2 Red      Bipartite as no 2 nodes have same color
'''
# e.g.
'''
                s 
        n1      n2      n3
        |        |      |


           w1   w2  w3 .... w6
    u1  u2  u3  u4........u5   - k level
    If cross edge is between u1 and u2 len of paths from s 
    s - u1 (k) - u2 (1) - s (k) = 2k + 1 - cannot be bipartited
    If cross edge is between u1 and w1 len of paths from s 
    s - u1 (k) - w1 (1) - s (k-1) = 2k - can be bipartited

'''

from collections import deque

# Approach where alternate layer nodes are put in different sets
def can_be_divided(num_of_people, dislike1, dislike2):
    """
    Args:
     num_of_people(int32)
     dislike1(list_int32)
     dislike2(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    adj_list = [[] for i in range(num_of_people)]
    for i in range(len(dislike1)):
        adj_list[dislike1[i]].append(dislike2[i])
        adj_list[dislike2[i]].append(dislike1[i])

    print(adj_list)

    def dfs(node, color):
        set_node[node] = color

        for nei in adj_list[node]:
            # check if neighbor is already visited and in the same set then return true
            # else call bfs on neighbor with alternate set_num
            if set_node[nei] == 0:
                if dfs(nei, -1 * set_node[node]):
                    return True
            else:
                if set_node[node] == set_node[nei]:
                    return True

        return False

    def bfs(node):
        set_node[node] = -1
        que.append(node)

        while que:
            curr_node = que.popleft()
            print(curr_node, set_node, que)
            for nei in adj_list[curr_node]:
                # check if neighbor is already visited and in the same set then return true
                # else call bfs on neighbor with alternate set_num
                if set_node[nei] == 0:
                    set_node[nei] = -1 * set_node[curr_node]
                    que.append(nei)
                else:
                    if set_node[curr_node] == set_node[nei]:
                        return True

        return False

    que = deque()
    set_node = [0 for _ in range(num_of_people)]
    for index in range(num_of_people):
        if set_node[index] == 0:
            # BFS
            if bfs(index):
                return False
            # DFS
            # if dfs(index, -1):
            #     return False

    return True



def can_be_divided(num_of_people, dislike1, dislike2):
    """
    Args:
     num_of_people(int32)
     dislike1(list_int32)
     dislike2(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    adj_list = [[] for i in range(num_of_people)]
    for i in range(len(dislike1)):
        adj_list[dislike1[i]].append(dislike2[i])
        adj_list[dislike2[i]].append(dislike1[i])

    print(adj_list)

    # def dfs(node, color):
    #     visited[node] = color
    #     distance[node] = 1
    #     for nei in adj_list[node]:
    #         # check if neighbor is already visited and in the same set then return true
    #         # else call bfs on neighbor with alternate set_num
    #         if visited[nei] == -1:
    #             distance[nei] = distance[node] + 1
    #             if dfs(nei, -1 * set_node[node]):
    #                 return True
    #         else:
    #             if parent[node] != nei:
    #                 if distance[nei] == distance[node]:
    #                     return True
    #
    #     return False

    def bfs(node):
        visited[node] = -1
        distance[node] = 1
        que.append(node)

        while que:
            curr_node = que.popleft()
            # print(curr_node, set_node, que)
            for nei in adj_list[curr_node]:
                # check if neighbor is already visited and in the same set then return true
                # else call bfs on neighbor with alternate set_num
                if visited[nei] == -1:
                    visited[nei] = 1
                    distance[nei] = distance[curr_node] + 1
                    parent[nei] = curr_node
                    que.append(nei)
                else:
                    if parent[curr_node] != nei:
                        if distance[nei] == distance[curr_node]:
                            return True

        return False

    que = deque()
    visited = [-1 for _ in range(num_of_people)]
    parent = [-1 for _ in range(num_of_people)]
    distance = [-1 for _ in range(num_of_people)]
    for index in range(num_of_people):
        if set_node[index] == 0:
            if visited[i] == -1:
                # BFS
                if bfs(index):
                    return False
                # DFS
                # if dfs(index, -1):
                #     return False

    return True

'''
edge_list = []
        duplicate_check = set()
        for index in range(len(graph)):
            for edges in graph[index]:
                key = "".join(str(elem) for elem in sorted([index, edges]))
                if key not in duplicate_check:
                    edge_list.append(sorted([index, edges]))
                    duplicate_check.add(key)

        # print(edge_list)
'''