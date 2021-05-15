'''
This program contains solution for below hackerank problem.
Problem -> https://www.hackerrank.com/challenges/py-check-subset/problem
'''

from sys import stdin

def getInputs():
    return set(map(int,stdin.readline().strip().split()))

no_test = int(input())

while no_test>0:
    n = int(input())
    setA = getInputs()
    m = int(input())
    setB = getInputs()
    if setA.issubset(setB):
        print(True)
    else:
        print(False)
    no_test -= 1 
