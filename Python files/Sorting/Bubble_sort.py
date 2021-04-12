'''
This program implements bubble sort algorithm to sort
an array of size n.
'''
from sys import stdin, stdout
def getInts():
    return list(map(int, stdin.readline().strip().split()))

arr = getInts()

for i in range(len(arr) - 1):
    
    for j in range(len(arr) - 1 - i ):
        if arr[j + 1] < arr[j]:
            arr[j+1],arr[j] = arr[j],arr[j+1]
    


print(f'final sorted array : {arr}')