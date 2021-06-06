'''
Problem-statement -> https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
'''
from sys import stdin
from collections import namedtuple
N = int(input())
my_record = namedtuple('student_record',stdin.readline())
sum_marks = 0
for i in range(N):
    std = my_record(*stdin.readline().split())
    sum_marks += int(std.MARKS)
print('{:.2f}'.format(sum_marks/N))