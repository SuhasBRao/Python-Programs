'''
This program implements solution for the following problem no hackerrank.
Problem -> https://www.hackerrank.com/challenges/py-set-union/problem
'''
from sys import stdin,stdout

def getInputs():
    return set(map(int,stdin.readline().strip().split()))

N = int(input())
set1 = getInputs()
M = int(input())
set2 = getInputs()

new_set = set1.union(set2)
print(len(new_set))