'''
A circus is designing a tower routine consisting of people standing atop one another’s shoulders. For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her. Given the heights and weights of each person in the circus, write a method to compute the largest possible number of people in such a tower.
EXAMPLE:
Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
Output: The longest tower is length 6 and includes from top to bottom: (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)
'''

from functools import cmp_to_key
def sort_desc(a, b):
    '''a[0] = int(a[0])
    a[1] = int(a[1])
    b[0] = int(b[0])
    b[1] = int(b[1])
    '''
    if a[0] > b[0]:
        return -1
    elif a[0] < b[0]:
        return 1
    else:
        if a[1] >= b[1]:
            return -1
        else:
            return 1

def sort_asc(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    else:
        if a[1] >= b[1]:
            return 1
        else:
            return -1

from _collections import deque
def get_max_height(all_people):
    print(all_people)
    sorted_array = sorted(all_people, key=cmp_to_key(sort_asc) )
    print(sorted_array)
    sorted_array_desc = sorted(all_people, key=cmp_to_key(sort_desc))
    print(sorted_array_desc)

    max_sequence = 0
    count = 0
    index = 0
    unfit_sequence = deque()
    while index < len(sorted_array):
        #print(index, count)
        if index == len(sorted_array) - 1:
            count += 1
            if max_sequence < count:
                max_sequence = count
            index += 1
            break

        if sorted_array[index][0] <= sorted_array[index+1][0]:
            if sorted_array[index][1] > sorted_array[index + 1][1]:
                index += 1
                continue

        count += 1
        if max_sequence < count:
            max_sequence = count
        index += 1

    print(index, count)
    return max_sequence


if __name__ == '__main__':

    all_people = []
    people = int(input("Enter no of people: "))
    for row_num in range(people):
        people_rec = list( map(int, input().strip().split()) )  #"Enter Height and Weight: " + str(row_num) + ": "
        all_people.append(people_rec)

    #65, 100:70, 150:56, 90:75, 80: 70, 82: 62, 100
    #all_people = list( map(str, input("Enter Height and Weight: ").strip().split(":")) )
    #print(all_people)
    #all_people = list( map(int, list(map(str, input("Enter Height and Weight: ").strip().split(":"))).split(",") ) )
    #print(all_people)

    print( get_max_height(all_people) )