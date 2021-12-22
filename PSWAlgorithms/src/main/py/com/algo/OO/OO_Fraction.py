'''
Created on Jan 10, 2020

@author: goyalpushkar
'''
from asn1crypto.core import InstanceOf
import fractions

class Fraction: 
    '''
    classdocs
    '''
    def __init__(self, top, bottom):
        '''
        Constructor
        '''
        if ( not isinstance(top, int) ) or (not isinstance(bottom, int) ):
            raise TypeError("The numerator and denominator must be integers.")
        
        if bottom == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        
        common = gcd( abs(top), abs(bottom) )
        #print("Common " + str(common) )
        if ( bottom < 0 ):
            #print("< 0")
            self.num = -1 * (top//common)
            self.den = -1 * (bottom//common) 
        else: 
            self.num = top//common
            self.den = bottom//common 
            
        #print( str(self.num) + " " + str(self.den) )
            
    def __get_num__(self):
        return self.num
    
    def __get_den__(self):
        return self.den
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    #Following are differences:
    ##str() is used for creating output for end user while repr() is mainly used for debugging and development. 
    ##reprs goal is to be unambiguous and strs is to be readable. For example, if we suspect a float has a small rounding error, repr will show us while str may not.
    ##repr() compute the official string representation of an object (a representation that has all information about the abject) and str() is used to compute the informal string representation of an object (a representation that is useful for printing the object).
    ##The print statement and str() built-in function uses __str__ to display the string representation of the object while the repr() built-in function uses __repr__ to display the object.
    def __repr__(self):
        return "Fraction(" + str(self.num) + ", " + str(self.den) + ")"
        
    def __add__(self, otherFraction):
        if ( isinstance(otherFraction, (int, fractions.Fraction, float)) ):
            otherNum = otherFraction.numerator
            otherDen = otherFraction.denominator
        else:
            otherNum = otherFraction.num
            otherDen = otherFraction.den
            
        new_num = self.num * otherDen + self.den * otherNum
        new_den = self.den * otherDen
        
        #common = gcd(new_num, new_den)
        if ( new_den <  0 ):
            return Fraction( -1 * new_num, -1 * new_den )
        else: 
            return Fraction( new_num , new_den ) #// common
    
    ##Imagine you've defined a type Foo and it makes sense to be able to add an instance of Foo 
    ##(we'll call it f) and an integer together. If you write f + 5, Python will call f.__add__(5). 
    ##But if you write 5 + f, Python will call (5).__add__(f), which will return an error 
    ##(because integers don't know how to add themselves to instances of Foo). 
    ##So, after (5).__add__(f) fails, Python will then try f.__radd__(5)    
    
    #after replacing num with numerator and den with denominator in current class __radd is not required
    #def __radd__(self, otherFraction):
    #    new_num = self.num * otherFraction.denominator + self.den * otherFraction.numerator
    #    new_den = self.den * otherFraction.denominator
    #    #common = gcd(new_num, new_den)
    #    return Fraction( new_num , new_den )
    __radd__ = __add__
    
    # __iadd__ is for self adding like +=
    def __iadd__(self, otherFraction):
        if ( isinstance(otherFraction, (int, fractions.Fraction, float)) ):
            otherNum = otherFraction.numerator
            otherDen = otherFraction.denominator
        else:
            otherNum = otherFraction.num
            otherDen = otherFraction.den
            
        new_num = self.num * otherDen + self.den * otherNum
        new_den = self.den * otherDen
        self.num = new_num
        self.den= new_den
        return self
    
    def __sub__(self, otherFraction):
        if ( isinstance(otherFraction, (int, fractions.Fraction, float)) ):
            otherNum = otherFraction.numerator
            otherDen = otherFraction.denominator
        else:
            otherNum = otherFraction.num
            otherDen = otherFraction.den
            
        new_num = self.num * otherDen - self.den * otherNum
        new_den = self.den * otherDen
        #common = gcd(new_num, new_den)
        if ( new_den <  0 ):
            return Fraction( -1 * new_num, -1 * new_den )
        else: 
            return Fraction( new_num , new_den ) #// common
       
    def __rsub__(self, otherFraction):
        if ( isinstance(otherFraction, (int, fractions.Fraction, float)) ):
            otherNum = otherFraction.numerator
            otherDen = otherFraction.denominator
        else:
            otherNum = otherFraction.num
            otherDen = otherFraction.den
            
        new_num = self.den * otherNum - self.num * otherDen
        new_den = self.den * otherDen
        #common = gcd(new_num, new_den)
        if ( new_den <  0 ):
            return Fraction( -1 * new_num, -1 * new_den )
        else: 
            return Fraction( new_num , new_den ) #// common
     
    def __mul__(self, otherFraction):
        if ( isinstance(otherFraction, (int, fractions.Fraction, float)) ):
            otherNum = otherFraction.numerator
            otherDen = otherFraction.denominator
        else:
            otherNum = otherFraction.num
            otherDen = otherFraction.den
            
        new_num = self.num * otherNum
        new_den = self.den * otherDen
        common = gcd(new_num, new_den)
        return Fraction( new_num // common, new_den // common)
       
    __rmul__ = __mul__
    
    ##def __truediv__
    def __div__(self, otherFraction):
        if ( isinstance(otherFraction, (int, fractions.Fraction, float)) ):
            otherNum = otherFraction.numerator
            otherDen = otherFraction.denominator
        else:
            otherNum = otherFraction.num
            otherDen = otherFraction.den
            
        new_num = self.num * otherDen
        new_den = self.den * otherNum
        common = gcd(new_num, new_den)
        return Fraction( new_num // common, new_den // common)
    
    def __rdiv__(self, otherFraction):
        if ( isinstance(otherFraction, (int, fractions.Fraction, float)) ):
            otherNum = otherFraction.numerator
            otherDen = otherFraction.denominator
        else:
            otherNum = otherFraction.num
            otherDen = otherFraction.den
            
        new_num = otherNum * self.den 
        new_den = self.num * otherDen
        common = gcd(new_num, new_den)
        return Fraction( new_num // common, new_den // common)
        
    def __eq__(self, otherFraction):
        if ( isinstance(otherFraction, (int, fractions.Fraction, float)) ):
            otherNum = otherFraction.numerator
            otherDen = otherFraction.denominator
        else:
            otherNum = otherFraction.num
            otherDen = otherDen
            
        first_num = self.num * otherDen
        second_num = otherNum * self.den
        return first_num == second_num

    def __gt__(self, otherFraction):
        #print("__gt__")
        if ( isinstance(otherFraction, (int, fractions.Fraction, float)) ):
            otherNum = otherFraction.numerator
            otherDen = otherFraction.denominator
        else:
            otherNum = otherFraction.num
            otherDen = otherFraction.den
        
        #print( str(self.num) + " " + str(self.den) )
        first_num = self.num * otherDen 
        second_num = otherNum * self.den
        return first_num > second_num
 
    def __ge__(self, otherFraction):
        if ( isinstance(otherFraction, (int, fractions.Fraction, float)) ):
            otherNum = otherFraction.numerator
            otherDen = otherFraction.denominator
        else:
            otherNum = otherFraction.num
            otherDen = otherFraction.den
            
        first_num = self.num * otherDen 
        second_num = otherNum * self.den
        return first_num >= second_num   
    
    def __lt__(self, otherFraction):
        if ( isinstance(otherFraction, (int, fractions.Fraction, float)) ):
            otherNum = otherFraction.numerator
            otherDen = otherFraction.denominator
        else:
            otherNum = otherFraction.num
            otherDen = otherFraction.den
            
        first_num = self.num * otherDen 
        second_num = otherNum * self.den
        return first_num < second_num
 
    def __le__(self, otherFraction):
        if ( isinstance(otherFraction, (int, fractions.Fraction, float)) ):
            otherNum = otherFraction.numerator
            otherDen = otherFraction.denominator
        else:
            otherNum = otherFraction.num
            otherDen = otherFraction.den
            
        first_num = self.num * otherDen
        second_num = otherNum * self.den
        return first_num <= second_num   

    def __ne__(self, otherFraction):
        if ( isinstance(otherFraction, (int, fractions.Fraction, float)) ):
            otherNum = otherFraction.numerator
            otherDen = otherFraction.denominator
        else:
            otherNum = otherFraction.num
            otherDen = otherFraction.den
            
        first_num = self.num * otherDen 
        second_num = otherNum * self.den
        return first_num <> second_num  
     
def gcd(m,n):
        while( m % n ) != 0:
            old_m = m
            old_n = n
            
            m = old_n
            n = old_m % old_n
        return n 
    
