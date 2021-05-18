'''
This program contains solution for the given hackkerank problem
Problem -> https://www.hackerrank.com/challenges/py-set-add/problem
'''

N = int(input())
name_stamp = set()
for _ in range(N):
    country = input()
    name_stamp.add(country)
print(len(name_stamp))