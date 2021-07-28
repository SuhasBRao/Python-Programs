
from abc import abstractclassmethod
import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    cntr = Counter(s)
    res = 'NO'
    if len(set(cntr.values())) ==  1:
        res = 'YES'
    else:
        my_dict = Counter(cntr.values())
        print(my_dict)
        
        if len(my_dict) == 2:
            
            mc= my_dict.most_common()[0]
            lc = my_dict.most_common()[-1]
            
            if abs(mc[0] - lc[0]) == 1:
                if 1 in my_dict.values():
                    res = 'YES'
            elif 1 in my_dict.keys() and my_dict[1] == 1:
                res='YES'
    return res

if __name__ == '__main__':
    
    s = input()

    result = isValid(s)
    print(result)