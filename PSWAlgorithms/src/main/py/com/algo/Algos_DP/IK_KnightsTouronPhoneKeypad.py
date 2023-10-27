'''
Given a phone keypad as shown below:

1 2 3
4 5 6
7 8 9
– 0 –

How many different phone numbers of given length can be formed starting from the given digit? The constraint is that the movement from one digit to the next is similar to the movement of the Knight in chess.

For example, if we are at 1, then the next digit can be either 6 or 8; if we are at 6 then the next digit can be 1, 7 or 0.

Repetition of digits is allowed, e.g. 1616161616 is a valid number.
There is no need to list all possible numbers, just find how many they are.
Find a polynomial-time solution, based on Dynamic Programming.

Example One
{
"start_digit": 1,
"phone_number_length": 2
}
Output:

2
Two possible numbers of length 2: 16, 18.

Example Two
{
"start_digit": 1,
"phone_number_length": 3
}
Output:

5
The possible numbers of length 3: 160, 161, 167, 181, 183

Notes
There are two input parameters: start_digit and phone_number_length, denoting the starting digit and the required length respectively.
Output is a long integer denoting the total number of valid phone numbers that can be formed.
Constraints:

0 <= start_digit <= 9
1 <= phone_number_length <= 30
'''

def count_phone_numbers_of_given_length(start_digit, phone_number_length):
    """
    Args:
    start_digit(int32)
    phone_number_length(int32)
    Returns:
    int64
    """
    # Write your code here.
    directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
    
    pad = {(3, 1): 0, (0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 7, (2, 1): 8, (2, 2): 9}
    reverse_pad = {0: (3, 1), 1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}
    
    track = [[0 for j in range(phone_number_length)] for i in range(10)]
    
    for i in range(10):
        track[i][0] = 1
        
    
    for col in range(1, phone_number_length):
        for row in range(10):
        
            curr_dir = reverse_pad[row]
            total_moves = 0
            for dir in directions:
                new_row = curr_dir[0] + dir[0]
                new_col = curr_dir[1] + dir[1]
                
                if (new_row >= 0 and new_row < 3 and new_col >= 0 and new_col < 3) or (new_row == 3 and new_col == 1):
                    new_val = pad[(new_row, new_col)]
                    # print(f"new_row: {new_row}, new_col: {new_col}, new_val: {new_val}")
                    total_moves += track[new_val][col-1]
            
            # print(f"total_moves: {total_moves}")
            track[row][col] = total_moves
            
    return track[start_digit][phone_number_length-1]

# def count_phone_numbers_of_given_length(start_digit, phone_number_length):
#     """
#     Args:
#     start_digit(int32)
#     phone_number_length(int32)
#     Returns:
#     int64
#     """
#     # Write your code here.
#     directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
#     reverse_pad = {0: (3, 1), 1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}
    
    
#     mem = {}
#     def dfs(row, col, level):
#         if (row, col) in mem:
#             return mem[(row, col)]
            
#         if level == phone_number_length:
#             return 1
            
#         total_moves = 0
#         for dir in directions:
#             new_row = row + dir[0]
#             new_col = col + dir[1]
                
#             if (new_row >= 0 and new_row < 3 and new_col >= 0 and new_col < 3) or (new_row == 3 and new_col == 1):
#                 total_moves += dfs(new_row, new_col, level+1)
        
#         mem[(row, col)] = total_moves  
#         return total_moves
    
#     start_row, start_col = reverse_pad[start_digit]
#     return dfs(start_row, start_col, 1)