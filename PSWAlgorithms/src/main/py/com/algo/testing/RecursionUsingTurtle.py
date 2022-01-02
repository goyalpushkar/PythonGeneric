'''
Created on Feb 1, 2020

@author: goyalpushkar
'''

if __name__ == '__main__':
    pass

import turtle
from turtle import *
import random

my_turtle = turtle.Turtle()  #shape=arrow, turtle, circle, square, triangle, classic, blank
my_win = turtle.Screen()

MAZE_PATH = '/Users/goyalpushkar/Library/Mobile Documents/com~apple~CloudDocs/Documents/STSworkspace/WarehouseConnect/'
PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze():
    def __init__(self, maze_file_name):
        self.rows_in_maze = 0
        self.columns_in_maze = 0
        self.maze_list = []
        maze_file = open(maze_file_name,'r') 
        
        rows_in_maze = 0
        for line in maze_file: 
            print( "Line - " + line )
            row_list = []
            col = 0
            for ch in line[: -1]:
                print( "Letter - " + ch )
                row_list.append(ch) 
                if ch == 'S':
                    self.start_row = rows_in_maze
                    self.start_col = col 
                col = col + 1
                
            rows_in_maze = rows_in_maze + 1 
            self.maze_list.append(row_list) 
            columns_in_maze = len(row_list)
        
        self.rows_in_maze = rows_in_maze 
        self.columns_in_maze = columns_in_maze 
        self.x_translate = - columns_in_maze / 2 
        self.y_translate = rows_in_maze / 2
         
        print( "Rows - " + str(self.rows_in_maze) + " :Cols - " + str(self.columns_in_maze) ) 
        print( "X Translate - " + str(self.x_translate) + " :Y Translate - " + str(self.y_translate) ) 
        self.t = turtle.Turtle() 
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates( - (columns_in_maze - 1) / 2 - .5,  # -10.5
                                     - (rows_in_maze - 1) / 2 - .5,     # -5.5
                                       (columns_in_maze - 1) / 2 + .5,  # 10.5
                                       (rows_in_maze - 1) / 2 + .5 )    # 5.5
    
    def draw_maze(self): 
        self.t.speed(10)
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate,
                                         - y + self.y_translate,
                                         'orange') 
        
        self.t.color('black')
        self.t.fillcolor('blue')
    
    def draw_centered_box(self, x, y, color): 
        self.t.up()
        self.t.goto(x - .5, y - .5) 
        self.t.color(color) 
        self.t.fillcolor(color) 
        self.t.setheading(90) 
        self.t.down() 
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90) 
            self.t.end_fill()
    
    def move_turtle(self, x, y): 
        self.t.up()
        self.t.setheading( self.t.towards(x + self.x_translate, - y + self.y_translate) )
        self.t.goto(x + self.x_translate, - y + self.y_translate)
    
    def drop_bread_crumb(self, color): 
        self.t.dot(10, color)

    def update_position(self, row, col, val=None): 
        if val:
            self.maze_list[row][col] = val 
        self.move_turtle(col, row)
        
        if val == PART_OF_PATH: 
            color = 'green'
        elif val == OBSTACLE: 
            color = 'red'
        elif val == TRIED: 
            color = 'black'
        elif val == DEAD_END: 
            color = 'red'
        else:
            color = None
            
        if color: 
            self.drop_bread_crumb(color)
            
    def is_exit(self, row, col): 
        return (row == 0 or
                row == self.rows_in_maze - 1 or 
                col == 0 or
                col == self.columns_in_maze - 1)
        
    def __getitem__(self,idx): 
        return self.maze_list[idx]
    
def search_maze(maze, start_row, start_column):
    # try each of four directions from this point until we find a way out.
    # base Case return values:
    # 1. We have run into an obstacle, return false 
    maze.update_position(start_row, start_column) 
    if maze[start_row][start_column] == OBSTACLE :
        return False
    # 2. We have found a square that has already been explored 
    if maze[start_row][start_column] == TRIED or maze[start_row][start_column] == DEAD_END: 
        return False
    # 3. We have found an outside edge not occupied by an obstacle
    if maze.is_exit(start_row,start_column): 
        maze.update_position(start_row, start_column, PART_OF_PATH) 
        return True
    
    maze.update_position(start_row, start_column, TRIED)
    # Otherwise, use logical short circuiting to try each direction # in turn (if needed)
    found = search_maze(maze, start_row-1, start_column) or \
            search_maze(maze, start_row+1, start_column) or \
            search_maze(maze, start_row, start_column+1) or \
            search_maze(maze, start_row, start_column-1)
            
    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
        
    return found

def draw_maze(filename):
    my_maze = Maze( MAZE_PATH + filename)
    my_maze.draw_maze()
    my_maze.update_position(my_maze.start_row, my_maze.start_col)

    search_maze(my_maze, my_maze.start_row, my_maze.start_col)

