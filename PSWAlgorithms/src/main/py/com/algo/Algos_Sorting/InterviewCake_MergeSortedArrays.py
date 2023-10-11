'''
In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.

For example:

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print merge_lists(my_list, alices_list)
'''

class Solution:

    def merge_sorted_array(self, list1, list2):

        s1, s2 = 0, 0
        l1 = len(list1)
        l2 = len(list2)
        new_list = []

        while s1 < l1 or s2 < l2:
            if list1[s1] < list2[s2]:
                new_list.append(list1[s1])
                s1 += 1
            else:
                new_list.append(list2[s2])
                s2 += 1

            if s1 == l1 or s2 == l2:
                break

        while s1 < l1:
            new_list.append(list1[s1])
            s1 += 1

        while s2 < l2:
            new_list.append(list2[s2])
            s2 += 1

        return new_list
