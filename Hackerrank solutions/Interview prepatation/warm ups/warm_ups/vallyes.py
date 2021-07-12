import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    my_path_vals = {'D':-1, 'U':1}
    sea_lvl = 0
    no_valley = 0
    for indx,item in enumerate(list(path)):
        
        #print(indx)
        if not sea_lvl+my_path_vals[item] and sea_lvl<0:

            no_valley += 1
        sea_lvl+=my_path_vals[item]

    return no_valley
    

if __name__ == '__main__':
    
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)