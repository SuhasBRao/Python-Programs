import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    a = Counter(a)
    b = Counter(b)
    
    sm = sum((a-b).values())
    sm += sum((b-a).values())
    return sm
    #print(sm)
    
    
    
if __name__ == '__main__':
    
    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)