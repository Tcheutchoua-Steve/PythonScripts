#!/usr/bin/python3
import time
import random

def main(item):
    sum_ss = sum_oss = sum_bsi = sum_bsr = 0

    for maximum_value in 100,500,1000 :
        for index in range(100):
            current_list = random.sample(range(maximum_value*5),maximum_value)
            sum_ss += sequential_search(current_list,item)[1]
            current_list.sort()
            sum_oss += ordered_sequential_search(current_list,item)[1]
            sum_bsi += binary_search_iterative(current_list,item)[1]
            sum_bsr += binary_search_recursive(current_list,item)[1]

    #Calculating the averages of each function now
    print("Sequential Search took %10.7f seconds to run, on average"% (sum_ss/300))
    print("Ordered Sequential Search took %10.7f seconds to run, on average"% (sum_oss/300))
    print("Iterative Binary Search took %10.7f seconds to run, on average"% (sum_bsi/300))
    print("Recursive Binary Search took %10.7f seconds to run, on average"% (sum_bsr/300))



def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1

    end = time.time()
    return found , end-start

def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()
    return found , end-start


def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    return found , end-start

def binary_search_recursive(a_list, item):
    start = time.time()
    if len(a_list) == 0:
        end = time.time()
        return False , end-start
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            end = time.time()
            return True , end-start
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

if __name__ == "__main__": main(-1)
