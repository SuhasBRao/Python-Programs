#!/bin/python3

from itertools import count
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

def squares(a, b):
    # Write your code
    count = 0
    a,b = [int(j) for j in input().strip().split()]
    square1 = a ** (.5)
    if (square1 != int(square1)):
        a1 = int(square1) + 1
    else:
        a1 = int(square1)
    square2 = b ** (.5)
    b1 = int(square2)
    count = b1 - a1 +1
    return count

if __name__ == '__main__':
    
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)
        print(result)

        