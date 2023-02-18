'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to
 take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

2, [[1,0]]
2, [[1,0],[0,1]]
4, [[2,0],[1,0],[3,1],[3,2],[1,3]]
5, [[1,4],[2,4],[3,1],[3,2]]
4, [[1,0],[2,1],[3,2],[1,3]]
100, [[6,27],[83,9],[10,95],[48,67],[5,71],[18,72],[7,10],[92,4],[68,84],[6,41],[82,41],[18,54],[0,2],[1,2],[8,65],[47,85],[39,51],[13,78],[77,50],[70,56],[5,61],[26,56],[18,19],[35,49],[79,53],[40,22],[8,19],[60,56],[48,50],[20,70],[35,12],[99,85],[12,75],[2,36],[36,22],[21,15],[98,1],[34,94],[25,41],[65,17],[1,56],[43,96],[74,57],[19,62],[62,78],[50,86],[46,22],[10,13],[47,18],[20,66],[83,66],[51,47],[23,66],[87,42],[25,81],[60,81],[25,93],[35,89],[65,92],[87,39],[12,43],[75,73],[28,96],[47,55],[18,11],[29,58],[78,61],[62,75],[60,77],[13,46],[97,92],[4,64],[91,47],[58,66],[72,74],[28,17],[29,98],[53,66],[37,5],[38,12],[44,98],[24,31],[68,23],[86,52],[79,49],[32,25],[90,18],[16,57],[60,74],[81,73],[26,10],[54,26],[57,58],[46,47],[66,54],[52,25],[62,91],[6,72],[81,72],[50,35],[59,87],[21,3],[4,92],[70,12],[48,4],[9,23],[52,55],[43,59],[49,26],[25,90],[52,0],[55,8],[7,23],[97,41],[0,40],[69,47],[73,68],[10,6],[47,9],[64,24],[95,93],[79,66],[77,21],[80,69],[85,5],[24,48],[74,31],[80,76],[81,27],[71,94],[47,82],[3,24],[66,61],[52,13],[18,38],[1,35],[32,78],[7,58],[26,58],[64,47],[60,6],[62,5],[5,22],[60,54],[49,40],[11,56],[19,85],[65,58],[88,44],[86,58]]


Main logic is to prepare adjacency matrix based on prerequisites and check for circle existence for each node in the
adjacency matrix
'''
class Solution:

    # Worked Beats 63.86% after removing print statements and checked_nodes ( 46/52 - OutputLimit Exceeded)
    def canFinish(self, numCourses, prerequisites):
        adjacency_matrix = {}
        visited_nodes = set()
        checked_nodes = set()
        for elem in prerequisites:
            if elem[0] in adjacency_matrix:
                if elem[1] not in adjacency_matrix[elem[0]]:
                    adjacency_matrix[elem[0]].append(elem[1])
            else:
                adjacency_matrix[elem[0]] = [elem[1]]

            # if elem[1] in adjacency_matrix:
            #     if elem[0] not in adjacency_matrix[elem[1]]:
            #         adjacency_matrix[elem[1]].append(elem[0])
            # else:
            #     adjacency_matrix[elem[1]] = [elem[0]]

        print(f"adjacency_matrix: {adjacency_matrix}")

        def is_circle(node):
            # print(f"node: {node}  visited_nodes:{visited_nodes}")
            if node in visited_nodes:
                return True

            if node not in adjacency_matrix:
                return False

            visited_nodes.add(node)
            for child in adjacency_matrix[node]:
                if is_circle(child):
                    return True

            visited_nodes.remove(node)
            checked_nodes.add(node)
            adjacency_matrix[node] = []
            return False

        for key in adjacency_matrix.keys():
            # visited_nodes = []
            if key in checked_nodes:
                continue
            # if adjacency_matrix[key]:
            if is_circle(key):
                return False

            # print(f"key: {key}\n\n")

        return True

    def canFinish_otherway(self, numCourses, prerequisites):
        adjacency_matrix = {}
        visited_nodes = set()
        for elem in prerequisites:
            if elem[0] in adjacency_matrix:
                if elem[1] not in adjacency_matrix[elem[0]]:
                    adjacency_matrix[elem[0]].append(elem[1])
            else:
                adjacency_matrix[elem[0]] = [elem[1]]

            # if elem[1] in adjacency_matrix:
            #     if elem[0] not in adjacency_matrix[elem[1]]:
            #         adjacency_matrix[elem[1]].append(elem[0])
            # else:
            #     adjacency_matrix[elem[1]] = [elem[0]]

        print(f"adjacency_matrix: {adjacency_matrix}")

        def dfs(node):
            # node already visited means circle, not possible to finish
            if node in visited_nodes:
                return False

            # no children means no dependency, possible to finish
            if node not in adjacency_matrix:
                return True

            visited_nodes.add(node)
            for child in adjacency_matrix[node]:
                if not dfs(child):
                    return False

            visited_nodes.remove(node)
            adjacency_matrix[node] = []
            return True

        for node in adjacency_matrix:
            if not dfs(node):
                return False

        return True