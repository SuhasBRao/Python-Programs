#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if y1>y2:
        #if year of return is greater than year due
        return 10000
    elif m1>m2 and y1==y2:
        #if returned in the same year and month of return is greater than month due
        return (m1-m2)*500
    elif d1>d2 and y1==y2 and m1==m2:
        #if returned in the same year and month, and the date of return is greater than due date
        return (d1-d2)*15
    else:
        return 0
    
if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)
