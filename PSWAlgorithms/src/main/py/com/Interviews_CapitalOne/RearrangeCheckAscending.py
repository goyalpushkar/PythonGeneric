# elements of an array are rearranged such that first element is a[0], a[last], a[1], a[last-1]....
# Return true if resultant array is sorted or false if not


def solution(numbers):
    return_value = False
    last_element = numbers[0]-1
    total_len = len(numbers)
    for index in range(0, total_len):
        print(index, total_len, numbers[total_len-1], numbers[index], last_element)
        if (numbers[total_len-1] > numbers[index]) & (numbers[total_len-1] > last_element) & \
                (numbers[index] > last_element):
            # print('in if')
            last_element = numbers[total_len-1]
            return_value = True
        else:
            # print('in else')
            return_value = False
            return return_value

        total_len = total_len - 1
        # print(total_len, last_element)
        if total_len <= (len(numbers)/2):
            return return_value

    return return_value


if __name__ == '__main__':
    numbers = [-91, -84, -67, -44, 9, 70, 88, 37, -11, -67, -72, -87]

    # [
    # [1, 3, 5, 6, 4, 2] -> [1, 2, 3, 4, 5, 6]
    # [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48] -> [-92, -48, -23, -17, 0, 41,,45, 89, 89, 96, 95, 99]
    # [-91, -84, -67, -44, 9, 70, 88, 37, -11, -67, -72, -87] -> []
    return_output = solution(numbers)
    print(return_output)