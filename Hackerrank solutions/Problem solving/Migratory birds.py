import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    # solution from discussions
    x=list(set(arr))
    y=sorted([(arr.count(i),i) for i in x], key=lambda x:x[0])[::-1]

    for i in range(len(y)):
        if y[0][0]==y[1][0] and y[0][1]>y[1][1]:
            return y[1][1]
        else:
            return y[0][1]
        

if __name__ == '__main__':
    
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    sys.stdout.write(str(result))
