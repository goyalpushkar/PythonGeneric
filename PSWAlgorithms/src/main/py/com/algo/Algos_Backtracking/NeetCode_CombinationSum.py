'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150
combinations for the given input.


Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

'''
class Solution:
    # [7,3,2] and 18
    # [2,3,6,7] and 7

    '''
    If you think of all possible combinations in that problem as a tree, it has a branching factor of N
    (unique number of candidates). Additionally, the maximum possible height of the tree is the Target divided
    by the value of the smallest Candidate i.e. the longest possible combination.

    For instance Target = 6, Candidates = [2,3,6] the longest possible combination is [2, 2, 2].
    All valid combinations must be length 3 or shorter.

    Thus the height of the tree is limited to (T/M) and the branching factor is N.
    Thus the max possible nodes in the combinatorial tree is N ^ (T/M). You can google this relation
    between the height of a tree, branching factor and number of nodes.
    '''

    # beats 34% 82 ms
    def combinationSum_rec(self, candidates, target):

        final_path = []
        # cache = {}  Including cache increased time limit as may be looping through current path is not good
        def combination_helper(candidates, target, curr_path):
            nonlocal final_path

            # elems = ",".join(str(e) for e in curr_path)
            # key = str(target)+'_'+elems
            # print(f"candidates: {candidates} \t target: {target}\n"
            #       f"curr_path: {curr_path}\t final_path:{final_path}\n"
            #       f"cache:{cache}")

            # if key in cache:
            #     return cache[key]

            if target == 0:
                # cache[key] = curr_path
                final_path.append(curr_path)
                return  curr_path[:-1] # ways

            if len(candidates) == 0 or target < 0 or curr_path is None:
                return curr_path[:-1] # 0

            curr_path = combination_helper(candidates, target-candidates[0], curr_path + [candidates[0]])
            curr_path = combination_helper(candidates[1:], target, curr_path)

            return curr_path  # ways

        combination_helper(candidates, target, [])
        return final_path

        # Count number of ways
        # def combination_helper(candidates, target, ways):
        #
        #     nonlocal final_path
        #     if target == 0:
        #         ways += 1
        #         return ways
        #
        #     if len(candidates) == 0 or target < 0:
        #         return 0
        #
        #     ways = combination_helper(candidates, target-candidates[0], ways) + \
        #            combination_helper(candidates[1:], target, ways)
        #
        #     return ways

    # beats 92% 51 ms more efficient then recursive approach
    # [7,3,2] and 18
    def combinationSum(self, candidates, target):
        # declare empty result set for all values from 0 -- target value
        # value of result set is a tuple with (number of ways, way value)
        # candidates = sorted(candidates)
        res = [(1, [[]]) if val == 0 else (0, None) for val in range(target+1)]

        # print(f"before start: {res}")
        # candidates - 2,3,6,7 target - 7
        for i in range(1, len(candidates)+1):  # candidates - 1, 2, 3, 4 e.g. (2,3,6,7)
            current_cand = candidates[i-1]
            for val in range(1, target + 1):   # target - 0-7
                prev_row = res[val]
                # print(f"row: {i} col: {val}\n"
                #       f"prev_row: {prev_row}")
                new_target = val - current_cand
                if new_target >= 0:
                    new_target_val = res[new_target]
                    new_target_val_num = new_target_val[0]
                    new_target_val_array = new_target_val[1]
                    # print(f"new_target_val: {new_target_val}\t new_target_val_array: {new_target_val_array}")
                    if new_target_val_num > 0:
                        # Gt the result set from prev candidate and append to it if prev candidate result is 1
                        # new_target_val[1].append(current_cand)
                        if prev_row[0] > 0:
                            new_0 = prev_row[0] + new_target_val_num
                            new_array = prev_row[1]
                            new_array_list = [arr + [current_cand] for arr in new_target_val_array]
                            new_1 = new_array + new_array_list
                            res[val] = (new_0, new_1)
                        else:
                            new_1 = [arr + [current_cand] for arr in new_target_val_array]
                            res[val] = (new_target_val_num, new_1)
                    else:   # new_target is not deduced using candidates so it is not possible to acheive current target
                        res[val] = prev_row # new_target_val
                # if target becomes negative copy value from above row
                else:
                    res[val] = prev_row
                # print(f"current_val: {val}: {res[val]}")

            # print(f"current row: {res}\n\n")

        print(f"res: {res}\n"
              f"No of ways: {res[-1][0]} \t Ways: {res[-1][1]}")
        # res[-1][-1] - last value in the matrix [0] number of ways. [1] - all the ways combinations
        return res[-1][1]

    # permutations
    def combinationSum_perm(self, candidates, target):
        # declare empty result set for all values from 0 -- target value
        # value of result set is a tuple with (number of ways, way value)
        candidates = sorted(candidates)
        res = [(1, [[]]) if val == 0 else (0, []) for val in range(target+1)]

        # print(f"before start: {res}")
        # candidates - 2,3,6,7 target - 7
        for val in range(1, target + 1):  # target - 0-7
            for i in range(len(candidates)):  # candidates - 1, 2, 3, 4 e.g. (2,3,6,7)
                new_target = val - candidates[i]
                prev_val = res[val]
                print(f"row: {val} col: {candidates[i]}\n"
                      f"prev_val: {prev_val} \t new_target: {new_target}")
                if new_target >= 0:
                    new_target_val = res[new_target]
                    print(f"new_target_val: {new_target_val}")
                    # if new_target is acheievable i.e. [0] > 0 then add permutations
                    if new_target_val[0] > 0:
                        new_val_num = new_target_val[0]
                        new_val_arr = [arr + [candidates[i]] for arr in new_target_val[1]]

                        # Check if already some permutations for current val then add it to them
                        if prev_val[0] > 0:
                            new_0 = prev_val[0] + new_val_num
                            new_1 = prev_val[1] + new_val_arr
                            res[val] = (new_0, new_1)
                        else:
                            res[val] = (new_val_num, new_val_arr)
                else:
                    res[val] = res[val]

                print(f"current res: {res}")

        print(f"res: {res}\n"
              f"No of ways: {res[-1][0]} \t Ways: {res[-1][1]}")
        # res[-1][-1] - last value in the matrix [0] number of ways. [1] - all the ways combinations
        return res[-1][1]


    def combinationSum_matrix(self, candidates, target):
        # declare empty result set for all values from 0 -- target value
        # value of result set is a tuple with (number of ways, way value)
        candidates = sorted(candidates)
        res = [[(1, [[]]) if val == 0 else (0, None) for val in range(target+1)]
               for i in range(0, len(candidates)+1)]

        # print(f"before start: {res}")
        # candidates - 2,3,6,7 target - 7
        for i in range(1, len(candidates)+1):  # candidates - 1, 2, 3, 4 e.g. (2,3,6,7)
            current_cand = candidates[i-1]
            for val in range(1, target + 1):   # target - 0-7
                prev_row = res[i-1][val]
                # print(f"row: {i} col: {val}\n"
                #       f"prev_row: {prev_row}")
                new_target = val - current_cand
                if new_target >= 0:
                    new_target_val = res[i][new_target]
                    new_target_val_array = new_target_val[1]
                    new_target_val_num = new_target_val[0]
                    # if new_target_val_num > 0:
                    #     new_target_val_array = new_target_val[1][-1]
                    # print(f"new_target_val: {new_target_val}\t new_target_val_array: {new_target_val_array}")
                    if new_target_val_num > 0:
                        # Gt the result set from prev candidate and append to it if prev candidate result is 1
                        # new_target_val[1].append(current_cand)
                        new_target_val_array = new_target_val[1][-1]
                        if prev_row[0] > 0:
                            new_0 = prev_row[0] + new_target_val_num
                            new_array = prev_row[1]
                            new_array_list = [arr + [current_cand] for arr in new_target_val_array]
                            new_1 = new_array + new_array_list
                            res[i][val] = (new_0, new_1)
                        else:
                            new_1 = [arr + [current_cand] for arr in new_target_val_array]
                            res[i][val] = (new_target_val_num, new_1)
                    else:   # new_target is not deduced using candidates so it is not possible to acheive current target
                        res[i][val] = prev_row # new_target_val
                # if target becomes negative copy value from above row
                else:
                    res[i][val] = prev_row
                # print(f"current_val: {res[i][val]}")

            # print(f"current row: {res[i]}\n\n")

        # print(f"res: {res}")
        # res[-1][-1] - last value in the matrix [0] number of ways. [1] - all the ways combinations
        return res[-1][-1][1]


    def combinationSum_eff(self, candidates, target):
        res = []

        def dfs(sum, arr, start):
            if sum == target:
                res.append(arr[:])
            else:
                for i in range(start, len(candidates)):
                    num = candidates[i]
                    if target >= num + sum:
                        arr.append(num)
                        dfs(num + sum, arr, i)
                        arr.pop()

        dfs(0, [], 0)
        return res

