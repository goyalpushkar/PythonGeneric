'''
Write a function that takes a non-empty string and returns a boolean representing whether string is a palindrome

A palindrome is defined as a string that's written the same forward and backward. Note that single character strings are
palindrome

input = "abcdcba"
Output = true

input = "abba"
Output = true

input = "abc"
Output = false

input = "a"
Output = true

first_index = 0
last_index = len(input)-1
start from first and last index exit if first_index >= second_index
    check if input(first_index) == input(last_index)
        increment first_index and decrement last_index
    else
        return false
'''

def isPalindrome(string):
    # Write your code here.
    first_index = 0
    last_index = len(string) - 1
    while first_index < last_index:
        if string[first_index] == string[last_index]:
            first_index += 1
            last_index -= 1
        else:
            return False

    return True


if __name__ == '__main__':
    input_sequence = "a"
    print(input_sequence)

    output_result = isPalindrome(input_sequence)

    print(output_result)
