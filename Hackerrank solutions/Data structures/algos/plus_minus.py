#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = len([x for x in arr if x > 0])
    neg = len([x for x in arr if x < 0])
    zeros = len([x for x in arr if x == 0])
    
    print('{:6f} \n{:6f} \n{:6f}'.format(pos/n,neg/n,zeros/n))
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
