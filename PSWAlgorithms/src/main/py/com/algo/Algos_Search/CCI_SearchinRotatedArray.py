'''
Given a sorted array of n integers that has been rotated an unknown number of times, give an O(log n) algorithm that finds an element in the array. You may assume that the array was originally sorted in increasing order.
EXAMPLE:
Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
Output: 8 (the index of 5 in the array)
'''

'''
low < mid -- Increasing in this half
  elem > mid
    low = mid + 1
  elem < mid
     high = mid - 1
  
low > mid -- Increasing and Decreasing in this half
'''

class Solution:
    def search(self, nums, target):
        import math

        # beats 30.90%   # 63.6%
        def search_helper(low, high):
            while low <= high:
                mid = math.floor(high - (high - low) / 2)
                print(f"low: {low} high: {high} mid: {mid} arr[mid]: {nums[mid]}")

                if nums[mid] == target:
                    return mid

                # lower half sorted
                if nums[low] <= nums[mid]:
                    if target > nums[mid]:
                        low = mid + 1
                    elif target >= nums[low]:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif target < nums[mid]:
                    high = mid - 1
                elif target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        # beats 45.39%
        def search_helper_recu(low, high):
            mid = math.floor(high - ((high - low) / 2))

            if low >= high:
                return -1

            if target == nums[mid]:
                return mid
            else:
                # Logic 3
                # if mid > low lower half is sorted
                # else upper half is sorted

                # check if key is between lower and upper boundary of sorted array if yes then key should be in that
                # part else in other half
                if nums[mid] > nums[low]:
                    # Lower half is sorted - low, mid
                    if target >= nums[low] and target <= nums[mid]:
                        return search_helper(low, mid)
                    else:
                        return search_helper(mid + 1, high)
                else:
                    # upper half is sorted - mid+1, high
                    if target >= nums[mid] and target <= nums[high - 1]:
                        return search_helper(mid + 1, high)
                    else:
                        return search_helper(low, mid)

        # beats 30.90% -
        # removing = from < mid or > mid condition and using and target improved performance 87.66%
        def search_helper_self(low, high):

            while low <= high:
                mid = math.floor(high - (high-low)/2)
                print(f"low: {low} high: {high} mid: {mid} arr[mid]: {nums[mid]}")

                if nums[mid] == target:
                    return mid

                # lower half sorted
                if nums[low] <= nums[mid]:
                    if nums[low] <= target and target < nums[mid]:
                        # search in sorted lower half
                        high = mid-1
                    else:
                        # while mid+1 < high and nums[mid+1] > nums[mid]:
                        #     mid += 1

                        low = mid+1

                # upper half sorted
                else:
                    if nums[mid] < target and target <= nums[high]:
                        # search in sorted lower half
                        low = mid + 1
                    else:
                        # while mid - 1 >= low and nums[mid - 1] < nums[mid]:
                        #     mid -= 1
                        high = mid - 1

            return -1

        # return search_helper(0, len(nums) - 1)
        # return search_helper_recu(0, len(nums))
        return search_helper_self(0, len(nums)-1)


def search_element(arr1, element):
    return search_element_helper1(arr1, element, 0, len(arr1)-1)

#Actual from book
def search_element_helper(arr1, element, low, high):

    while low <= high:
        print("low: ", low, " high: ", high)
        mid = ( low + high ) // 2

        print("mid: ", mid)
        if element == arr1[mid]:
            return mid
        elif arr1[low] <= arr1[mid]: #Increasing sequence
            if element > arr1[mid]:
                low = mid +1
            elif element >= arr1[low]:
                high = mid - 1
            else:
                low = mid + 1
        elif element < arr1[mid]:
            high = mid - 1
        elif element <= arr1[high]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

#self
def search_element_helper1(arr1, element, low, high):

    while low <= high:
        print("low: ", low, " high: ", high)
        mid = ( low + high ) // 2

        print("mid: ", mid)
        if element == arr1[mid]:
            return mid
        elif arr1[low] <= arr1[mid]: #Increasing sequence
            if element > arr1[mid]:
                low = mid +1
            elif element > arr1[low]:
                high = mid - 1
            else:
                low = mid + 1
        elif element < arr1[mid]:
            high = mid - 1
        elif element > arr1[mid] and element <= arr1[high]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == '__main__':
    arr1 = list( map(int, input("Rotated Sorted Array: ").strip().split()) )
    element = int(input("Element to be found: "))
    index_at = search_element(arr1, element)

    print( index_at, end=" ")