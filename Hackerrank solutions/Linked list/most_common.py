'''
Problem statement --> https://www.hackerrank.com/challenges/most-commons/problem
'''
import math
import os
import random
import re
import sys
from collections import Counter

def most_cmn(mystr):
    mylst = [x for x in mystr]
    mylst.sort()
    my_cntr = Counter(mylst)
    final_otpt_lst = my_cntr.most_common(3)
    for tpls in final_otpt_lst:
        print(*tpls)
    

if __name__ == '__main__':
    s = input()
    most_cmn(s)
