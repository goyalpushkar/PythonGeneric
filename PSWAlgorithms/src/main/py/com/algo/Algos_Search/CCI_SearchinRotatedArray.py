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