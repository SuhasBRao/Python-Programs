'''
This program contains solution for the below hackkerank problem.
Problem -> https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
'''
n = int(input())
s = set(map(int, input().split()))
op = int(input())

for i in range(op):
    query = input().strip().split()
    
    if len(query) == 1:
        s.pop()
    if len(query) > 1:
        query, val = query
        #print(query)
        if query == 'remove':
            s.remove(int(val))
        if query == 'discard':
            s.discard(int(val))

print(sum(s))