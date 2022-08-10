'''
A simple python program to reverse a given input array (without using inbuilt function)
'''
from sys import stdin,stdout

def get_array():
    return list(map(int, stdin.readline().strip().split()))

arr = get_array()
start = 0
end = len(arr) - 1

while start < end:
    arr[start], arr[end] = arr[end],arr[start]
    start += 1
    end -= 1 

print(arr)