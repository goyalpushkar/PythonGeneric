'''
There are zombies in Seattle. Some of them know each other directly. Others might know each other 
transitively, through others. For example, if zombies A<->B and B<->C know each other directly, 
then A and C know each other indirectly and all three belong to one cluster.

Knowing which zombies know each other directly, find the number of the zombie clusters.

Input is a square matrix where each cell, zombies[A][B], indicates whether zombie A knows zombie B directly.

Example One
{
"zombies": [
"1100",
"1110",
"0110",
"0001"
]
}
Output:

2
There are four zombies: z0, z1, z2 and z3.
Each zombie knows oneself, thus the matrix diagonal has all 1s.
Other than that, the green matrix cells indicate that z0<->z1 and z1<->z2 know each other directly.
Because of the transitive property, zombies z0, z1 and z2 form one cluster.
The remaining zombie, z3, doesn't know others and forms their own separate cluster.
This gives us a total of 2 zombie clusters.

Example Two
Example one

{
"zombies": [
"10000",
"01000",
"00100",
"00010",
"00001"
]
}
Output:

5
Each zombie forms their own cluster: {z0}, {z1}, {z2}, {z3}, and {z4}. The total number of clusters is 5.

Notes
Constraints:

1 <= number of zombies <= 1000
'''
def zombie_cluster(zombies):
    """
    Args:
        zombies(list_str)
    Returns:
        int32
    """
    # Write your code here.
    def dfs(row, visited):
        # print(f"row: {row}, col: {col}, zombies: {zombies}")
        visited[row] = True
        for curr_row, _ in enumerate(zombies):
            if not visited[curr_row] and zombies[row][curr_row]  == "1":
                dfs(curr_row, visited)
                
        return
        
    connected_comp = 0
    visited = [False for i, _ in enumerate(zombies)]
    for curr_row, _ in enumerate(zombies):    # range(len(zombies))
            # print(f"curr_row: {curr_row}, curr_col: {curr_col}, zombies[curr_row][curr_col]: {zombies[curr_row][curr_col]}, connected_comp:{connected_comp}")
        if not visited[curr_row]:
            connected_comp += 1
            dfs(curr_row, visited)
            
    return connected_comp

    # This didn't work for 1 test case
    # directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    # def dfs(row, col):
    #     # print(f"row: {row}, col: {col}, zombies: {zombies}")
    #     zombies[row] = zombies[row][:col]+"2"+zombies[row][col+1:]
    #     for dir in directions:
    #         new_row = row+dir[0]
    #         new_col = col+dir[1]
    #         # print(f"new_row: {new_row}, new_col: {new_col}")
    #         if new_row >= 0 and new_row < len(zombies) and new_col >= 0 and new_col < len(zombies[0]) and  zombies[new_row][new_col] == "1":
    #             dfs(new_row, new_col)
                
    #     return
        
    # connected_comp = 0
    # for curr_row, word in enumerate(zombies):    # range(len(zombies))
    #     for curr_col, _ in enumerate(word):  # range(len(zombies[0]))
    #         # print(f"curr_row: {curr_row}, curr_col: {curr_col}, zombies[curr_row][curr_col]: {zombies[curr_row][curr_col]}, connected_comp:{connected_comp}")
    #         if zombies[curr_row][curr_col] == "1":
    #             connected_comp += 1
    #             dfs(curr_row, curr_col)
                
    # return connected_comp