'''
Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
class Solution:
    # beats 58.68%
    def topKFrequent(self, nums, k):
        # Approach 1
        # create a dictionary of nums and their occurrences -> T O(N) and S O(N)
        # sort dictionary by values -> T O(N log N)
        # loop over dictionary to return keys until k keys are derived  -> T O(N) and S O(k)
        key_val = {}
        for num in nums:
            if num in key_val:
                key_val[num] += 1
            else:
                key_val[num] = 1

        # sorted_array = sorted(key_val, reverse=False)  # It will sort by keys
        sorted_key_val = dict(sorted(key_val.items(), key=lambda x: x[1], reverse=True))

        # print(sorted_array)
        print(sorted_key_val)

        return_arr = []
        # for k in range(k):
        #     return_arr.append(sorted_array[k])
        for key, value in sorted_key_val.items():
            if len(return_arr) < k:
                return_arr.append(key)
            else:
                break

        return return_arr

    # beats 22.4%
    def topKFrequent_heap(self, nums, k):
        # Approch 2
        # create a dictionary of nums and their occurrences -> T O(N) and S O(N)
        # create a max heap of values of dict -> O(N)
        # return top k elements from the heap -> O(N)
        import heapq
        key_val = {}
        for num in nums:
            if num in key_val:
                key_val[num] += 1
            else:
                key_val[num] = 1

        new_list = [(-1*value, key) for key, value in key_val.items()]
        heapq.heapify(new_list)

        # new_list = []
        # for entry in key_val:
        #     it is inserting min values and keeping only k entries in the heap
        #     so that max k will stay in the new_list
        #     heapq.heappush(new_list, (key_val[entry], entry))
        #     if k <= 0:
        #         heapq.heappop(new_list)
        #     k -= 1

        return_arr = []
        for i in range(k):
        # for elem in new_list:
            return_arr.append(heapq.heappop(new_list)[1])
            # return_arr.append(elem[1])

        return return_arr