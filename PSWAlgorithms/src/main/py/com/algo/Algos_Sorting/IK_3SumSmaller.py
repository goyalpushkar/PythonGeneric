'''
Given a list of numbers, count the number of triplets having a sum less than a given target.

Example One
{
"target": 4,
"numbers": [5, 0, -1, 3, 2]
}
Output:

2
{numbers[1], numbers[2], numbers[3]} and {numbers[1], numbers[2], numbers[4]} are the triplets having sum
less than 4.

Example Two
{
"target": 7,
"numbers": [2, 2, 2, 1]
}
Output:

4
{numbers[0], numbers[1], numbers[2]}, {numbers[0], numbers[1], numbers[3]}, {numbers[0], numbers[2], numbers[3]}
and {numbers[1], numbers[2], numbers[3]} are the triplets having sum less than 7.

Notes
The original array's indexes identify a triplet. Therefore, any two triplets will differ if they are denoted by a
different triplet of indexes, even if the values present at those indexes are the same. Please observe Example
Two for more details on this.

Constraints:
3 <= size of the input list <= 103
-10^5 <= any element of the input list <= 10^5
-10^9 <= target number <= 10^9
'''
class Solution:
    def count_triplets(target, numbers):

        count = 0
        numbers.sort()
        for index_1 in range(len(numbers)):
            first = numbers[index_1]

            left = index_1 + 1
            right = len(numbers)-1

            while left < right:
                if sum([first, numbers[left], numbers[right]]) < target:
                    count += (right-left)
                    left += 1
                else:
                    right -= 1

        return count

    # def count_triplets(target, numbers):
    #     """
    #     Args:
    #      target(int32)
    #      numbers(list_int32)
    #     Returns:
    #      int32
    #     """
    #     # Write your code here.
    #     final_list = set()
    #     for index_1 in range(len(numbers)):
    #         new_target = target - numbers[index_1]
    #         target_dict = {}
    #
    #         left = 0
    #         right = len(numbers) - 1
    #         while left <= right:
    #             if left == index_1:
    #                 left += 1
    #
    #             if right == index_1:
    #                 right -= 1
    #
    #             if numbers[left] + numbers[right] < new_target:
    #                 final_list.add(",".join(str(val) for val in sorted([index_1, left, right])))
    #                 # final_list.add(",".join(str(val) for val in [index_1, left, right]))
    #
    #             left += 1
    #             right -= 1
    #
    #         print(final_list)
    #         # print(index_1, new_target)
    #         # for index_2 in range(len(numbers)):
    #         #     print(index_2, target_dict)
    #         #     if index_1 != index_2:
    #         #         if new_target - numbers[index_2] in target_dict:
    #         #             print(sorted([index_1, index_2, target_dict[new_target - numbers[index_2]]]))
    #         #             final_list.add(",".join(str(val) for val in sorted([index_1, index_2, target_dict[new_target - numbers[index_2]]])))
    #
    #         #         target_dict[numbers[index_2]] = index_2
    #
    #     return len(final_list)
