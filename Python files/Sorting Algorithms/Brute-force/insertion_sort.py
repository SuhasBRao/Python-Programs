# The program Implements insertion sort algorithm in python.

# Check out Insertion sort Description here -> (https://www.geeksforgeeks.org/insertion-sort/)
def checkFurther(i,key,arr):
    # recusrsive function that checks for smaller elements
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
        print()
        print('#####')
        
        key = arr[i]
        if key < arr[i -1]:
            arr = checkFurther(i-1,key,arr)
            
    

#arr = [4,3,2,10,12,1,5,6]
#arr = [7, 1, 3, 2, 4, 5, 6]
arr = [2,3,4,1,5]
insertionSort(arr)
