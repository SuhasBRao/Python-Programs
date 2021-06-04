'''
Problem statement -> https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
'''

from collections import defaultdict

def getInputs(no_times):
    my_tmp = []
    for _ in range(no_times):
        my_tmp.append(input())
    return my_tmp

n,m = map(int,input().split()) # get multiple inputs using this type

A = getInputs(n)
B = getInputs(m)

dflt_dct = defaultdict(list)

for i,v in enumerate(A):
    dflt_dct[v].append(i+1)

for item in B:
    if item in A:
        print(*dflt_dct[item], end = ' ')
        print()
    else:
        print(-1)
