import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sum_arr = []
    for i in range(len(arr)):
        if all(ele == arr[0] for ele in arr):
            max_term = sum(arr) - arr[0]
            min_term = max_term
            print(min_term, max_term)
            return
        
        four_ele_sum = sum([x for x in arr if x != arr[i]])
        sum_arr.append(four_ele_sum)
         
    print(min(sum_arr),max(sum_arr))
    #print(min(sum_arr),max(sum_arr))
        
    pass

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
