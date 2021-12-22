'''
You are given two sorted arrays, A and B, and A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order
'''

def merge_two_Arrays(arr1, arr2):
    arr1_length = len(arr1) - 1
    arr2_length = len(arr2) - 1
    final_arr_length = arr1_length + arr2_length + 1

    arr1 += arr2

    while arr1_length >= 0 and arr2_length >= 0:
        #print(arr1_length, " : ", arr1[arr1_length], " ", arr2_length, " : ", arr2[arr2_length], " ")
        if arr1[arr1_length] > arr2[arr2_length]:
            arr1[final_arr_length] = arr1[arr1_length]
            arr1_length -= 1
        else:
            arr1[final_arr_length] = arr2[arr2_length]
            arr2_length -= 1

        final_arr_length -= 1

    while arr2_length >= 0:
        arr1[final_arr_length] = arr2[arr2_length]
        arr2_length -= 1
        final_arr_length -= 1

    return arr1


if __name__ == '__main__':
    arr1 = list( map(int, input("First Array: ").strip().split()) )
    arr2 = list( map(int, input("Second Array: ").strip().split()) )

    final_arr = merge_two_Arrays(arr1, arr2)

    for index in range(len(final_arr)):
        print( final_arr[index], end=" ")