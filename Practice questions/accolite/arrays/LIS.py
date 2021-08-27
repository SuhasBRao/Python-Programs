def lis(arr):
    n = len(arr)
    lis = [1]*n

    for i in range(1, n):
        for j in range(0,i):
            if arr[i]>arr[j] and lis[i] < lis[j] + 1:
                lis[i] =  lis[j] + 1
    return max(lis)
    pass


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        maximum_lis = lis(arr)

        print(maximum_lis)