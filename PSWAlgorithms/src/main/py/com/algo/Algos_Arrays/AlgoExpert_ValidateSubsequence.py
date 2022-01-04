'''
Given 2 non-empty arrays of integers, write a function athat determines whether the second array is subsequence of
the first one
A subsequence of an array is a set of numbers that arent necessarily adjacent in the array but that are in the same order
as they appear in the array. For instance numbers [1, 3, 4]form a subsequence of the array [1, 2, 3, 4]and so do the
numbers [2, 4]. Note that single number in an array and the array itself are both valid subsequences of the array

input_array = [5, 1, 22, 25, 6, -1, 8, 10]
Sequence = [1, 6, -1, 10]

output = True
'''

'''
Loop over array and check if element is in sequence
    if yes then move next in sequence
    
    if sequence index > len(sequence) then it is sub sequence and return from loop else not 

Normal test case:
input_array = [5, 1, 22, 25, 6, -1, 8, 10]
Sequence = [1, 6, -1, 10]

Same as input array
input_array = [5, 1, 22, 25, 6, -1, 8, 10]
Sequence = [5, 1, 22, 25, 6, -1, 8, 10]

Just one element in sequence
input_array = [5, 1, 22, 25, 6, -1, 8, 10]
Sequence = [1]

Out of sequence
input_array = [5, 1, 22, 25, 6, -1, 8, 10]
Sequence = [5, 1, 6, 22]
'''

def isValidSubsequence(array, sequence):
    # Write your code here.
    start_sequence_index = 0
    for index in range(len(array)):
        if sequence[start_sequence_index] == array[index]:
            start_sequence_index += 1

        if start_sequence_index == len(sequence):
            return 'true'

    if start_sequence_index < len(sequence):
        return 'false'


if __name__ == '__main__':
    input_array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [5, 1, 6, 22]
    print(input_array)

    output_result = isValidSubsequence(input_array, sequence)

    print(output_result)