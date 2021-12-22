'''
Created on Jan 26, 2020

@author: goyalpushkar
'''
from altgraph import Graph
from Carbon.QuickTime import kGraphicsImageImportGetSequenceEnabledSelect

if __name__ == '__main__':
    pass

###############################################################3
#from graphics  import *
#from ezgraphics import GraphicsWindow

#win = GraphWin('Sample', 300,300)

###############################################################3
#Testing Plotting Graphs
from matplotlib import pyplot

pyplot.title("Average Temperatures in Keene")
pyplot.bar(1, 33)
pyplot.bar(2, 34.3)
pyplot.bar(3, 40.2)
pyplot.bar(4, 42.2)
pyplot.bar(5, 45.4)
pyplot.bar(6, 50.3)
pyplot.bar(7, 55.4)
pyplot.bar(8, 45.2)
pyplot.bar(9, 42.6)
pyplot.bar(10, 37.2)
pyplot.bar(11, 34.5)
pyplot.bar(12, 33.3)

pyplot.xticks([1,2,3,4,5,6,7,8,9,10,11,12], 
              ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])

pyplot.legend(["High","Low"])
#pyplot.xlim(.8,14)
#pyplot.bar("Jan", 33)
#pyplot.bar("Feb", 34.3)
#pyplot.bar("Mar", 40.2)
#pyplot.bar("Apr", 42.2)
#pyplot.bar("May", 45.4)
#pyplot.bar("Jun", 50.3)
#pyplot.bar("Jul", 55.4)
#pyplot.bar("Aug", 45.2)
#pyplot.bar("Sep", 42.6)
#pyplot.bar("Oct", 37.2)
#pyplot.bar("Nov", 34.5)
#pyplot.bar("Dec", 33.3)

pyplot.xlabel("Month")
pyplot.ylabel("Temperature")

pyplot.show()

###############################################################3
#Testing Epsilon and Math Functions
from math import sqrt
r = sqrt(2.0)
epsilon = 1E-14

#if ( r * r == 2.0 ):
if ( r * r - 2.0 < epsilon):
    print("sqrt of 2 squared is equal to 2.0")
else:
    print("sqrt of 2 squared is not equal to 2.0")

