#!/usr/bin/python

import random
import time

def selectionsort(li):
    for i in range(len(li) - 1):
        for j in range(i + 1, len(li)):
            if li[i] > li[j]:
		tmp = li[i]
		li[i] = li[j]
		li[j] = tmp
if __name__ == "__main__":
    li = [random.randrange(3000) for i in range(20000)]
    start = time.time()
    print start
    selectionsort(li)
    end = time.time()
    print end
