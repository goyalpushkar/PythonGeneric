'''
Created on Mar 5, 2020

@author: goyalpushkar
'''

import threading
from threading import *

#Threading without creating a class
def threadWithoutClass():
    print(current_thread().getName())
    def mt():
        print("Child Thread")
    child=Thread(target=mt)
    child.start()
    print("Executing thread name :",current_thread().getName())

#Threading by extending thread class
class myThread(threading.Thread):
    def run(self):
        for x in range(7):
            print("Hi from child")
            
def threadUsingThreadClass():
    a = myThread()
    a.start()
    a.join  #join() function makes the main thread wait for the child to finish.
    print("Bye from " + current_thread().getName())
    
#Threadong without extending thread class
class ex:
    def myfunc(self): #self necessary as first parameter in a class func
        for x in range(7):
            print("Child")
            
def threadWithoutThreadClass():
    myobj=ex()
    thread1=Thread(target=myobj.myfunc)
    thread1.start()
    thread1.join()
    print("done")

##Wihtout Threading
import time
def sqr(n):
    for x in n:
        time.sleep(1)
        print('Remainder after dividing by 2', x%2 )
        
def cube(n):
    for x in n:
        time.sleep(1)
        print('Remainder after dividing by 3', x%3 )
        
n=[1,2,3,4,5,6,7,8]

def withoutThreading():
    s=time.time()
    sqr(n)
    cube(n)
    e=time.time()
    print(e-s)
    
def withThreading():
    s=time.time()
    sqrThread = Thread(target=sqr, args=(n,))
    cubeThread = Thread(target=cube, args=(n,))
    sqrThread.run()
    #time.sleep(1)
    cubeThread.run()
    sqrThread.join()
    cubeThread.join()
    e=time.time()
    print(e-s)

if __name__ == '__main__':
    #threadWithoutClass()
    #threadUsingThreadClass()
    #threadWithoutThreadClass()
    
    withoutThreading()
    withThreading()