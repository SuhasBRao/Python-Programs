#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    mnth_days = [31,28,31,30,31,30,31,31]
    if year > 1918:
        if (year%400 == 0) or (year%4 ==0 and year%100 !=0):
            mnth_days[1] = 29
    else:
         if (year%4 == 0):
            mnth_days[1] = 29
    if year == 1918:
            
        total_days = sum(mnth_days)
        pd = 256 - total_days +13
    else:
        total_days = sum(mnth_days)
        pd = 256 - total_days 
        
    return f'{pd}.09.{year}'

if __name__ == '__main__':
    
    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)