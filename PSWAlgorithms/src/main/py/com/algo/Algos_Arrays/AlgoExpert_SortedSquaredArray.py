'''
Write a function that takes in a non-empty array of integers that are sorted in ascending order and return a new array
of the same length with the squares of the original integers also sorted in ascending order

Input - array = [1,2,3,5,6,8,9]
Output - [1,4,9,25,36,64,81]

Optimal Time and Space should O(N) and O(N)
'''

'''
Approach 1 - take square of all the inputs and sort the final array - 
Time O( N log N ) because of sorting in the end, Space O (N)

'''

''' 
Test Cases
Normal - any sorted array
End cases - Array with negative numbers [-3, -4, 0, 2, 3]
'''

def usingSort(array):
    final_output = []
    for elem in array:
        final_output.append(elem*elem)

    final_output.sort()

    return final_output


def using2Pointers(array):
    final_output = [0] * len(array)
    start = 0
    end = len(array) - 1
    final_index = len(array) - 1

    while start <= end:
        if abs(array[start]) > abs(array[end]):
            final_output[final_index] = array[start]*array[start]
            start += 1
        else:
            final_output[final_index] = array[end]*array[end]
            end -= 1

        final_index -= 1

    return final_output


if __name__ == '__main__':
    input_array = [1, 2, 3, 5, 6, 8, 9]
        # [-4, -3, 0, 2, 3, 5, 6]
    print(input_array)

    output_array = usingSort(input_array)
    output_array_1 = using2Pointers(input_array)

    print(output_array)
    print(output_array_1)