#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    shared_to = 5
    no_likes_current_day = 0
    cumulative_likes = 0
    
    for days in range(n):
        no_likes_current_day = shared_to // 2
        cumulative_likes += no_likes_current_day
        
        shared_to = no_likes_current_day * 3
    
    return cumulative_likes
    # pass

if __name__ == '__main__':
    n = int(input().strip())

    result = viralAdvertising(n)

    print(result)