# a,b,c is a triplet if -> a < b > c or a > b < c

# Input is a numbers array
# Output is an array with values as 1 (triplet) or 0 (not triplet) for each set of 3 numbers
def solution(numbers):
    output_values = []
    for index in range(0, len(numbers)):
        a = numbers[index]
        b = numbers[index+1]
        c = numbers[index+2]

        if (a < b > c) or (a > b < c):
            output_values.append(1)
        else:
            output_values.append(0)

    return output_values

if __name__ == '__main__':
    numbers = []
    solution(numbers)

