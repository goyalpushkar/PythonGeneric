'''
Created on Jan 10, 2020

@author: goyalpushkar
'''
from OO_Fraction import Fraction
import fractions

if __name__ == '__main__':
    pass

c = 5 
c1 = fractions.Fraction(3, 4) 
x = Fraction(4, -6)
y = Fraction(3, 4)
print("c = " + str(c.numerator) + "/" + str(c.denominator) )  #str(c) + " :Num = " +
print("c1 = " + str(c1.numerator) + "/" + str(c1.denominator) )  #str(c) + " :Num = " +
print("x = " + str(x) )
print("y = " + str(y) )
print(y.__str__())
print(y.__repr__())
print("\n")

print( "x > y = " +  (x > y).__str__() )
print( "y > x = " +  (y > x).__str__() )
print( "y < c = " +  (y < c).__str__() )
print( "y <= c = " +  (y <= c).__str__() )
print( "y >= c1 = " +  (y >= c1).__str__() )
print( "y = c1 = " +  (y == c1).__str__() )
print( "x != c = " +  (x != c).__str__() )
print("\n")

z = x - y
print("x-y = " + str(z) )

z = x - c
print("x-c = " + str(z) )

z = c - x
print("c-x = " + str(z) )

z = x/y
print("x/y = " + str(z) )

z = y/c
print("y/c = " + str(z) )

z = c/y   
#not working and giving result same as y/c when __rdiv__ = __div__
#working when __rdiv__ is changed 
print("c/y = " + str(z) )

z = x*y
print("x*y = " + str(z) )

z = y*c
print("y*c = " + str(z) )

z = c*y
print("c*y = " + str(z) )

x -= y
print("x-=y = " + str(x) )

x += c
print("x+=c = " + str(x) )

c += y
print("c+=y = " + str(c) )

