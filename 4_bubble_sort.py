#!/usr/bin/python

import time
import random

def bubblesort(bubble_list):
    for j in range(len(bubble_list) - 1):
        for i in range(len(bubble_list) - 1):
            if bubble_list[i] > bubble_list[i + 1]:
	        tmp = bubble_list[i]
	        bubble_list[i] = bubble_list[i + 1]
	        bubble_list[i + 1] = tmp

if __name__ == "__main__":
    bubble_list = [random.randrange(30000) for i in range(20000)]
    start = time.time()
    print start
    bubblesort(bubble_list)
    end = time.time()
    print end
