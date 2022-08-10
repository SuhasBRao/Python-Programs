'''
This program searches for a given key in an integer array with size n.
This uses a linear search algorithm.
'''
from sys import stdin
def getInputs():
    return list(map(int, stdin.readline().strip().split()))

def linear_search(arr,key):
    for item in arr:
        if item == key:
            return True
    return -1

arr = getInputs()
key = int(input('Enter a key to search: '))

res = linear_search(arr,key)
if res == True:
    print('The element is present.')
if res == -1:
    print('Element not present.')