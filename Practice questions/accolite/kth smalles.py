def quicksort(arr):
    if arr == []:return []
    if len(arr) == 1:
        return arr
    if len(arr) > 1:
        pivot = arr[0]
        la = [x for x in arr if x<pivot]
        ra = [x for x in arr if x>pivot]
        return quicksort(la)+[pivot] + quicksort(ra)

arr = [ 5,4,3,2,1]
print(quicksort(arr))