'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
'''
class Solution:
    # Beats 85.25% 79 ms
    def insert(self, intervals, newInterval):
        res = []

        for index in range(len(intervals)):
            # new interval before current interval
            if newInterval[1] < intervals[index][0]:
                res.append(newInterval)
                return res + intervals[index:]
            # new interval after current interval
            elif newInterval[0] > intervals[index][1]:
                res.append(intervals[index])
            # else overlapping
            else:
                newInterval = [min(newInterval[0], intervals[index][0]), max(newInterval[1], intervals[index][1])]

        res.append(newInterval)
        return res

    # Beats 69.35% 83 ms
    def insert_1st(self, intervals, newInterval):
        new_start = None
        new_end = None
        new_insert = True
        return_intervals = []

        for interval in intervals:
            if new_start is None:
                if newInterval[0] in range(interval[0], interval[1] + 1):
                    new_start = min(interval[0], newInterval[0])
                else:
                    if newInterval[0] < interval[0]:
                        new_start = newInterval[0]

            if new_end is None:
                if newInterval[1] in range(interval[0], interval[1] + 1):
                    new_end = max(interval[1], newInterval[1])
                else:
                    if new_start is not None and newInterval[1] < interval[0]:
                        new_end = newInterval[1]

            if new_start is not None and new_end is not None and new_insert:
                return_intervals.append([new_start, new_end])
                new_insert = False

            if new_start is None and new_end is None:
                return_intervals.append(interval)

            if new_end is not None and new_end < interval[0]:
                return_intervals.append(interval)

        if new_start is None and new_end is None:
            return_intervals.append(newInterval)

        if new_start is not None and new_end is None:
            new_end = newInterval[1]
            return_intervals.append([new_start, new_end])

        return return_intervals

    # Beats 99% 59ms
    def insert(self, intervals, newInterval):
        l, r = [], []

        for interval in intervals:
            # new interval after current interval, append current interval to left
            if interval[1] < newInterval[0]:
                l.append(interval)
            # new interval after current interval, append current interval to right
            elif interval[0] > newInterval[1]:
                r.append(interval)
            else:
                newInterval = (min(interval[0], newInterval[0]), \
                               max(interval[1], newInterval[1]))
        return l + [newInterval] + r