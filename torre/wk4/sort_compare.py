#!/usr/bin/python3
import time
import random

def main():
    sum_insertion_sort = sum_shell_sort = sum_python_sort = 0

    for maximum_value in 100,500,1000 :
        for index in range(100):
            current_list = random.sample(range(maximum_value*2),maximum_value)
            sum_insertion_sort += insertion_sort(current_list)
            sum_shell_sort += shell_sort(current_list)
            sum_python_sort += python_sort(current_list)

    #Calculating the averages of each function now
    print("Insertion sort took %10.7f seconds to run, on average"% (sum_insertion_sort/300))
    print("Shell Sort took %10.7f seconds to run, on average"% (sum_shell_sort/300))
    print("Python Sort took %10.7f seconds to run, on average"% (sum_python_sort/300))



def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

    end = time.time()
    return end-start
def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        #print("After increments of size", sublist_count, "The list is",a_list)
        sublist_count = sublist_count // 2

    end = time.time()
    return end-start
def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value

def python_sort(a_list):
    start = time.time()
    a_list.sort()
    end = time.time()
    return end-start

if __name__ == "__main__": main()