########################
####### Spiral #########
########################
def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)
        
########################
######### Sun ##########
########################        
def draw_sun(my_turtle):
    my_turtle.color("red","yellow")
    my_turtle.begin_fill()
    while True:
        my_turtle.forward(200)
        my_turtle.left(170)
        if abs(my_turtle.pos()) < 1:
            break
    my_turtle.end_fill()
    #done()  #It stops the screen from getting closed 
       
########################
######### Tree #########
########################         
def draw_tree_worec(my_turtle, branch_len):    
        my_turtle.forward(branch_len)
        my_turtle.right(60)
        #my_turtle.forward(branch_len)
        #draw_tree(my_turtle, branch_len - 15 )
        my_turtle.left(120)
        #my_turtle.forward(branch_len)
        #draw_tree(my_turtle, branch_len - 15 )
        my_turtle.right(60)
        #my_turtle.forward(branch_len)
        my_turtle.backward(branch_len)   
#draw_spiral(my_turtle, 100)
#draw_sun(my_turtle)

def draw_tree_practice(my_turtle, branch_len):
    if branch_len > 5:
        my_turtle.forward(branch_len)
        my_turtle.right(20)
        #my_turtle.width()
        draw_tree_practice(my_turtle, branch_len - 15 )
        my_turtle.left(20)
        #draw_tree(my_turtle, branch_len - 15 )
        #my_turtle.right(20)
        my_turtle.backward(branch_len)
    
def draw_tree_practice_worec(my_turtle, branch_len):
    if branch_len > 5:
        my_turtle.forward(branch_len)
        my_turtle.right(20)
        #my_turtle.width()
        #draw_tree(my_turtle, branch_len - 15 )
        my_turtle.left(20)
        #draw_tree(my_turtle, branch_len - 15 )
        #my_turtle.right(20)
        my_turtle.backward(branch_len)
            
dictColor = {2:'brown',4:'yellow',6:'orange',8:'red',10:'green',12:'black'}
def draw_tree(my_turtle, branch_len, pensize, angle):
    #pensize = 2
    if branch_len > 5:
        #my_turtle.width(-1)
        if pensize < 0:
            pensize = 2
          
        #Set Pensize and color
        print( str(branch_len) + " " + str(pensize) + " " +str(angle)  )
        my_turtle.pensize(pensize)
        my_turtle.color( dictColor.get(pensize,'blue') )
        my_turtle.forward(branch_len)
        
        #angle = random.randrange(0,45)
        my_turtle.right(angle)
        draw_tree( my_turtle, ( branch_len - random.randrange(1,16) ), pensize-2, random.randrange(0,45) ) #random.randrange(0,45)
        
        my_turtle.left(2 * angle)
        #if branch_len <= 60:
        draw_tree( my_turtle, ( branch_len - random.randrange(1,16)  ), pensize-2, random.randrange(0,45) ) #random.randrange(0,45)
        my_turtle.right(angle)
        
        #Reset Pensize and color
        my_turtle.pensize(pensize)
        my_turtle.color( dictColor.get(pensize,'blue') )
        my_turtle.backward(branch_len)
         
########################
####### Triangle #######
########################              
#my_points = [[-100, -50], [0, 100], [100, -50]]
def draw_triangle(pointA, pointB, pointC, color, my_turtle):
    '''
    print( 'color - ' + color)
    print('Point A - ' + str(pointA[0]) + "," + str(pointA[1]) )
    print('Point B - ' + str(pointB[0]) + "," + str(pointB[1]) )
    print('Point C - ' + str(pointC[0]) + "," + str(pointC[1]) )
    '''
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(pointA[0], pointA[1]) 
    my_turtle.down()
    my_turtle.begin_fill() 
    my_turtle.goto(pointB[0], pointB[1]) 
    my_turtle.goto(pointC[0], pointC[1]) 
    my_turtle.goto(pointA[0], pointA[1]) 
    my_turtle.end_fill()
    
def midpoint( pointA, pointB ):
    return ( ( pointA[0] + pointB[0] ) / 2, ( pointA[1] + pointB[1] ) / 2 )

