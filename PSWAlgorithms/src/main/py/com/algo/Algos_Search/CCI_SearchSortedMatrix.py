'''
Given a matrix in which each row and each column is sorted, write a method to find an element in it.
'''

def search_element(matrix, element, rows, cols):
    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == element:
            return (row, col)
        elif element < matrix[row][col]:
            col -= 1
        elif element > matrix[row][col]:
            row += 1

    return (-1,-1)

if __name__ == '__main__':

    matrix = []
    rows = int(input("Enter no of rows: "))
    for row_num in range(rows):
        cols = list( map(int, input("Enter Row: " + str(row_num) + ": ").strip().split()) )
        matrix.append(cols)

    cols = len(matrix[0])

    noOfElem = int(input("No of elements to found: "))

    for index in range(noOfElem):
        element = int(input("Element to be found: "))
        index_at = search_element(matrix, element, rows, cols)

        print( "row: ", index_at[0], " - col: ", index_at[1], end=" ")