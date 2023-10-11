'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.


Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''
class Solution:

    # Beats 70.17% 149 ms
    def merge(self, intervals):
        intervals = sorted(intervals)

        return_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            if return_intervals[-1][1] >= intervals[i][0]:
                return_intervals[-1][1] = max(return_intervals[-1][1], intervals[i][1])
            else:
                return_intervals.append(intervals[i])

        return return_intervals


    # Beats 49.52% 154 ms
    def merge(self, intervals):

        intervals = sorted(intervals)

        merged_interval = []
        return_intervals = []
        n = len(intervals)
        i = 0
        while i <= n-1:
            if merged_interval:
                check_interval = merged_interval
            else:
                check_interval = intervals[i]

            if i+1 < n and check_interval[1] >= intervals[i+1][0]:
                merged_interval = [min(check_interval[0], intervals[i + 1][0]),
                                   max(check_interval[1], intervals[i + 1][1])]
            else:
                merged_interval = []
                return_intervals.append(check_interval)

            i += 1

        if merged_interval:
            return_intervals.append(merged_interval)

        return return_intervals
        # merged_interval = []
        # return_intervals = []
        # i = len(intervals) - 1
        # # for i in range(len(intervals)-1,-1,-1):
        # while i >= 0:
        #     if merged_interval:
        #         check_interval = merged_interval
        #     else:
        #         check_interval = intervals[i]
        #
        #     if i >= 1 and check_interval[0] <= intervals[i - 1][1]:
        #         merged_interval = [min(check_interval[0], intervals[i - 1][0]),
        #                            max(check_interval[1], intervals[i - 1][1])]
        #         i -= 2
        #     else:
        #         if merged_interval and i == 0:
        #             check_interval = [min(check_interval[0], intervals[i][0]), max(check_interval[1], intervals[i][1])]
        #             return_intervals.append(check_interval)
        #             merged_interval = []
        #             break
        #         elif merged_interval:
        #             return_intervals.append(check_interval)
        #             merged_interval = []
        #
        #         return_intervals.append(intervals[i])
        #         i -= 1
        #
        # if merged_interval:
        #     return_intervals.append(merged_interval)
        #
        # return return_intervals