
import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    n = len(s)
    m = len(t)
    i = 0
    
    while i < n -1:
        if i >= m-1:
            break
        if s[i] != t[i]:
            break
        i += 1
    diff_str = s[i:]
    print(diff_str)
    diff_len = len(diff_str)
    if diff_len >= k:
        return 'No'
    else:
        return 'Yes'
        
    

if __name__ == '__main__':
    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    