'''
This program implements solution for the following problem no hackerrank.
Problem -> https://www.hackerrank.com/challenges/py-the-captains-room/problem
'''
from sys import stdin,stdout

def getInputs():
    return list(map(int,stdin.readline().strip().split()))

k = int(input())
arr = getInputs()
myset = set(arr)

print(((sum(myset)*k)-(sum(arr)))//(k-1))
