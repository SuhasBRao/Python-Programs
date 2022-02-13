#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    res = []
    n = len(p)
    for x in range(1, n+1):
        for y in range(1,n+1):
            if p[p[y-1] -1] == x:
                res.append(y)
    return res 

if __name__ == '__main__':
    
    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    