#!/usr/bin/python

import random
import time

def insertionsort(li):
    for i in range(1, len(li)):
	tmp = li[i]
	for j in range(i-1, -1, -1):
	    if li[j] > tmp:
		li[j+1] = li[j]
	    else:
		li[j + 1] = tmp
		break
	else:
	    li[j] = tmp

if __name__ == "__main__":
    li = [random.randrange(30000) for i in xrange(20000)]
    start = time.time()
    insertionsort(li)
    end = time.time()
    print end - start	    
