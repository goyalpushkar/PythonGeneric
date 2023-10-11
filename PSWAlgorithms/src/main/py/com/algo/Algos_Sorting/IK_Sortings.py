# Selection Sort

# Bubble Sort

# Insertion Sort

# Merge Sort

# Quick Sort
def quick_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """

    # Write your code here.

    def partition(arr, start, end):

        pivot_value = arr[start]

        smaller = start + 1
        bigger = end

        # Hoars
        # while smaller <= bigger:
        #     if arr[smaller] <= pivot_value:
        #         smaller += 1
        #     elif arr[bigger] >= pivot_value:
        #         bigger -= 1
        #     else:
        #         arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
        #         smaller += 1
        #         bigger -= 1

        # other
        done = True
        while done:
            while smaller <= bigger and arr[smaller] <= pivot_value:
                smaller += 1

            while smaller <= bigger and arr[bigger] >= pivot_value:
                bigger -= 1

            if smaller > bigger:
                done = False
            else:
                arr[smaller], arr[bigger] = arr[bigger], arr[smaller]

        # other 1
        # while smaller <= bigger:
        #     while smaller < len(arr)-1 and arr[smaller] <= pivot_value:
        #         smaller += 1

        #     while bigger > 0 and arr[bigger] > pivot_value:
        #         bigger -= 1

        #     if smaller < bigger:
        #         arr[smaller], arr[bigger] = arr[bigger], arr[smaller]

        arr[start], arr[bigger] = arr[bigger], arr[start]
        return bigger

    def sort(arr, start, end):

        # If start has exceeded the end
        if start >= end:
            return

        # Get pivot index
        # in case randomness required
        # Put random logic here and swap random index with index 0
        pivot_index = partition(arr, start, end)
        arr[start], arr[pivot_index] = arr[pivot_index], arr[start]
        # print(pivot_index)

        # Keep partitioning at pivot index
        sort(arr, start, pivot_index - 1)
        sort(arr, pivot_index + 1, end)

    sort(arr, 0, len(arr) - 1)

    return arr


# Heap Sort
def heap_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """

    # Write your code here.

    # This is for max heap so that sortify will sort the heap in ascendng order
    def get_child(arr, index, limit_end=None):
        if limit_end is None:
            limit_end = len(arr)

        child_left = 2 * index + 1
        child_right = 2 * index + 2

        # If left child is beyond array limit then return left index
        if child_left >= limit_end:
            return child_left

        # If right child is beyond array limit and left child is not then return left index
        elif child_right >= limit_end:
            return child_left

        # If left child is smaller than right child then return left index
        elif arr[child_left] >= arr[child_right]:
            return child_left

        else:
            return child_right

    # This is for max heap so that sortify will sort the heap in ascendng order
    def bubble_down(arr, index, limit_end=None):
        if limit_end is None:
            limit_end = len(arr)

        # Perform until the end of array limit
        while index < limit_end:
            # get eligible child
            eligible_child = get_child(arr, index, limit_end)

            # check if eligible child index is within limits and child value is
            # greater than parent then swap
            if eligible_child < limit_end and arr[eligible_child] > arr[index]:
                arr[eligible_child], arr[index] = arr[index], arr[eligible_child]
            else:
                break

            index = eligible_child

    def heapify(arr):
        index = len(arr) - 1

        while index >= 0:
            bubble_down(arr, index)
            index -= 1

    def sortify(arr):
        index = len(arr) - 1

        while index >= 0:
            # Swap max element at index 0 with last element for the loop
            arr[0], arr[index] = arr[index], arr[0]

            # Push 0th index element to down
            bubble_down(arr, 0, index)

            # reduce index by 1 as this element is at its position
            index -= 1

    # Heapify the array
    heapify(arr)

    # sortify the array
    sortify(arr)

    return arr
