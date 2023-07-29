#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    num_to_insert = arr[-1]
    # print(num_to_insert)
    for i in range(n-1,0,-1):
        if arr[i-1] > num_to_insert:
            arr[i] = arr[i-1]
            print(' '.join([str(k) for k in arr]))
        else:
            arr[i] = num_to_insert
            break
    if i == 1 and arr[i-1] > num_to_insert:
        arr[i-1] = num_to_insert
    print(' '.join(map(str,arr)))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
