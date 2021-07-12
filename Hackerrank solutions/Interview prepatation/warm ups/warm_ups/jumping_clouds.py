
import math
import os
import random
import re
import sys
from typing import ValuesView

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    x,y = 0,0
    while x<len(c)-2:
        x = x+1 if c[x+2] else x+2
        y+=1
    if x<len(c)-1:
        y+=1
    return y
    

if __name__ == '__main__':
   
    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)
