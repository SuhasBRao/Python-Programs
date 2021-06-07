
#Problem - statement -> https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
from collections import OrderedDict
from sys import stdin
N = int(input())
my_data = OrderedDict()
for _ in range(N):
    inpts = stdin.readline().strip().split()
    key, val = ' '.join(inpts[:-1]), int(inpts[-1])
    try:
        my_data[key] += val
    except:
        my_data[key] = val

for item in my_data.items():
    print(*item)
