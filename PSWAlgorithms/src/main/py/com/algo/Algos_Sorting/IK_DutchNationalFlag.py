'''
Given some balls of three colors arranged in a line, rearrange them such that all the red balls go first,
then green and then blue ones.

Do rearrange the balls in place. A solution that simply counts colors and overwrites the array is not the one we are
looking for.

This is an important problem in search algorithms theory proposed by Dutch computer scientist Edsger Dijkstra.
Dutch national flag has three colors (albeit different from ones used in this problem).

Example
{
"balls": ["G", "B", "G", "G", "R", "B", "R", "G"]
}
Output:

["R", "R", "G", "G", "G", "G", "B", "B"]
There are a total of 2 red, 4 green and 2 blue balls. In this order they appear in the correct output.

Notes
Constraints:
1 <= n <= 100000
Do this in ONE pass over the array, NOT TWO passes
Solution is only allowed to use constant extra memory

'''
class Solution:

    def dutch_flag_sort(balls):
        """
        Args:
         balls(list_char)
        Returns:
         list_char
        """
        # Write your code here.
        # color_dict = {'R': 0, 'G': 1, 'B': 2}

        # middle_val = 0 + (0-len(balls)-1) // 2

        low = 0
        traverse = 0
        high = len(balls) - 1

        while traverse <= high:
            if balls[traverse] == 'R':    # color_dict[balls[traverse]] < 1:  # color_dict[balls[traversedle_val]]:
                balls[low], balls[traverse] = balls[traverse], balls[low]
                low += 1
                traverse += 1
            elif balls[traverse] == 'B':   # color_dict[balls[traverse]] > 1:  # color_dict[balls[traversedle_val]]:
                balls[traverse], balls[high] = balls[high], balls[traverse]
                high -= 1
            else:
                traverse += 1

        return balls