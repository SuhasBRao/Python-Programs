def sort012(arr,n):
    a = arr
    lo = 0
    hi = n - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return arr

arr = list(map(int,input().split()))
print(sort012(arr,len(arr)))
        
