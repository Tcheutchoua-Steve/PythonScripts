#!/usr/bin/python3
import time

def some_function():

    start = time.time()
    sum = 0
    for i in range (0,500):
        sum += i

    end = time.time()
    return sum, end-start

time_result = some_function()[1]
print ("%10.7f" % time_result)

aList = ['123', 'xyz', 'zara', 'abc', 'xyz']

aList.sort()
print ("List : ", aList)
