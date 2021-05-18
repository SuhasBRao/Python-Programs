import math
import os
import random
import re
import sys

def arrayManipulation(n, queries):
    
    arr = [0]*n
    for query in queries:
        a = query[0] - 1
        b = query[1] - 1
        k = query[2]
        for indx in range(a,b+1):
            new_val = k + arr[indx]
            arr[indx] = new_val
        
    return arr
        
    # Write your code here
def getINputs():
    return list(map(int, sys.stdin.readline().strip().split()))

if __name__ == '__main__':
    
    n,m = getINputs()
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)
