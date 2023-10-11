'''
There are n cities connected by some number of flights. You are given an array flights where flights[i]
 = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.


Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.


Constraints:
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
'''
import math
import heapq
class Solution:
    '''
        Bellman Ford and Djikstra
    '''
    # Beats 95.46% 100ms
    def findCheapestPrice(self, n, flights, src, dst, k):
        adjacency_mat = {i : [] for i in range(n)}
        for flight in flights:
            # print(f"flight: {flight}")
            adjacency_mat.get(flight[0], []).append((flight[1], flight[2]))
            # if flight[0] in adjacency_mat:
            #     adjacency_mat.get(flight[0], []).append((flight[1], flight[2]))
            # else:
            #     adjacency_mat[flight[0]] = [(flight[1], flight[2])]

        dist_mat = [math.inf] * n
        dist_mat[src] = 0
        # no of stops, node name, cost
        priority_q = [(0, src, 0)]
        heapq.heapify(priority_q)

        while priority_q:
            # no of stops, node name, cost
            node = heapq.heappop(priority_q)
            if node[0] > k:
                continue

            for neigh in adjacency_mat[node[1]]:
                if neigh[1] + node[2] < dist_mat[neigh[0]] and node[0] <= k:
                    dist_mat[neigh[0]] = neigh[1] + node[2]
                    heapq.heappush(priority_q, (node[0]+1, neigh[0], dist_mat[neigh[0]]))

        return -1 if dist_mat[dst] == math.inf else dist_mat[dst]

    # Beats 38.46% 239 ms
    def findCheapestPrice_neetCode(self, n, flights, src, dst, k):
        dist_mat = [math.inf] * n
        dist_mat[src] = 0

        for i in range(k+1):
            temp_dist_mat = dist_mat.copy()

            for flight in flights:
                # if the distance is still infinity skip it
                if dist_mat[flight[0]] == math.inf:
                    continue

                # source distance + edge length between source and des < dest distance
                # update dest distance
                if dist_mat[flight[0]] + flight[2] < temp_dist_mat[flight[1]]:
                    temp_dist_mat[flight[1]] = dist_mat[flight[0]] + flight[2]

            dist_mat = temp_dist_mat

        return -1 if dist_mat[dst] == math.inf else dist_mat[dst]

    # 28/52 passed
    # [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
    def findCheapestPrice_1st(self, n, flights, src, dst, k):
        # print(f"flights: {flights}")
        adjacency_mat = {} #  {i : [] for i in range(n)}
        for flight in flights:
            # print(f"flight: {flight}")
            if flight[0] in adjacency_mat:
                adjacency_mat.get(flight[0], []).append((flight[1], flight[2]))
            else:
                adjacency_mat[flight[0]] = [(flight[1], flight[2])]
        print(f"adjacency_mat: {adjacency_mat}\n\n")

        memo = {}
        visited_set = set()

        # final_routes = []
        def route(dest_node, cost, dist_from_source):
            # nonlocal final_routes
            # print(f"dest_node: {dest_node} \tcost:{cost} \tdist_from_source:{dist_from_source}\tvisited_set: {visited_set}\n\n")
            key = str(dest_node)  # str(src_node) + "," +

            visited_set.add(dest_node)
            # if key in memo:
            #     return memo[key]

            if dest_node == dst:
                # memo[key] = (cost, 0)
                return (cost, 0)

            if dest_node in adjacency_mat:
                curr_cost = math.inf
                for neigh in adjacency_mat[dest_node]:
                    # print(f"neigh: {neigh}\tvisited_set: {visited_set}")
                    if neigh[0] not in visited_set:
                        key = str(neigh[0])  # str(src_node) + "," +

                        neigh_cost = route(neigh[0], neigh[1], dist_from_source + 1)
                        visited_set.remove(neigh[0])
                        # print(f"neighbours: {neigh}\t {neigh_cost}\tvisited_set: {visited_set}")
                        if neigh_cost[1] is not None:
                            if neigh_cost[1] + dist_from_source <= k:
                                curr_cost = min(curr_cost, neigh_cost[0])
                                memo[key] = (curr_cost + cost, neigh_cost[1] + 1)
                                return (curr_cost + cost, neigh_cost[1] + 1)
                            # else:
                            #     memo[key] = (neigh_cost[0] + cost, None)
                        #         return (neigh_cost[0] + cost, None)
                        # else:
                        #     memo[key] = (neigh_cost[0] + cost, None)
                        #     return (neigh_cost[0] + cost, None)

                        # return memo[key]

            # memo[key] = (cost, None)
            return (cost, None)

        return_val = route(src, 0, 0)
        if return_val[1] is not None:
            return return_val[0]
        else:
            return -1