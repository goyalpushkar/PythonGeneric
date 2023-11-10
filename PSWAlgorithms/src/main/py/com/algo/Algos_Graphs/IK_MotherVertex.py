'''
'''
def get_mother_vertex(n, edges):
    """
    Args:
    n(int32)
    edges(list_list_int32)
    Returns:
    int32
    """
    # Write your code here.
    # Start from any node, do tree traversal and collect the visited nodes in a set
    # after visiting all nodes check the len of set if it is equal to n that means all are visited and return starting node
    # if no then start with some other node
    # if none return success then return -1
    graph = {}
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = [edge[1]]
        else:
            graph[edge[0]].append(edge[1])

    def dfs(curr):
        nonlocal visited

        visited.add(curr)
        if curr in graph:
            for edge in graph[curr]:
                if edge not in visited:
                    dfs(edge)
    
    for i in range(n):
        visited = set()
        dfs(i)
        # print(visited)
        if len(visited) == n:
            return i
        
    return -1


def get_mother_vertex(n, edges):
    """
    Args:
    n(int32)
    edges(list_list_int32)
    Returns:
    int32
    """
    # Write your code here.
    arr = [-1 for i in range(n)]
    def dfs(curr, parent):
        arr[curr] = parent
        for edge in edges:
            if edge[0] == curr and arr[edge[1]] == -1:
                dfs(edge[1], curr)

    for i in range(n):
        if arr[i] == -1:
            dfs(i, i)
        
    print(f"arr: {arr}")
    # not_changed = False
    i = 0
    while i < n:
        while arr[i] != arr[arr[i]]:
            arr[i] = arr[arr[i]]
            i = arr[arr[i]]
        
        i += 1
    
    print(f"arr: {arr}")
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            return -1
    
    return arr[0]