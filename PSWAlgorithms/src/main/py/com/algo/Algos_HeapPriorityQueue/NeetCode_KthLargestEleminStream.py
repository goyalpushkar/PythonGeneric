'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order,
 not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element
in the stream.

Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

Constraints:
1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
'''
import heapq

# Beats 72.32% 97ms
class KthLargest:
    import heapq
    # Beats 80.82% 95ms
    def __init__(self, k, nums):
        self.nums = nums
        self.k = k

        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

        # print(self.nums)

    def add(self, val):
        # print(f"{self.nums[0]} \t {val} \t {self.nums}")
        if (len(self.nums) < self.k):
            heapq.heappush(self.nums, val)

        elif val > self.nums[0]:
            heapq.heappushpop(self.nums, val)

        return self.nums[0]

# Beats 80.82% 95ms
class KthLargest_1st:

    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        self.heap_arr = []

        sorted_arr = sorted(self.nums)
        # print(f"sorted_arr: {sorted_arr} \t k:{k}")
        for i in range(len(sorted_arr) - 1, - 1, -1):
            # print(f"i: {i} \t {self.heap_arr} \t {len(self.heap_arr)}")
            if len(self.heap_arr) < self.k:
                heapq.heappush(self.heap_arr, sorted_arr[i])
            else:
                break

        # print(self.heap_arr)

    def add(self, val):
        # print(f"{self.heap_arr[0]} \t {val} \t {self.heap_arr}")
        self.nums.append(val)
        if (len(self.heap_arr) < self.k):
            heapq.heappush(self.heap_arr, val)

        elif val > self.heap_arr[0]:
            heapq.heappop(self.heap_arr)
            heapq.heappush(self.heap_arr, val)

        return self.heap_arr[0]

    # 9/10 Output Limit exceeded
        # heapq.heappush(self.heap_arr, -val)
        # get_elems = []
        # for i in range(self.k):
        #     get_elems.append(heapq.heappop(self.heap_arr))
        #
        # print(get_elems)
        # return_val = -1 * get_elems[-1]
        # for i in range(len(get_elems)):
        #     heapq.heappush(self.heap_arr, get_elems[i])
        #
        # return return_val