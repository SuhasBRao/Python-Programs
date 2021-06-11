# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Problem -> https://www.hackerrank.com/challenges/py-collections-deque/problem
'''
from collections import deque
from sys import stdin
my_deque = deque()
N = int(input())
for _ in range(N):
    inpts = stdin.readline().strip().split()
    op = inpts[0]
    if len(inpts) > 1:
        val = inpts[1]

    if op == 'append':
         my_deque.append(val)
    elif op == 'appendleft':
        my_deque.appendleft(val)

    elif op=='pop':
        my_deque.pop()
    elif op=='popleft':
        my_deque.popleft()
    
print(*my_deque)