#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    
    beautifulDays_count = 0
    # Write your code here
    for num in range(i,j+1):
        rev_num = int(''.join(str(num))[::-1])
        if abs(num - rev_num) % k == 0:
            beautifulDays_count += 1
    
    return beautifulDays_count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)
    
    print(result)

    
