
import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    val = 0
    for i in range(len(s) - 1):
        if s[i] ==  s[i + 1]:
            val+= 1
    #print(val)
    
    
    return(val)   
    
    pass

if __name__ == '__main__':
    
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(result)