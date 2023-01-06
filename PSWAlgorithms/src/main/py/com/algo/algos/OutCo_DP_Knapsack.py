'''
Given a set of items where each item has a weight and a value. And given a knapsack with max weight capacity, determine the maximum value that can be placed into the knapsack without going over the capacity.

Input: An integer array of weights
       An integer array of values
           (The ith item has weights[i] and values[i])
       Integer value of the max weight capacity of the knapsack
Output: Integer of maximum total value
'''

# DP
'''
    weights = [10,20,30]
    values = [60, 100, 120]
    allowed_cap = 50
    
                0 1 ..... 9   10   11 ..... 19   20   21   22 ..... 29   30   31   32 ..... 39   40   41   42 ..... 49   50 
     {0}        0 0       0    0    0        0    0    0    0        0    0    0    0        0    0    0    0        0    0
     {10}       0 0       0   60   60       60   60   60   60       60   60   60   60       60   60   60   60       60   60 
   {10, 20}     0 0       0   60   60       60  100  100  100      100  160  160  160      160  160  160  160      160  160
 {10, 20, 30}   0 0       0   60   60       60  100  100  100      100  160  160  160      160  160  160  160      160  220
 
 opt(i, w) =  0                 if i=0
              opt(i-1, w)       if wi > w
              max(opt(i-1, w), vi + opt(i-1, w-wi))
'''

def knapsack(weights, values, capacity):

    max_val = [[0 for _ in range(0, capacity+1, 1)]for _ in range(len(weights)+1)]

    for i in range(0, capacity+1, 1):
        max_val[0][i] = 0

    for row in range(1, len(weights)+1):
        for col in range(1, capacity+1, 1):
            if weights[row-1] > col:
                max_val[row][col] = max_val[row-1][col]
            else:
                max_val[row][col] = max(max_val[row-1][col], values[row-1]+max_val[row-1][col-weights[row-1]])

    return max_val[len(weights)][capacity]

# recursive approach
def knapsack_rec(weights, values, capacity):

    len_elems = len(weights)

    def helper(cap, val, height, final_cap, final_val):
        print(f"{'-'*height}cap: {cap}\tval: {val}\theight: {height}\n"
              f"final_cap: {final_cap}\tfinal_val:{final_val}"
              f"\n")
        if height == len_elems:
            return cap, val

        # right
        final_cap_left, final_val_left = helper(cap, val, height+1, final_cap, final_val)

        # left
        final_cap_right, final_val_right = helper(cap-weights[height], val+values[height], height + 1, final_cap, final_val)

        print(f"{'-'*height}final_cap_left: {final_cap_left}\t{final_val_left}\n"
              f"{'-'*height}final_cap_right: {final_cap_right}\t{final_val_right}\n")
        if final_cap_left >=0 and final_cap_left <= capacity and final_cap_right >= 0 and final_cap_right <= capacity:
            return final_cap_right if final_val_right > final_val_left else final_cap_left, max(final_val_right, final_val_left)
        elif final_cap_left >=0 and final_cap_left <= capacity:
            return final_cap_left, final_val_left
        elif final_cap_right >=0 and final_cap_right <= capacity:
            return final_cap_right, final_val_right
        else:
            return final_cap, final_val

    final_cap, final_val = helper(capacity, 0, 0, 0, 0)

    return final_val


if __name__ == '__main__':
    no_of_tests = int(input("No of tests: "))
    # for i in range(no_of_tests):
    #     no_of_items = int(input("Enter No of items: "))
    #     weights = []
    #     values = []
    #     for i in range(no_of_items):
    #         weights.append(int(input(f"Enter weight for item {i+1}: ")))
    #         values.append(int(input(f"Enter value for item {i+1}: ")))
    #
    #     allowed_cap = int(input("Enter capactity: "))
    weights = [10,20,30]
    values = [60, 100, 120]
    allowed_cap = 50
    result = knapsack(weights, values, allowed_cap)
    # longest_palindrome(input_string)
    print(f"result: {result}")