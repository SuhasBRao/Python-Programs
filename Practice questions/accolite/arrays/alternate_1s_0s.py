arr = list(map(int, input().split()))
def alternate(arr):
    for i in range(len(arr) - 1):
        cur = arr[i]
        next = 0 if cur else 1
        j = i+1
        while j<len(arr) - 1 and arr[j] != next:
            j += 1
        arr[j], arr[i+1] = arr[i+1], arr[j]
    print(*arr)

alternate(arr)