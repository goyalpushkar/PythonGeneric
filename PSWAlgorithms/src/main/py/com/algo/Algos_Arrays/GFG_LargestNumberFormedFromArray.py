'''
Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.The result is going to be very large, hence return the result in the form of a string.

Input:
The first line of input consists number of the test cases. The description of T test cases is as follows:
The first line of each test case contains the size of the array, and the second line has the elements of the array.

Output:
In each separate line print the largest number formed by arranging the elements of the array in the form of a string.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 102
0 ≤ A[i] ≤ 103

Example:
Input:
2
5
3 30 34 5 9
4
54 546 548 60

Output:
9534330
6054854654
'''

def comparator(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return ((int(ba) > int(ab)) - (int(ba) < int(ab)))  #Largest Number
    #return ((int(ab) > int(ba)) - (int(ab) < int(ba)))  #Smallest Number

def myCompare(mycmp):

    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K

def largest_number_usin_comparator(array_size, arr):

    sorted_arr = sorted(arr, key=myCompare(comparator))

    return "".join(str(i) for i in sorted_arr)



def largest_number(array_size, arr):

    '''

    :param array_size:
    :param arr:
    :return:
    max_size = 0
    for elem in arr:
        if max_size < len(str(elem)):
            max_size = len(str(elem))
    '''

    max_size = len(str(max(arr)))
    dict_elem = [] #{} cannot be taken as keys can repeat once Zeros are appended to the element
    for index in range(len(arr)):
        #dict_elem.append( (int(str(arr[index]).ljust(max_size, '0')), arr[index]) )
        new_elem = str(arr[index]) * max_size
        dict_elem.append((new_elem[:max_size:], arr[index]))

    max_string = ""
    for elems in sorted(dict_elem, reverse=True):

        #if prev_key == keys:
        #    if dict_elem[keys] < dict_elem[prev_key]:

        #prev_key = keys
        max_string += str(elems[1])

    return max_string

from functools import cmp_to_key

def largest_number_usin_std_comparator(array_size, arr):

    sorted_arr = sorted(arr, key=cmp_to_key(comparator))
    return "".join(str(i) for i in sorted_arr)


if __name__ == '__main__':
    test_cases = int(input("No of test cases: "))
    for elem in range(test_cases):
        array_size = int(input("Array Size: "))
        arr = list(map(int, input("Array Elem: ").strip().split()))

        res = largest_number_usin_comparator(array_size, arr)
        print(res)

        res = largest_number(array_size, arr)
        print(res)

        res=largest_number_usin_std_comparator(array_size, arr)
        print(res)