# The program Implements insertion sort algorithm in python.

# Check out Insertion sort Description here -> (https://www.geeksforgeeks.org/insertion-sort/)

from sys import stdin

def getInputs():
    return list(map(int, stdin.readline().split()))

def checkFurther(i,key,arr):
    # This checks if the key is smaller than the elements in sorted part of 
    # the list
    if i >= 0:
        if key < arr[i-1]:
            return checkFurther(i-1,key,arr)
        else:
            arr.remove(key)
            arr.insert(i,key)
    
    if i<0:
        arr.remove(key)
        arr.insert(0,key)

            
    return arr

def insertionSort(arr):
    
    for i in range(1,len(arr)):
        
        key = arr[i]
        if key < arr[i -1]:
            arr = checkFurther(i-1,key,arr)
            
    return arr

# {
# Driver Code starts
if __name__ == "__main__":
    # write your code here
    unsorted_list = getInputs()
    sorted_list = insertionSort(unsorted_list)
    print('Sorted array : {0}'.format(sorted_list))
# } Driver Code ends
