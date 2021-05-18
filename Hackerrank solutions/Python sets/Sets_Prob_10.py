'''
This program contains solution for below hackerank problem.
Problem -> https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
'''

from sys import stdin

def getInputs():
    return set(map(int,stdin.readline().strip().split()))

N = int(input())
setA = getInputs()
M = int(input())
setB = getInputs()

symmetric_difference = setA.symmetric_difference(setB)
print(len(symmetric_difference))