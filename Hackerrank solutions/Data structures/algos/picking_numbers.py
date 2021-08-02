
import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(l):
    
    # Write your code here
    #cur = a[0]
    
    maximum=0
    for i in l:
        c=l.count(i)
        #print(c)
        d=l.count(i-1)
        #print(d)
        c=c+d
        if c > maximum:
            maximum=c
    return maximum

if __name__ == '__main__':
    
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)