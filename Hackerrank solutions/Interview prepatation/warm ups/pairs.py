import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    no_pairs = 0
    socks_no = Counter(ar)
    for item in socks_no:
        val = socks_no.get(item)
        
        no_pairs += math.floor(val/2)

      
    return no_pairs

if __name__ == '__main__':
    
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
