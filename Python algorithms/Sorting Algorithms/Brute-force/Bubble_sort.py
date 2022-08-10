'''
This program implements bubble sort algorithm to sort
an array of size n.
'''
from sys import stdin

def getInputs():
    return list(map(int, stdin.readline().strip().split()))

def bubble_sort(alist):
    # The function returns a sorted list by taking unsorted list as input
    size = len(alist)
    
    for i in range(size - 1):
        
        for j in range(size - 1 - i ):
            
            if alist[j + 1] < alist[j]:
                alist[j+1],alist[j] = alist[j],alist[j+1]
    
    return alist
        
# {
# Driver Code starts
if __name__ == "__main__":
    # write your code here
    
    unsorted_list = getInputs()
    sorted_list = bubble_sort(unsorted_list)
    print(f'final sorted array : {sorted_list}')

# } Driver Code ends

