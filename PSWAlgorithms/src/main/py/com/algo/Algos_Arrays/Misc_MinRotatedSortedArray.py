'''
A sorted array has been rotated so that the elements might appear in the order 3 4 5 6 7 1 2. How would you find the minimum element?
'''

def min_element(arr):

    print(arr)
    min_element.min_number = float('inf')  #if negative numbers are allowed then pass infinity
    return min_find(arr)
    #print(min_value)
    #return min_value

def min_find(arr):
    #minimum = 0
    print(arr, min_element.min_number)
    if len(arr) == 0:
        return min_element.min_number

    mid = len(arr) // 2

    if arr[0] < arr[mid]:
        if min_element.min_number > arr[0]:
            min_element.min_number = arr[0]
        #return min_find(arr[mid + 1:])
    else:
        if min_element.min_number > arr[mid]:
            min_element.min_number = arr[mid]
        #return min_find(arr[:mid+1])

    if len(arr) == 1:
        return min_element.min_number

    return min_find(arr[mid + 1:])
    #return min_number


if __name__ == '__main__':
    test_cases = int(input("No of test cases: "))
    for i in range(test_cases):

        arr = list(map(int, input().rstrip().split()))

        min_value = min_element(arr)
        print(min_value)
