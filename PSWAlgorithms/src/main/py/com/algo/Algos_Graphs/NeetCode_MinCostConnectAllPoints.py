'''
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them:
 |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple
path between any two points.


Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18


Constraints:
1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
'''
import math
import heapq
class Solution:

    # Beats 64.85% 1792ms
    # Beats 89.28% 1038 ms - After removing logic for preparing adjacency list
    def minCostConnectPoints(self, points):
        def get_distance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        N = len(points)
        # prepare adjacency list
        # adj_list = {i: [] for i in range(N)}
        # for i in range(N):
        #     for j in range(i+1, N):
        #         dist = get_distance(points[i], points[j])
        #         adj_list[i].append((dist, j))
        #         adj_list[j].append((dist, i))

        # Prims
        min_heap = []   # cost and node index
        heapq.heappush(min_heap, (0,0))
        visited = set()
        total_cost = 0
        while len(visited) < N:
            cost, index = heapq.heappop(min_heap)
            if index in visited:
                continue
            total_cost += cost
            visited.add(index)
            for i in range(N):
                if i not in visited:
                    dist = get_distance(points[index], points[i])
                    heapq.heappush(min_heap, (dist, i))
            # for neigh in adj_list[index]:
            #     if neigh[1] not in visited:
            #         heapq.heappush(min_heap, neigh)

        return total_cost

    # 98.58% 801ms
    def minCostConnectPoints(self, points):
        distance = [math.inf for i in range(len(points))]
        remaining = set([i for i in range(1, len(points))])

        def get_distance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        # def rec_help(point, sum):
        point = 0
        total_cost = 0
        while remaining:

            min_dist = math.inf
            min_point = None
            for check_point in remaining:
                dist = get_distance(points[point], points[check_point])
                distance[check_point] = min(distance[check_point], dist)
                if distance[check_point] < min_dist:
                    min_point = check_point
                    min_dist = distance[check_point]

            total_cost += min_dist
            point = min_point
            remaining.remove(point)

        return total_cost


    # def minCostConnectPoints_1st(self, points):
    #     visited = set()
    #     def get_distance(point1, point2):
    #         return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    #
    #     def rec_help(point, sum):
    #         min_dist = math.inf
    #         min_point = None
    #         for check_point in points:
    #             key = str(check_point[0]) + "," + str(check_point[1])
    #             if key not in visited:
    #                 dist = get_distance(point, check_point)
    #                 if dist < min_dist:
    #                     min_point = check_point
    #                     sum += dist
    #                     visited.add(key)
    #
    #         sum = rec_help(min_point, sum)
    #         return sum

        visited.add(str(points[0]) + "," + str(points[1]))
        rec_help(points[0])



