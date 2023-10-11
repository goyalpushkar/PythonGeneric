'''
One pixel on a grayscale image changes color. Recolor all the adjacent pixels of the same color to the same new color.

Grayscale colors are simply numbers.

Example One
{
"pixel_row": 0,
"pixel_column": 1,
"new_color": 2,
"image": [
[0, 1, 3],
[1, 1, 1],
[1, 5, 4]
]
}
I.e. the pixel at row 0 and column 1 changes to color 2.

Output:

[
[0, 2, 3],
[2, 2, 2],
[2, 5, 4]
]
Example Two
{
"pixel_row": 1,
"pixel_column": 0,
"new_color": 9,
"image": [
[0, 2, 1],
[1, 1, 2],
[2, 5, 4]
]
}
I.e. the pixel at row 1 and column 0 changes to color 9.

Output:

[
[0, 2, 1],
[9, 9, 2],
[2, 5, 4]
]
Notes
Two pixels are considered adjacent if they share a side; sharing a diagonal is not enough.

Constraints:

1 <= image width <= 1000
1 <= image height <= 1000
0 <= pixel color <= 1000
'''

# first approach with visited nodes maintenance
def flood_fill(pixel_row, pixel_column, new_color, image):
    """
    Args:
     pixel_row(int32)
     pixel_column(int32)
     new_color(int32)
     image(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    
    directions = [(-1,0), (1,0), (0,-1), (0, 1)]
    already_visited = set()
    
    def traverse(row, col):
        nonlocal existing_color, new_color
        # print(f"row: {row}, col: {col}, alread_visited: {already_visited}, image: {image}, {existing_color}, {new_color}")
        if (row, col) in already_visited:
            return
        
        already_visited.add((row, col))
        
        if image[row][col] != existing_color:
            return
        else:
            image[row][col] = new_color
            
        for dir in directions:
            # print(f"new direction: {row+dir[0]}, {col+dir[1]}")
            if row+dir[0] >= 0 and row+dir[0] < len(image) and col+dir[1] >= 0 and col+dir[1] < len(image[0]):
                traverse(row+dir[0], col+dir[1])
        
        return  
        
    existing_color = image[pixel_row][pixel_column]
    # image[pixel_row][pixel_column]  = new_color
    traverse(pixel_row, pixel_column)
    
    return image


# Another approach without maintain visited nodes
# this does not work if existing color and new color are same then it will keep on going in loop
'''
{
"pixel_row": 0,
"pixel_column": 4,
"new_color": 7,
"image": [
[7, 7, 7, 7, 7, 7]
]
}
'''
def flood_fill(pixel_row, pixel_column, new_color, image):
    """
    Args:
     pixel_row(int32)
     pixel_column(int32)
     new_color(int32)
     image(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    directions = [(-1,0), (1,0), (0,-1), (0, 1)]
    already_visited = set()
    
    def traverse(row, col):
        nonlocal existing_color, new_color
        # print(f"row: {row}, col: {col}, alread_visited: {already_visited}, image: {image}, {existing_color}, {new_color}")
        # if (row, col) in already_visited:
        #     return
        
        # already_visited.add((row, col))
        
        # if image[row][col] != existing_color:
        #     return
        # else:
        image[row][col] = new_color
            
        for dir in directions:
            # print(f"new direction: {row+dir[0]}, {col+dir[1]}")
            if row+dir[0] >= 0 and row+dir[0] < len(image) and col+dir[1] >= 0 \
               and col+dir[1] < len(image[0]) and image[row+dir[0]][col+dir[1]] == existing_color:
                traverse(row+dir[0], col+dir[1])
        
        return  
        
    existing_color = image[pixel_row][pixel_column]
    # image[pixel_row][pixel_column]  = new_color
    traverse(pixel_row, pixel_column)
    
    return image