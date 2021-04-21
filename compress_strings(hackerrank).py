
'''
This program implements solution for hackerrank problem of compress string.
https://www.hackerrank.com/contests/pythonist3/challenges/compress-the-string/problem
'''

import itertools
from sys import stdin,stdout

def getInputs():
    return stdin.readline().strip()
arr = getInputs()

x = itertools.groupby(arr)
my_str = ''
for k,g in x:
    my_str += ' ' + f'{(int(k), list(g).count(k))}'

stdout.writelines(my_str)