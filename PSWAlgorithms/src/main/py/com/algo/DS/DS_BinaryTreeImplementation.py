'''
Created on Feb 12, 2020

@author: goyalpushkar
'''
from src.main.py.com.algo.DS.DS_BinaryTreeUsingList import get_left_child


if __name__ == '__main__':
    pass

from DS_Stack import Stack
from DS_BinaryTreeUsingClass import BinaryTree, main as main_class
from DS_BinaryTreeUsingList import binary_tree, main as main_list
import operator

def build_parse_tree(fp_exp):
    fp_list = fp_exp.split()
    
    parentStack = Stack()
    e_tree = BinaryTree('')
    parentStack.push(e_tree)
    
    current_tree = e_tree
    
    for element in fp_list:
        #print( element + e_tree.get_root_val() )
        if element == '(':
            current_tree.insert_left_child('')
            parentStack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif element not in ('+','-','*','/',')'):
            current_tree.set_root_val(int(element))
            current_tree = parentStack.pop()
        elif element in ('+','-','*','/'):
            current_tree.set_root_val(element)
            current_tree.insert_right_child('')
            parentStack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif element == ')':
            current_tree = parentStack.pop()
        else:
            raise ValueError
        
    return e_tree


def evaluator(e_tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    
    left = e_tree.get_left_child()
    right= e_tree.get_right_child()
    
    if left and right:
        fn = opers[e_tree.get_root_val()]
        return fn( evaluator(left), evaluator(right) )
    else:
        return e_tree.get_root_val()
   
def postorder_eval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    if tree:
        res1 = postorder_eval( tree.get_left_child() )
        res2 = postorder_eval( tree.get_right_child() )
        
        if res1 and res2:
            return opers[str(tree.get_root_val())](res1, res2)
        else:
            return tree.get_root_val()
         
def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())
        
def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())
        
def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())
        
#Write method for level order traversal        
    
#print_exp
def inorder_exp(tree):
    strValue = ""
    if tree:
        if str(tree.get_root_val()).isdigit():
            strValue = inorder_exp( tree.get_left_child() )
        else:
            strValue = "(" + inorder_exp( tree.get_left_child() )
        
        strValue = strValue + str(tree.get_root_val())
        
        if str(tree.get_root_val()).isdigit():
            strValue = strValue + inorder_exp( tree.get_right_child() )
        else:
            strValue = strValue + inorder_exp( tree.get_right_child() ) + ")" 
 
    return strValue 

def buildTreeClass(value):
    return BinaryTree(value)

def buildTreeList(value):
    return binary_tree(value)

def insertLeftChild(tree, value):
    tree.insert_left_child(value)
    
def insertRightChild(tree, value):
    tree.insert_right_child(value)
    
def ex12():
    x = BinaryTree('language')
    x.insert_left_child('compiled')
    x.insert_right_child('interpreted')
    x.get_left_child().insert_left_child('C')
    x.get_left_child().insert_right_child('Java')
    x.get_right_child().insert_left_child('Python')
    x.get_right_child().insert_right_child('Scheme')
    
    print(x.get_root_val(), x.get_left_child().get_root_val(), x.get_right_child().get_root_val(), x.get_left_child().get_left_child().get_root_val(), x.get_left_child().get_right_child().get_root_val(), x.get_right_child().get_left_child().get_root_val(), x.get_right_child().get_right_child().get_root_val())
    
def main():
    print("Enter number for below programs")
    print("\t 1. Test Tree Using Lists")
    print("\t 2. Test Tree using Class")
    print("\t 3. Build Parse Tree")
    print("\t 4. Evaluate Parse Tree")
    print("\t 5. PreOrder Tree")
    print("\t 6. Post Order Tree")
    print("\t 7. In Order Tree")
    print("\t 8. In Order Expression")
    print("\t 9. Post Order Evaluation")
    print("\t 10. Build Tree using List")
    print("\t 11. Build Tree using Class")
    print("\t 12. Exercise 12")
    print("\t 12. Exercise 12")
    
    userInput = 'P'
    while userInput != 'Q':
        userInput = raw_input("Enter number corresponding to above function or Q to quit: ")
        
        if userInput.upper() == 'Q':
            break
        
        if userInput == '1':
            main_class()
        elif userInput == '2':
            main_list()
        elif userInput == '3':
            math_expr = raw_input('Enter mathematical expression to build the parse tree: ')
            print("math_expr - " + math_expr)
            parsed_tree = build_parse_tree(math_expr)
            print( "Root Value - " + parsed_tree.get_root_val() )
        elif userInput == '4':
            print( "Calculated Value - " + str( evaluator(parsed_tree) ) )
        elif userInput == '5':
            preorder(parsed_tree)
        elif userInput == '6':
            postorder(parsed_tree)
        elif userInput == '7':
            inorder(parsed_tree)
        elif userInput == '8':
            print( "Expression - " + inorder_exp(parsed_tree) )
        elif userInput == '9':
            print( "Calculated Value - " + str( postorder_eval(parsed_tree) ) )
        elif userInput == '10':
            value = raw_input("Enter Root Node")
            tree = buildTreeList(value)    
        elif userInput == '11':
            tree = buildTreeClass(value)  
        elif userInput == '12':
            ex12()  
                    
# ( ( 10 + 5 ) * 3 )
main()