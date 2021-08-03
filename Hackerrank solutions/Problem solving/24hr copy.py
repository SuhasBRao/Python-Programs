mport math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here

    hh,mm,ss = map(int,s[:-2].split(':'))
    meri = s[-2:]
    #print(meri)
    #print(s)
    #print(hh,mm,ss)
    if meri == 'AM' and hh==12:
        hh = 0
    if meri =='PM':
        hh = hh+12 if hh != 12 else 12
    #print(hh)
    print("{:0>2d}:{:0>2d}:{:0>2d}".format(hh,mm,ss))
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)