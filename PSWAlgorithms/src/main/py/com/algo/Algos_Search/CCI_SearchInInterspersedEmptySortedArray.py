'''
Given a sorted array of strings which is interspersed with empty strings, write a method to find the location of a given string.
Example: find “ball” in [“at”, “”, “”, “”, “ball”, “”, “”, “car”, “”, “”, “dad”, “”, “”] will return 4
# at "" "" "" ball "" "" car "" "" dad "" ""
Example: find “ballcar” in [“at”, “”, “”, “”, “”, “ball”, “car”, “”, “”, “dad”, “”, “”] will return -1
at "" "" "" "" ball car "" "" dad "" ""
'''

def search_element(arr, element):
    if element is None or arr is None:
        return -1

    if element == "":
        for i in range(len(arr)):
            if arr[i] == element:
                return i

    return search_element_util(arr, element, 0, len(arr)-1)

def search_element_util(arr, element, low, high):
    while low <= high:
        #print("low high", low, " ", high, " ", arr[high])
        while '""'.__eq__(arr[high]) and low <= high:  #not arr[high]  arr[high] == ""
            #print("inside high")
            high -= 1

        if high < low:
            return -1
        
        mid = ( low + high ) // 2
        #print("mid: ", mid, " - ", arr[mid])
        while '""'.__eq__(arr[mid]):  # not arr[mid] arr[mid] == ""
            #print("inside mid")
            mid += 1

        #print("new mid: ", mid)
        if element == arr[mid]:
            return mid

        if element < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

if __name__ == '__main__':
    arr = list( map(str, input("Sorted Array: ").strip().split()) )
    element = str(input("Element to be found: "))

    print(arr)
    index_at = search_element(arr, element)

    print( index_at, end=" ")