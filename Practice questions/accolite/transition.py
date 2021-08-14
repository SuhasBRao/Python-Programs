def transitionPoint(arr, n):
    #Code here
    i = 0
    pnt = -1
    st = set(arr)
    if len(st) ==1 and list(st)[0] == 1: 
        return 0
    while i<n:
        if arr[i] == 1:
            pnt = i
            break
        i+= 1
    return pnt

#{ 
#  Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends