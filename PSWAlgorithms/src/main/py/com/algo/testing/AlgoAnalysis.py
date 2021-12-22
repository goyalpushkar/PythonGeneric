'''
Created on Jan 23, 2020

@author: goyalpushkar
'''

if __name__ == '__main__':
    pass


import time

def sum_of_n2(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i
    end = time.time()
    return the_sum, end-start
    
def sum_of_n3(n):
    start = time.time()
    the_sum = (n * (n+1)) / 2
    end = time.time()
    return the_sum, end-start

for i in range(5):
    print("Sum is %d required %10.8f seconds" % sum_of_n3(10000))