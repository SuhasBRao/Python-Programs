import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    itr = iter(scores)
    max_cnt, min_cnt = 0,0
    max_val, min_val = scores[0],scores[0]
    notDone = True
    while notDone:
        try:
            cur = next(itr)
            if cur > max_val:
                max_val = cur
                max_cnt += 1
            if cur < min_val:
                min_val = cur
                min_cnt += 1
            pass
        except:
            #print(max_cnt, min_cnt)
            notDone = False
            pass
    return max_cnt, min_cnt
  

if __name__ == '__main__':
    
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)