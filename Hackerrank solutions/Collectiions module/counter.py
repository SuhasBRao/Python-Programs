'''
Problem statement -> https://www.hackerrank.com/challenges/collections-counter/problem
'''
from collections import Counter
from sys import stdin

def getInputs():
    return list(map(int, stdin.readline().strip().split()))

no_shoes = int(input())
shoe_sizes = getInputs()
no_customers = int(input())

shoe_sizes_counter = Counter(shoe_sizes)
amt_earned = 0

for _ in range(no_customers):
    size, price = getInputs()
    if size in shoe_sizes_counter:
        amt_earned += price

        shoe_sizes_counter[size] -= 1
        if shoe_sizes_counter[size] == 0:
            del shoe_sizes_counter[size]
            
print(amt_earned)