def sierpinski(points, triangleNum, my_turtle):
    colorList = ('red','yellow','brown','green','orange','blue','white','black')
    
    if triangleNum > len(colorList):
        colorA = 'violet'
    else:
        colorA = colorList[triangleNum]
     
    draw_triangle(points[0], points[1], points[2], colorA, my_turtle)
    if triangleNum > 0:
        '''
        newPoints = list()
        newPoints.append( midpoint(points[0], points[1])  )
        newPoints.append( midpoint(points[1], points[2]) )
        newPoints.append( midpoint(points[2], points[0]) )
        sierpinski(newPoints, triangleNum-1, my_turtle)
        '''
        newPoints = list()
        newPoints.append( points[0] )
        newPoints.append( midpoint(points[0], points[1]) )
        newPoints.append( midpoint(points[0], points[2]) )
        sierpinski(newPoints, triangleNum-1, my_turtle)
        
        newPoints = list()
        newPoints.append( points[1] )
        newPoints.append( midpoint(points[1], points[0]) ) ##10
        newPoints.append( midpoint(points[1], points[2]) )
        sierpinski(newPoints, triangleNum-1, my_turtle)
        
        newPoints = list()
        newPoints.append( points[2] )
        newPoints.append( midpoint(points[2], points[1]) )
        newPoints.append( midpoint(points[2], points[0]) )
        sierpinski(newPoints, triangleNum-1, my_turtle)


########################
#### Hanooi Tower ######
########################  
def move_disk(fromPole, toPole):
    print("Disk Moved from ", fromPole, ' to ' , toPole )

def hanoii_towers(height, from_pole, intermediate_pole, to_pole):
    if height >= 1:
        hanoii_towers(height-1, from_pole, to_pole, intermediate_pole)
        move_disk(from_pole, to_pole)
        hanoii_towers(height-1, intermediate_pole, from_pole, to_pole )
        
          
def draw_function(functionNumber):
    if functionNumber in ( 1, 2, 3, 4):
        my_turtle.left(90)  
        my_turtle.up()
        my_turtle.backward(70)
        my_turtle.down()
    
    if functionNumber == 1:
        #Draw Spiral
        spiralLength = raw_input("Enter Length for Spiral: ")
        draw_spiral(my_turtle, int(spiralLength) )
    if functionNumber == 2:
        #Draw Sun
        draw_sun(my_turtle)
    if functionNumber == 3:
        #Draw Tree
        treeHeight = raw_input("Enter Tree Height: ")
        penSize = raw_input("Enter Max Pen Size for Branches: ")
        draw_tree(my_turtle, int(treeHeight), int(penSize), random.randrange(0,45)) #
        #draw_tree_worec(my_turtle, 75)
        #draw_tree_practice(my_turtle, 75)
        #draw_tree_practice_worec(my_turtle, 75)
    #my_turtle.done()
    if functionNumber == 4:
        #Draw Spiral
        coordinates = list()
        pointA = raw_input("Enter comma separated Coordinates for Point A: ")
        pointAL = [ int( pointA.split(",")[0].strip() ), int( pointA.split(",")[1].strip() ) ]
        pointB = raw_input("Enter comma separated Coordinates for Point B: ")
        pointBL = [ int( pointB.split(",")[0].strip() ), int( pointB.split(",")[1].strip() ) ]
        pointC = raw_input("Enter comma separated Coordinates for Point C: ")
        pointCL = [ int( pointC.split(",")[0].strip() ), int( pointC.split(",")[1].strip() ) ]
        triangleNum = raw_input("Enter Number of Triangles to be created: ")
        coordinates.append(pointAL)
        coordinates.append(pointBL)
        coordinates.append(pointCL)
        #draw_triangle(pointAL, pointBL, pointCL, 'red', my_turtle)
        sierpinski(coordinates, int(triangleNum), my_turtle)
    
    if functionNumber == 5:
        numOfDisks = raw_input("Enter number of disks in Hanoi Tower: ")
        hanoii_towers( int(numOfDisks), "A", "B", "C") #1, 2, 3)
     
    if functionNumber == 6:   
        
        draw_maze('maze2.txt')
    
    my_win.exitonclick()
    
def main():
    '''
    my_turtle.left(90)  
    my_turtle.up()
    my_turtle.backward(70)
    my_turtle.down()
  
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.up()
    '''
    #my_turtle.color('green')
    
    print("Run one of the following functions: ")
    print( "\t 1. DRAW_SPIRAL" )
    print( "\t 2. DRAW_SUN" )
    print( "\t 3. DRAW_TREE" )
    print( "\t 4. DRAW_SEIRPINSKI" )
    print( "\t 5. DRAW_HANOII_TOWERS" )
    print( "\t 6. DRAW_MAZE" )
    usrInput = raw_input("Enter Number for below programs or q to quit: ")
    while usrInput.upper() != 'Q':
        draw_function( int(usrInput) )
        print("Run one of the following functions: ")
        print( "\t 1. DRAW_SPIRAL" )
        print( "\t 2. DRAW_SUN" )
        print( "\t 3. DRAW_TREE" )
        print( "\t 4. DRAW_SEIRPINSKI" )
        print( "\t 5. DRAW_HANOII_TOWERS" )
        print( "\t 6. DRAW_MAZE" )
        usrInput = raw_input("Enter Number for below programs or q to quit: ")
   

main()