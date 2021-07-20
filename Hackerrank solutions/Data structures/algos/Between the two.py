import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    # Write your code here
    
    # grabs the elements in range a[-1] to b[0] + 1
    cm_multi = [x for x in range(a[-1],b[0] + 1)]
    
    # Below statements checs how many numbers in cm_multi 
    # is divisible by all elements of list a
    isdivi = lambda n,mylst: all(map(lambda y: n%y == 0, mylst)) 
    cm_multi = [x for x in cm_multi if isdivi(x,a)]
    
    # Below condition checks which numbers from cm_multi divides
    # all elements of list b.

    divids = lambda n,mylst: all(map(lambda y: y%n == 0, mylst))
    cm_multi = [x for x in cm_multi if divids(x,b)]

    return len(cm_multi)

    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)