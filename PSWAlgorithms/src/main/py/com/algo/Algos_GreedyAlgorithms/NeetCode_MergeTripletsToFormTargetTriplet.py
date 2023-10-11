'''
A triplet is an array of three integers. You are given a 2D integer array triplets,
where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer
array target = [x, y, z] that describes the triplet you want to obtain.

To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become
[max(ai, aj), max(bi, bj), max(ci, cj)].
For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to
 [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or
false otherwise.


Example 1:
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the last triplet to be
[max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4],[2,7,5]]
The target triplet [2,7,5] is now an element of triplets.

Example 2:
Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false
Explanation: It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.

Example 3:
Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]. Update the third triplet to be
[max(2,1), max(5,2), max(3,5)] = [2,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
- Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. Update the fourth triplet to be
[max(2,5), max(5,2), max(5,3)] = [5,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
The target triplet [5,5,5] is now an element of triplets.

Constraints:
1 <= triplets.length <= 105
triplets[i].length == target.length == 3
1 <= ai, bi, ci, x, y, z <= 1000
'''
class Solution:
    # Beats 97.9% 1963ms
    def mergeTriplets(self, triplets, target):

        good_triplet = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for k, v in enumerate(t):
                if v == target[k]:
                    good_triplet.add(k)

            if len(good_triplet) == 3:
                return True

        return False  # len(good_triplet) == 3

    # 48/62 Time Limit Exceeded
    def mergeTriplets_TLE(self, triplets, target):
        memo = {}

        def dfs(index, curr_val, visited_index):
            # print(f"index: {index}\t curr_val: {curr_val}")
            key = ",".join(str(curr_val))
            if key in memo: return memo[key]

            if len(curr_val) > 0 and curr_val[0] == target[0] and curr_val[1] == target[1] and curr_val[2] == target[2]:
                return True

            for i in range(len(triplets)):
                # print(f"i: {i}\t {triplets[i]}\t visited_index:{visited_index}")
                if i not in visited_index and triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and \
                        triplets[i][2] <= target[2]:
                    if len(curr_val) > 0:
                        new_val = [max(triplets[i][0], curr_val[0]), max(triplets[i][1], curr_val[1]),
                                   max(triplets[i][2], curr_val[2])]
                    else:
                        new_val = triplets[i]
                    visited_index.add(i)
                    check_val = dfs(i, new_val, visited_index)
                    visited_index.remove(i)
                    # print(f"i: {i}\t {check_val}")
                    if check_val:
                        memo[key] = True
                        return True

            memo[key] = False
            return False

        return dfs(None, [], set())
        # for i in range(len(triplets)):
        #     memo = {}
        #     visited_index = set()
        #     visited_index.add(i)
        #     # print(f"\n\nStart: {i}")
        #     if dfs(i, triplets[i], visited_index):
        #         return True

        # return False

    # 48/62 Time Limit Exceeded
    def mergeTriplets_TLE(self, triplets, target):

        '''
        [[7,15,15],[11,8,3],[5,3,4],[12,9,9],[5,12,10],[7,15,10],[7,6,4],[3,9,8],[2,13,1],[14,2,3]]
        [14,6,4]
        Expected True
        '''

        def dfs(index, curr_val, visited_index):
            # print(f"index: {index}\t curr_val: {curr_val}")
            if index in memo: return memo[index]

            if curr_val[0] == target[0] and curr_val[1] == target[1] and curr_val[2] == target[2]:
                return True

            for i in range(len(triplets)):
                # print(f"i: {i}\t {triplets[i]}\t visited_index:{visited_index}")
                if i not in visited_index and triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and \
                        triplets[i][2] <= target[2]:
                    new_val = [max(triplets[i][0], curr_val[0]), max(triplets[i][1], curr_val[1]),
                               max(triplets[i][2], curr_val[2])]
                    visited_index.add(i)
                    check_val = dfs(i, new_val, visited_index)
                    visited_index.remove(i)
                    # print(f"i: {i}\t {check_val}")
                    if check_val:
                        memo[index] = True
                        return True

            memo[index] = False
            return False

        for i in range(len(triplets)):
            memo = {}
            visited_index = set()
            visited_index.add(i)
            # print(f"\n\nStart: {i}")
            if dfs(i, triplets[i], visited_index):
                return True

        return False