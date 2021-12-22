'''
Created on Feb 11, 2020

@author: goyalpushkar
'''

from matplotlib import pyplot
import turtle
from turtle import *

my_turtle = turtle.Turtle()  #shape=arrow, turtle, circle, square, triangle, classic, blank
my_win = turtle.Screen()

class BinaryTree:
    '''
    classdocs
    '''


    def __init__(self, value):
        '''
        Constructor
        '''
        self.key = value
        self.left_child = None
        self.right_child = None
        
    def insert_left_child(self, new_node):
        newNode = BinaryTree(new_node)
        if self.left_child == None:
            self.left_child = newNode
        else:
            newNode.left_child = self.left_child
            self.left_child = newNode
            
    def insert_right_child(self, new_node):
        newNode = BinaryTree(new_node)
        if self.right_child == None:
            self.right_child = newNode
        else:
            newNode.right_child = self.right_child
            self.right_child = newNode
                
    def get_root_val(self):
        return self.key
    
    def set_root_val(self, value):
        self.key = value    
        
    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child
    

def main_testing():    
    r = BinaryTree('a') 
    print(r.get_root_val()) 
    print(r.get_left_child()) 
    r.insert_left_child('b') 
    print(r.get_left_child()) 
    print(r.get_left_child().get_root_val()) 
    r.insert_right_child('c') 
    print(r.get_right_child()) 
    print(r.get_right_child().get_root_val()) 
    r.get_right_child().set_root_val('hello') 
    print(r.get_right_child().get_root_val())


def self_check():
    print("No assignment")
    build_tree()
    
def build_tree():
    '''
    my_turtle.left(90)  
    my_turtle.up()
    my_turtle.backward(70)
    my_turtle.down()
    '''
    
    r = BinaryTree('a')
    print( r.get_root_val() )
    '''
    my_turtle.circle(45, None, None)
    my_turtle.setpos(-60, 0)
    my_turtle.write(r.get_root_val())
    my_turtle.down
    my_turtle.left(60)
    my_turtle.forward(60)
    '''
    r.insert_left_child('b')
    print( r.get_left_child().get_root_val() )
    '''
    my_turtle.circle(45, None, None)
    my_turtle.setpos(-60, 0)
    my_turtle.write(r.get_left_child().get_root_val())
    my_turtle.right(120)
    my_turtle.backward(60)
    my_turtle.right(60)
    my_turtle.forward(60)
    '''
    
    r.insert_right_child('c')
    print( r.get_right_child().get_root_val() )
    '''
    my_turtle.circle(45, None, None)
    my_turtle.setpos(-60, 0)
    my_turtle.write(r.get_right_child().get_root_val())
    my_turtle.left(120)
    my_turtle.backward(60)
    my_turtle.right(60)
    '''
    
    r.get_left_child().insert_right_child('d')
    print(r.get_left_child().get_right_child().get_root_val())
    
    r.get_right_child().insert_left_child('e')
    r.get_right_child().insert_right_child('f')
    print( r.get_right_child().get_left_child().get_root_val() + r.get_right_child().get_right_child().get_root_val() )
    
    #my_win.exitonclick()

def main():
    print("Enter choice to run the program")
    print( "\t 1. Main Testing")
    print( "\t 2. Self Check")
    print( "\t 3. Build Tree")
    value = 'P'
    while value.upper() != 'Q':
        value = raw_input("Enter choice: " )
        
        if value.upper() == 'Q':
            break
        
        if value == "1":
            main_testing()
        elif value == "2":
            self_check()
        elif value == "3":
            build_tree()
            
#main()
