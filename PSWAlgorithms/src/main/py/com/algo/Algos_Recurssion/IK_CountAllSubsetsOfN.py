'''
Given a number denoting the size of a set, count the number of unique subsets of that set.

Example
{
"n": 3
}
Output:

8
If we have a set {1, 2, 3}, then all the possible subsets are: {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}.

Notes
Empty subset should also be counted.

Constraints:

0 <= input number <= 30.
'''

class Solution:
    def count_all_subsets(n):
        """
        Args:
         n(int32)
        Returns:
         int32
        """
        # Write your code here.

        def count_subset_helper(level, count):
            if level == n:
                count += 1
                return count

            # left
            left = count_subset_helper(level + 1, count)
            # # right
            # right = count_subset_helper(level+1, count)

            return 2 * left

        return count_subset_helper(0, 0)