'''
Created on Jan 30, 2020

@author: goyalpushkar
'''

import random
from StdSuites.Table_Suite import row

if __name__ == '__main__':
    pass

class baseBox:
    def __init__(self):
        self.box = [0] * 9
        
    def __setitem__(self, index, value):
        self.box[index] = value

    def __getitem__(self, index):
        return self.box[index]
    
    def __len__(self):
        return len(self.box)
    
    def __str__(self):
        index = 0
        #for index in range( 0, len(self.box) ):
        while index < len(self.box):
            if ( index in (0, 3, 6) ):
                print("\n")
                
            print( str(self.box[index]) + "\t" + str(self.box[index+1]) + "\t" + str(self.box[index+2]))
            index = index + 3

class sudokuBox:
    
    def __init__(self):
        self.completeBox = []
        for index in range(0,9):
            box = baseBox()
            self.completeBox.append(box)
    
    def __getitem__(self, row):
        return self.completeBox[row]
    
    def adjacentRowPlaces(self, row):
        if row in (0,3,6):
            return row+1, row+2
        elif row in (1,4,7):
            return row-1, row+1
        elif row in (2,5,8):
            return row-1, row-2
        
    def adjacentColPlaces(self, col):
        if col + 3 >= 9:
            newCol= col - 6 
        else:
            newCol = col + 3
        
        if col + 6 >= 9:
            newCol1 = col - 3 
        else:
            newCol1 = col + 6 
            
        return newCol, newCol1
    
    def check_value_in_box(self, box, value):
        for col in range(0,9):
            if self.completeBox[box][col] == value:
                print( "Value already in same Box" )
                return 0

        return 1   
        
    def check_value_in_row(self, box, col, value):   #(3, 4)
        ##Value shouldnt be in same col of row adjacent boxes
        #0 -> 1, 2   1 -> 0, 2  2 -> 0, 1
        #3 -> 4, 5   4 -> 3, 5  5 -> 3, 4
        #6 -> 7, 8   7 -> 6, 8  8 -> 6, 7
        rowValues = self.adjacentRowPlaces(box)   #3 - 4, 5
        colValues = self.adjacentRowPlaces(col)   #4 - 3, 5
        for rows in rowValues:
            for cols in colValues:
                if self.completeBox[box][col] == value \
                or self.completeBox[rows][col] == value \
                or self.completeBox[rows][cols] == value:
                    print( "Value already in same Row" )
                    return 0
                
        return 1
        
        '''
        if box in (0,3,6):
            if self.completeBox[box+1][col] == value \
            or self.completeBox[box+1][colValues[0]] == value \
            or self.completeBox[box+1][colValues[1]] == value \
            or self.completeBox[box+2][col] == value \
            or self.completeBox[box+2][colValues[0]] == value \
            or self.completeBox[box+2][colValues[1]] == value:
                print( "Value already in same Row" )
                return 0
            else: 
                return 1
        elif box in (1,4,7):
            if self.completeBox[box-1][col] == value \
            or self.completeBox[box-1][colValues[0]] == value \
            or self.completeBox[box-1][colValues[1]] == value \
            or self.completeBox[box+1][col] == value \
            or self.completeBox[box+1][colValues[0]] == value \
            or self.completeBox[box+1][colValues[1]] == value:
                print( "Value already in same Row" )
                return 0
            else: 
                return 1
        elif box in (2,5,8):
            if self.completeBox[box-1][col] == value \
            or self.completeBox[box-1][colValues[0]] == value \
            or self.completeBox[box-1][colValues[1]] == value \
            or self.completeBox[box-2][col] == value \
            or self.completeBox[box-2][colValues[0]] == value \
            or self.completeBox[box-2][colValues[1]] == value:
                print( "Value already in same Row" )
                return 0
            else: 
                return 1
        else:
            return 1
        '''
        
    def check_value_in_col(self, box, col, value):
        ##Value shouldnt be in same col of column adjacent boxes ( n+3>=9 n-6 else n+3, n+6>=9 n-3 else n+6 )
        #0 -> 0+3, 0+6                        1 -> 0, 2  2 -> 0, 1
        #3 -> 3+3, 0+9>9 0+9-9                4 -> 3, 5  5 -> 3, 4
        #6 -> 6+3>=9, 6+3-9, 6+6>=9 6+6-9     7 -> 6, 8  8 -> 6, 7
        rowValues = self.adjacentColPlaces(box)  #4 - 1, 7
        colValues = self.adjacentColPlaces(col)  #4 - 1, 7
        for rows in rowValues:
            for cols in colValues:
                if self.completeBox[box][cols] == value \
                or self.completeBox[rows][col] == value \
                or self.completeBox[rows][cols] == value:
                    print( "Value already in same Column" )
                    return 0
        
        return 1 
        '''
        if box + 3 >= 9:
            newRow = box - 6 
        else:
            newRow = box + 3
        
        if self.completeBox[newRow][col] == value:
            print("Value already in same Column")
            return 0
        
        if box + 6 >= 9:
            newRow = box - 3 
        else:
            newRow = box + 6   

        if self.completeBox[newRow][col] == value:
            print("Value already in same Column")
            return 0
        
        return 1        
        '''
                        
    def put_value(self, row, col, value):
        
        rowVerification = self.check_value_in_row(row, col, value)
        colVerification = self.check_value_in_col(row, col, value)
        boxVerification = self.check_value_in_box(row, value)
        if rowVerification == 1 and colVerification == 1 and boxVerification == 1:
            self.completeBox[row][col] = value  
            return 1
        else:
            return 0      
        
    def get_value(self, row, col):
        return self.completeBox[row][col]
        
    def __str__(self):
        index = 0
        while index < len(self.completeBox):
        #for index in range( 0, len(self.completeBox) ):
            if ( index in (0, 3, 6) ):
                print("\n")
             
            #for index in range( 0, len(self.box) ):
            #self.completeBox[index].__str__()  
            #print( "\t" )
            #self.completeBox[index+1].__str__() 
            #print( "\t" )
            #self.completeBox[index+2].__str__() 
            indexJ = 0
            while indexJ < len(self.completeBox[index]):
                if ( index in (0, 3, 6) ):
                    print("\n")
                    
                print( str(self.completeBox[index][indexJ]) + "\t" + str(self.completeBox[index][indexJ+1]) + "\t" + str(self.completeBox[index][indexJ+2]) + "\t\t"
                     + str(self.completeBox[index+1][indexJ]) + "\t" + str(self.completeBox[index+1][indexJ+1]) + "\t" + str(self.completeBox[index+1][indexJ+2]) + "\t\t"
                     + str(self.completeBox[index+2][indexJ]) + "\t" + str(self.completeBox[index+2][indexJ+1]) + "\t" + str(self.completeBox[index+2][indexJ+2])  
                       )
                indexJ = indexJ + 3
            
            index = index + 3

def createPuzzle( fillValues ):
    newBox = sudokuBox()
    
       
    #for row in range(0, 9):
    #    for col in range(0, 9):
    #for index in range(1, fillValues):
    index = 0
    while index < fillValues:
        randomRow = random.randrange(0,9)
        randomCol = random.randrange(0,9)
        value = random.randrange(1, 10)
        if newBox.put_value(randomRow, randomCol, value) == 1:
            index = index + 1
        #newBox[randomRow][randomCol] = value
    
    return newBox

def solveSudoku():
    #newBox = sudokuBox()
    
    box = baseBox()
    box.__str__()
    
    #create Sudoku Puzzle
    puzzle = createPuzzle(17)
    puzzle.__str__()
    
solveSudoku()