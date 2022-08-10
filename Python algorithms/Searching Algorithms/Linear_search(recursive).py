'''
This program implements linear search algorithm recursively.
'''
from sys import stdin
def getInputs():
    return list(map(int, stdin.readline().split()))

def linear_search(arr,key,indx):
    if indx == len(arr):
        return -1
    if arr[indx] == key:
        return True
    else:
        return linear_search(arr,key,indx + 1)
    
arr = getInputs()
key = int(input('Enter a key to search: '))

print(linear_search(arr,key,0))