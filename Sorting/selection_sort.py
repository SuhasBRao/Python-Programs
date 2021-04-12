'''
This program implements a selection sort technique to sort
an array of size n.
In an ith iteration with ith element as the smalles,
the algorithm finds the smallest element in 
i+1 to n, and swaps the position.

'''
from sys import stdin,stdout
def getInts():
    return list(map(int,stdin.readline().strip().split()))
arr = getInts()

for i in range(len(arr) - 1):
    curr_indx = i
    small_ele = min(arr[i:])    # finds the minimum in i+1 to n.

    if small_ele < arr[curr_indx]:
        small_indx = arr.index(small_ele)
        arr[small_indx],arr[curr_indx] = arr[curr_indx],arr[small_indx]

print('--------------------------')
print('Sorted array : {}'.format(arr))

        