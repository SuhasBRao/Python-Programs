
import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    eql_or_grtr = [(ar[i],ar[j]) for i in range(len(ar)) for j in range(len(ar)) 
                   if ar[i] + ar[j] >= k if i < j]
    #print(eql_or_grtr)
    divsble = [x for x in eql_or_grtr if sum(x)%k == 0]
    
    return len(divsble)
    pass

if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    
    print(result)

    