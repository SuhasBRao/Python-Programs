def transitionPoint(arr, n):
    #Code here
    l = 0 
    r = n-1
    #print(bS(arr,l,r))
    st = list(set(arr))
    if st[0] == 1:
        return 0
    else:
        return bS(arr,l,r)
    pass
   
    
def bS(arr,l,r):
    
    while l<=r:
        mid = int((l+r)//2)
        if arr[mid] == 0:
            l = mid -1
        elif (mid == 0 or (mid > 0 and arr[mid - 1] == 0)):
            return mid
        r = mid -1
    return -1 

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