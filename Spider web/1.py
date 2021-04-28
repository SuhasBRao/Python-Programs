'''
This program contains my solution for 1st problem in Spider-web
Coding challenge
'''
from sys import stdin,stdout
from collections import Counter

def getInputs():
    return list(map(int, stdin.readline().strip().split()))

N = int(input())
arr = getInputs()
my_diction = Counter(arr)
my_diction = dict(my_diction)
max_val = max(my_diction.values())
max_key = next(key for key, value in my_diction.items() if value == max_val)
indx = arr.index(max_key)
print(max_val,indx)