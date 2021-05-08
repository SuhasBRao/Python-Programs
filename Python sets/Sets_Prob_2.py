'''
This program contains my solution for the given problem in hackerrank
Problem -> https://www.hackerrank.com/challenges/no-idea/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin,stdout

def getInputs():
    return list(map(int, stdin.readline().strip().split()))

n,m = getInputs()
arr = getInputs()
set_A = set(getInputs())
set_B = set(getInputs())
setc = set()
happiness = 0
for item in arr:
    if item in set_A:
        happiness += 1
    if item in set_B:
        happiness -= 1
print(happiness)