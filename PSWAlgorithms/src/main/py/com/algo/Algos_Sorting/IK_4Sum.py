'''
Given a list of numbers, find all the unique quadruples that sum up to a given target value.

Example
{
"arr": [0, 0, 1, 3, 2, -1],
"target": 3
}
Output:

[
[-1, 0, 1, 3],
[0, 0, 1, 2]
]
Notes
Two quadruples are considered different if there exists a number whose frequencies differ in those two quadruples.
The quadruples can be returned in any order.
The order of numbers inside any quadruple does not matter.

Constraints:
1 <= size of the input list <= 300
-105 <= any element of the input list <= 105
-4 * 105 <= target value <= 4 * 105

https://uplevel.interviewkickstart.com/resource/rc-codingproblem-470031-900132-1127-6931
'''
class Solution:

    def four_sum(arr, target):
        """
        Args:
         arr(list_int32)
         target(int32)
        Returns:
         list_list_int32
        """

        # Write your code here.
        def get_2Sum(arr, target, start, end, curr_val, final_val):
            # print(curr_val)
            while start < end:
                if target - arr[start] == arr[end]:
                    final_val.append(curr_val + [arr[start], arr[end]])
                    start += 1
                    end -= 1

                    while start < end and arr[start] == arr[start - 1]:
                        start += 1

                elif target - arr[start] < arr[end]:
                    end -= 1
                else:
                    start += 1

        def get_3sum(arr, target, start, end, curr_val, final_val):
            for j in range(start, end + 1):
                if j > start and arr[j] == arr[j - 1]:
                    continue

                new_target = target - arr[j]
                # curr_val.append(arr[j])

                get_2Sum(arr, new_target, j + 1, end, curr_val + [arr[j]], final_val)

        arr = sorted(arr)
        final_val = []
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            new_target = target - arr[i]

            get_3sum(arr, new_target, i + 1, len(arr) - 1, [arr[i]], final_val)

        # print(map(tuple, final_val))
        # final_val = list(set(map(tuple, final_val)))
        return final_val

    def four_sum_dupissue(arr, target):
        """
        Args:
         arr(list_int32)
         target(int32)
        Returns:
         list_list_int32
        """

        def get_2Sum(arr, target, start, end, res):
            two_sums = []
            while start < end:
                if target - arr[start] == arr[end]:
                    res.append([arr[start], arr[end]])
                    start += 1
                    end -= 1

                    while start < end and arr[start] == arr[start-1]:
                        start += 1

                elif target - arr[start] < arr[end]:
                    end -= 1
                else:
                    start += 1

        def get_3sum(arr, target, start, end, res):
            for j in range(start, end):
                if j > start + 1 and arr[j] == arr[j - 1]:
                    continue
                new_target = target - arr[j]
                get_2Sum(arr, new_target, j + 1, end, res.append(arr[j]))

        arr = sorted(arr)
        final_val = []
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue

            get_3sum(arr, target, i+1, len(arr), final_val.append(arr[i]))

        # print(map(tuple, final_val))
        # final_val = list(set(map(tuple, final_val)))
        return final_val

    def four_sum_timeissue(arr, target):
        """
        Args:
         arr(list_int32)
         target(int32)
        Returns:
         list_list_int32
        """
        all_comb = set()
        for i in range(len(arr)):
            first = target - arr[i]

            for j in range(len(arr)):
                if j != i:
                    second = first - arr[j]
                    check_arr = {}

                    for k in range(len(arr)):
                        if k != j and k != i:
                            third = second - arr[k]
                            if third in check_arr:
                                all_comb.add(",".join(str(val) for val in sorted([arr[i], arr[j], third, arr[k]])))
                                # all_comb.append([arr[i], arr[j], third, arr[k]])
                            check_arr[arr[k]] = k

        # print(all_comb)
        final_list = [list(map(int, elem.split(","))) for elem in all_comb]
        return final_list



