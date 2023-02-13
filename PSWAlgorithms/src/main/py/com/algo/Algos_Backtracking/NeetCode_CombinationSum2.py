'''
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

'''
from collections import Counter
class Solution:
    def combinationSum2(self, candidates, target):
        # create key value pair
        candidates_kv = Counter(candidates)
        candidates = list(set(candidates))

        res = [(1, [[]]) if i == 0 else (0, None) for i in range(target+1)]
        # print(f"before start: {res}\n"
        #       f"candidates_kv: {candidates_kv}")
        for row in range(1, len(candidates)+1):
            curr_cand = candidates[row - 1]
            for col in range(1, target+1):
                prev_row = res[col]
                new_target = col - curr_cand
                # print(f"row: {row} col: {col} curr_cand: {curr_cand} new_target: {new_target}\n"
                #       f"prev_row: {prev_row} candidates_kv: {candidates_kv}")
                if new_target >= 0 and candidates_kv[curr_cand] > 0:  #
                    new_target_val = res[new_target]
                    # print(f"new_target_val: {new_target_val}")
                    if new_target_val[0] > 0:
                        new_array = []
                        for arr in new_target_val[1]:
                            existing_vals = Counter(arr)
                            # print(f"existing_vals: {existing_vals}")
                            if existing_vals.get(curr_cand, 0) + 1 <= candidates_kv[curr_cand]:
                                # print(f"{arr + [curr_cand]}")
                                new_array.append(arr + [curr_cand])

                        # print(f"new_array: {new_array}")
                        if prev_row[0] > 0:
                            new_array = prev_row[1] + new_array
                            res[col] = (new_target_val[0] + prev_row[0], new_array)
                        else:
                            res[col] = (new_target_val[0], new_array)
                        # candidates_kv[curr_cand] -= 1
                    else:
                        res[col] = prev_row
                else:
                    res[col] = prev_row

            #     print(f"current_col: {res[col]}")
            #
            # print(f"res[row]: {res}\n\n")

        print(f"res: {res}\n"
              f"No of ways: {res[-1][0]} \t Ways: {res[-1][1]}")
        return res[-1][1]



