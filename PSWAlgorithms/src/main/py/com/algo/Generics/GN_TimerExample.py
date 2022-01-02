'''
Created on Jan 23, 2020

@author: goyalpushkar
'''

if __name__ == '__main__':
    pass

#import timeit
from timeit import Timer
import random
from matplotlib import pyplot

##Check List operations
'''
def test1(): 
    l = []
    for i in range(1000): 
        l = l + [i]
def test2(): 
    l = []
    for i in range(1000): 
        l.append(i)
def test3():
    l = [i for i in range(1000)]
def test4():
    l = list(range(1000))

t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3") 
print("comprehension ",t3.timeit(number=1000), "milliseconds") 
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")
'''

xAxis = []
yAxisZero = []
yAxisEnd = []

'''
##Comaprison of Pop(0) and pop() in list
pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")
for i in range(1000000,10000001,1000000):  #100000001
    x = list(range(i))    
    pz = pop_zero.timeit(1000)
    x = list(range(i))  
    pe = pop_end.timeit(1000)
    print("%d %15.5f %15.5f" %(i, pz, pe) )
    yAxisZero.append(pz)
    yAxisEnd.append(pe)
    xAxis.append(i)
    #xAxisEnd.append(i)
    #pyplot.plot(i, pz)
    #pyplot.hlines(i, 10000000, 10000001)
    #pyplot.vlines(pz, 0, 100)
    #pyplot.vlines(pe, 0, 100)
 
#pyplot.title("Compare pop(0) and pop() from List")
'''

##Comparison of List and Dictionary contains operation
'''  
xAxis = []
yAxisZero = []
yAxisEnd = []
for i in range(1000000,10000001,1000000):  #100000001
    getRandom = Timer("random.randrange(%d) in x" %i, "from __main__ import random, x")
    x = list(range(i))    
    listContains = getRandom.timeit(1000)
    x = { j:None for j in range(i)}
    DictContains = getRandom.timeit(1000)
    print("%d %15.5f %15.5f" %(i, listGet, DictGet) )
    yAxisZero.append(listContains)
    yAxisEnd.append(DictContains)
    xAxis.append(i)
    #pyplot.plot(i, pz)
    #pyplot.hlines(i, 10000000, 10000001)
    #pyplot.vlines(pz, 0, 100)
    #pyplot.vlines(pe, 0, 100)

pyplot.title("Compare contains from List and Dictionary") 
#pyplot.ylabel("Time(s) to execute get statement")
'''

##Comparison of List index, Get and Set on Dictionary  
xAxis = []
yAxisZero = []
yAxisEnd = []
yAxisDictGet = []
yAxisListDel = []
yAxisDictDel = []
print("%20s %15s %15s %20s %15s %15s" %("Index", "List Index", "List Del", "Dictionary Set", "Dictionary Get", "Dictionary Del" ) )
for i in range(1000000,9000001,1000000):  #100000001
    listIndex = Timer("x.index( random.randrange(%d) )" %i, "from __main__ import random, x")
    listDel = Timer("del x[random.randrange(%d)]" %(i-1), "from __main__ import random, x")
    #x.__delitem__( random.randrange(%d) )
    
    dictSet = Timer("x[random.randrange(%d)] = random.randrange(%d)" %(i, i), "from __main__ import random, x")
    dictGet = Timer("x.get( random.randrange(%d) )" %i, "from __main__ import random, x")
    dictDel = Timer("del x[random.randrange(%d)]" %(i-1), "from __main__ import random, x")
    #x.__delitem__( random.randrange(%d) )
    
    x = list(range(i))    
    listIndexI = listIndex.timeit(1000)
    listDelD = listDel.timeit(10)
    
    x = { j:j for j in range(i) }
    DictSetI = dictSet.timeit(1000)
    DictGetI = dictGet.timeit(1000)
    dictDelD = dictDel.timeit(10)
    
    print("%20d %15.5f %15.5f %15.5f %15.5f %15.5f" %(i, listIndexI, listDelD, DictSetI, DictGetI, dictDelD) )
    yAxisZero.append(listIndexI)
    yAxisEnd.append(DictSetI)
    yAxisDictGet.append(DictGetI)
    yAxisListDel.append(listDelD)
    yAxisDictDel.append(dictDelD)
    xAxis.append(i)
pyplot.title("Compare List index, List Del, Get, Set and Del on Dictionary")

print("Show plot")
subplot = pyplot.subplot()
pyplot.ylabel("Time(s) to execute statements")
pyplot.xlabel("List Size")

#ax = pyplot.axes()
#pyplot.axis(1000000,10000000, -1, 25)
pyplot.xticks(xAxis)
subplot.plot(xAxis, yAxisZero, 'bo--', label='List Index', marker='.',linewidth = 6)   #ZeroPop List Use Short form color='blue', linestyle='solid'
subplot.plot(xAxis, yAxisListDel, 'g', linestyle='dashed', label='List Del', marker='p',linewidth = 7)   #ZeroPop 
subplot.plot(xAxis, yAxisEnd, color='red', linestyle='solid', label='Dictionary Set', marker='^', linewidth = 8)  #EndPop  Dictionary
subplot.plot(xAxis, yAxisDictGet, 'c', linestyle='dotted', label='Dictionary Get', marker='s',linewidth = 9)   #ZeroPop 
subplot.plot(xAxis, yAxisDictDel, 'y', linestyle='dashdot', label='Dictionary Del', marker='p',linewidth = 10)   #ZeroPop 

#legend works only after giving label
chartBox = subplot.get_position()  ##This is required to put legend outside
subplot.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.7, chartBox.height])
subplot.legend(loc='upper center', bbox_to_anchor=(1.30, 0.8), shadow=True, ncol=1)
#pyplot.legend
#(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2) Put legend in the bottom
#(loc='upper center', bbox_to_anchor=(0.5, 1.00), shadow=True, ncol=2) Put legend on the top
 
pyplot.show()
#pyplot.show()