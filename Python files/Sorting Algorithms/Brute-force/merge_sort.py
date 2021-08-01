'''
This program implements merge sort algorithm (recursive)
'''
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left_sub_array = mergeSort(arr[:mid])
    right_sub_array = mergeSort(arr[mid:])
    
    i,j,k = [0]*3
    arr= []
    while i<len(left_sub_array) and j< len(right_sub_array):
        if left_sub_array[i] < right_sub_array[j]:
            arr.append(left_sub_array[i])
            i += 1
        else:
            arr.append(right_sub_array[j])
            j += 1
    
    while j<len(right_sub_array):
        arr.append(right_sub_array[j])
        j+=1
    while i<len(left_sub_array):
        arr.append(left_sub_array[i])
        i+=1
    
    return arr

if __name__ == "__main__":
    
    arr = list(map(int,input().split()))
    print(mergeSort(arr))