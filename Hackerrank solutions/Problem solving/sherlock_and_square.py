#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def is_Square(n):
    if (math.ceil(math.sqrt(n)) ==
       math.floor(math.sqrt(n))):
        return n
    

def squares(a, b):
    # Write your code
    x = a
    while not is_Square(x):
        x += 1
    root = math.sqrt(x)
    cnt = 1
    while root**2 < b:
        cnt += 1
        root += 1
    return cnt

if __name__ == '__main__':
    
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)
        print(result)

        