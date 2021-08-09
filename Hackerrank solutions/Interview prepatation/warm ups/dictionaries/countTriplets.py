
import math
import os
import random
import re
import sys
from itertools import combinations
from collections import Counter
# Complete the countTriplets function below.
def checkGP(tup,r):
    return tup[1] == tup[0]*r and tup[2] == tup[1]*r
        
def countTriplets(arr, r):
    val = 0
    combi = Counter([tup for tup in list(combinations(arr,3)) if tup[0]*r == tup[1] and tup[1]*r == tup[2]])
    i = 0
    print(combi)
    for i in range(len(arr)):
        if arr[i]*r in arr[i+1:] and arr[i]*r*r in arr[i+1:]:
            val += combi[(arr[i],arr[i]*r,arr[i]*r*r)]
            #print(arr[i],arr[i]*r, arr[i]*r*r)
            combi[(arr[i],arr[i]*r,arr[i]*r*r)]=0
        
    return val

    pass
if __name__ == '__main__':
   
    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    
    ans = countTriplets(arr, r)
    print(ans)
    