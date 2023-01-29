'''
The median is the middle value in an ordered integer list. If the size of the list is even,
 there is no middle value and the median is the mean of the two middle values.

Making it clear, when the input size is odd, we take the middle element of sorted data.
If the input size is even, we pick the average of the middle two elements in the sorted stream.

Example: arr = [2, 3, 4], the median is 3.
Example: arr = [1, -2, 3], the median is 1.

Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
addNum(int num) adds the integer num from the data stream to the data structure.
findMedian() returns the median of all elements so far.
Example
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
medianFinder = MedianFinder()
medianFinder.addNum(1)   # arr = [1]
medianFinder.addNum(2)    # arr = [1, 2]
medianFinder.findMedian() # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)    # arr[1, 2, 3]
medianFinder.findMedian() # return 2.0
Constraints
- Time: addNum: O(logn)
- Time: findMedian O(1)
- Space: O(n)

'''
''' 
use globals min_heap and max_heap, as per declared in driver code
use heapify modules , already imported by driver code
'''
import atexit
import io
import sys
import heapq
from collections import  defaultdict
import math

class Solution:
    def __init__(self):
        # self.median = Medians()
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)

    def balanceHeaps(self):
        # Balance the two heaps size , such that difference is not more than one.
        # code here
        '''
        You don't need to call getMedian it will be called itself by driver code
        for more info see drivers code below.
        '''

    def getMedian(self):
        # return the median of the data received till now.
        # code here
        if len(self.max_heap) == len(self.min_heap):
            median = (self.max_heap[0] - self.min_heap[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            median = self.max_heap[0]
        else:
            median = self.min_heap[0]

        return median

    def insertHeaps(self, x):
        heapq.heappush(self.max_heap, x)
        val = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, val)


#:param x: value to be inserted
#:return: None
# code here

# {
# Driver Code Starts.

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input("Enter no of test cases: "))
        ob = Solution()
        for i in range(n):
            x = int(input("Enter Element: "))
            ob.insertHeaps(x)
            print(math.floor(ob.getMedian()))

# } Driver Code Ends