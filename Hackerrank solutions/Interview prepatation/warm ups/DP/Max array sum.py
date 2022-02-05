import math
import os
import random
import re
import sys
import csv
# Complete the maxSubsetSum function below.
def maxSubsetSum(arr,memo = {}):
    maxi = 0
    neg = lambda x: True if x<0 else False
    
    if arr == [] or all(map(neg,arr)):
        return 0
    if len(arr) == 1:
        return arr[0]
        
    for indx,ele in enumerate(arr):
        non_adj = arr[indx+2:]
        if ele in memo.keys():
            maxi = max(maxi, memo[ele])
            
        elif non_adj:
            #if ele not in memo.keys():
            memo[ele] = ele  + maxSubsetSum(non_adj, memo)
        else: memo[ele] = ele
        #memo[ele] = [x+ele for x in maxSubsetSum(non_adj)]
        maxi = max(maxi, memo[ele])
        
    return maxi
    
    

if __name__ == '__main__':
    
    
    with open("inpt.txt") as file: 
        #n = int(input())
        arr  = []
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            #arr = list(map(int, input().rstrip().split()))
            row = [arr.append(int(x)) for x in row]
        n = arr.pop(0)
        #print(arr[0])
        res = maxSubsetSum(arr)
        #print(res)
        #print(len(arr))
    
    

    '''
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    #print(arr)
    res = maxSubsetSum(arr)

    print(res)
    '''
    
         
    