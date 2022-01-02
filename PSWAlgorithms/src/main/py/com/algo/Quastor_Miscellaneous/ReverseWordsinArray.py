'''

You are given a character array containing a set of words separated by whitespace.

Your task is to modify that character array so that the words all appear in reverse order.

Do this without using any extra space.

Example

input - ['A', 'l', 'i', 'c', 'e', ' ', 'l', 'i', 'k', 'e', 's', ' ', 'B', 'o', 'b']

output - ['B', 'o', 'b', ' ', 'l', 'i', 'k', 'e', 's', ' ', 'A', 'l', 'i', 'c', 'e']

https://leetcode.com/problems/reverse-words-in-a-string/
'''

def reverseArray(input_array):
    word = []
    final_array = []
    print(input_array)
    for i in range(len(input_array)-1, -1, -1):
        if input_array[i] == ' ':
            for word_index in range(len(word)):
                final_array.append(word.pop())

            # start should not have empty character and end shouldnt have empty characters
            if final_array[-1] != ' ':
                final_array.append(input_array[i])

        else:
            word.append(input_array[i])

    if len(word) > 0:
        for word_index in range(len(word)):
            final_array.append(word.pop())

    print(final_array)
    final_array = ''.join(final_array)
    return final_array


if __name__ == '__main__':
    input_string = "  hello  world a  "
        #"the sky is blue"
    input = [char for char in input_string.strip()]
    output = reverseArray(input)
    print(output)