#!/usr/bin/python

import random
import time

def insertionsort(li):
    for i in range(1, len(li)):
	current_pos = i
        current_val = li[i]
	while current_val < li[current_pos - 1] and current_pos > 0:
	    li[current_pos] = li[current_pos - 1]
	    current_pos -= 1
	else:
	    li[current_pos] = current_val

if __name__ == "__main__":
    li = [random.randrange(30000) for i in xrange(20000)]
    start = time.time()
    insertionsort(li)
    end = time.time()
    print end - start	    
