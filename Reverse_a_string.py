'''
A simple python program to reverse a given input array
'''
from sys import stdin,stdout

def get_array():
    return list(map(int, stdin.readline().strip().split()))

arr = get_array()
print(arr[::-1])