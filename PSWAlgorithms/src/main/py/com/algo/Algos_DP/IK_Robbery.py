'''
There are n houses built in a line, each of which contains some value in it. A thief is going to steal the maximal
value in these houses, but he cannot steal in two adjacent houses because the owner of a stolen house will tell his
two neighbours on the left and right side. What is the maximal stolen value?

For example, if there are four houses with values [6, 1, 2, 7], the maximal stolen value is 13, when the first and
fourth houses are stolen.

Example
{
"values": [6, 1, 2, 7]
}
Output:
13
Steal from the first and the last house.

Notes
Constraints:
1 <= n <= 105
1 <= values[i] <= 104, for all i.
'''
def maximum_stolen_value(values):
    """
    Args:
     values(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    # if len(values) == 1:
    #     return values[0]
    # elif len(values) == 2:
    #     return max(values[0], values[1])
    max1 = 0 # values[0]
    max2 = 0 # values[1]
    for i in range(len(values)):
        temp_max = max(values[i] + max1, max1)
        max1 = max(max1, max2)
        max2 = temp_max
        # print(i, max1, max2, temp_max)

    return max(max1, max2)

def maximum_stolen_value(values):
    """
    Args:
     values(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    if len(values) == 1:
        return values[0]
    elif len(values) == 2:
        return max(values[0], values[1])
    max_values = [0 for _ in range(len(values))]
    for i in range(len(values)):
        max_values[i] = max(values[i] + max_values[i-2], max_values[i-1])

    return max_values[-1]
