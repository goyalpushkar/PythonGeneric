'''


'''

class Solution:

    def generate_all_combinations(arr, target):
        result = []

        memo = set()
        # 2 failed with Time Limit exceeded
        def helper_TLE(i, sol, sum):
            key = "".join(str(elem) for elem in sorted(sol)) + '_' + str(sum)

            # print(i, '-', sol, '-', key, '****', memo, '****', sum)

            if key in memo:  # +'_'+str(i-1)
                return

            if sum == target:
                result.append(sol.copy())
                memo.add(key)
                return

            if i == len(arr) or sum > target:
                return
            else:
                # left exclude branch
                helper_TLE(i + 1, sol, sum)
                # memo.add("".join(str(elem) for elem in sorted(sol))+'_'+str(sum))   # +'_'+str(i)

                # right include branch
                sol.append(arr[i])
                helper_TLE(i + 1, sol, sum + arr[i])
                # memo.add("".join(str(elem) for elem in sorted(sol))+'_'+str(sum+arr[i]))   # +'_'+str(i)
                sol.pop()

        def helper(sol, sum_till, index):
            # print(sol, '-', sum, '-', index)
            if sum_till == target:
                result.append(sol.copy())
                return

            # if all elements of array sum is less than target then no point of checking the
            # array
            if (sum(arr[index:]) + sum_till < target):
                return

            # print(sum(arr))
            if sum_till > target:  # sum(arr[index:])
                return
            else:
                popped = None
                for i in range(index, len(arr)):
                    if popped != arr[i]:
                        if sum_till + arr[i] <= target:
                            sol.append(arr[i])
                            helper(sol, sum_till + arr[i], i + 1)
                            popped = sol.pop()

        arr = sorted(arr)
        helper([], 0, 0)
        return result

        # helper_TLE(0, [], 0)
        # return result
