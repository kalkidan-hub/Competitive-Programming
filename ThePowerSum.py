#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N):
    
    def subset(target, current):
        if target == 0:
            return 1
        if target < 0 or current <= 0:
            return 0
        
        ct1 = subset(target - (current ** N),current - 1)
        ct2 = subset(target,current - 1)
        
        return ct1 + ct2
    
    
    return subset(X,math.floor(X**(1/N)))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
