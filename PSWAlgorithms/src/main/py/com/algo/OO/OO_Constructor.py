'''
Created on Feb 5, 2020

@author: goyalpushkar
'''
        
class CashRegister :
    
    _lastPriceBeforeItemAdd = 0  #class Variable 
    _totalItems = 0 
    #Accessible to all methods with class name It is common to all instances of the class
    
    #Comment constructor for Constructor Test
    #Below test is for the class without constructor
    def __init__(self, items = 0, price = 0):
        self._itemCount = items
        self._totalPrice = price
        
       
    ## Adds an item to this cash register. # @param price the price of this item #
    def addItem(self, price) :
        CashRegister._lastPriceBeforeItemAdd = CashRegister._lastPriceBeforeItemAdd + price
        CashRegister._totalItems = CashRegister._totalItems + 1
        
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price
    
    ## Gets the price of all items in the current sale. # @return the total price
    #
    def getTotal(self) :
        return self._totalPrice
    
    def getCount(self) :
        return self._itemCount
    
    def clear(self) :
        self._itemCount = 0
        self._totalPrice = 0
        

def constructorTest():
    #################################################
    ############# Constructor Test ##################
    #################################################
    #Comment constructor for this test
    checkWoConstructor= CashRegister()
    
    #With calling clear if Constructor __init__ is not defined 
    # Worked fine
    checkWoConstructor.clear()
    
    #Without calling clear if Constructor __init__ is not defined 
    # Got Error - AttributeError: CashRegister instance has no attribute '_itemCount'
    
    checkWoConstructor.addItem(7.5)
    print( "Count - " + str( checkWoConstructor.getCount() ) )
    print( "Price - " + str( checkWoConstructor.getTotal() ) )

def classVariableTest():
    #################################################
    ############### Class Variable ##################
    #################################################
    classVariable1 = CashRegister()
    classVariable2 = CashRegister()
    
    classVariable1.addItem(10)
    print( "Count 1 - " + str( classVariable1.getCount() ) )
    print( "Price 1 - " + str( classVariable1.getTotal() ) )
    print( "Last Total Items and Price 1 - " + str( CashRegister._totalItems ) + ":" + str( CashRegister._lastPriceBeforeItemAdd ) )

    classVariable2.addItem(15)
    print( "Count 2 - " + str( classVariable2.getCount() ) )
    print( "Price 2 - " + str( classVariable2.getTotal() ) )
    print( "Last Total Items and Price 1 - " + str( CashRegister._totalItems ) + ":" + str( CashRegister._lastPriceBeforeItemAdd ) )
    
    classVariable1.addItem(5)
    print( "Count 3 - " + str( classVariable1.getCount() ) )
    print( "Price 3 - " + str( classVariable1.getTotal() ) )
    print( "Last Total Items and Price 1 - " + str( CashRegister._totalItems ) + ":" + str( CashRegister._lastPriceBeforeItemAdd ) )
    
#constructorTest()
classVariableTest()
    
#Self Check
#27