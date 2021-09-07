#User function Template for python3
class Solution:
     def zigZag(self,arr, n):
        for i in range(n-1):
            cur = arr[i]
            next = arr[i+1]
            
            if (i%2 == 0 and not (cur<next)) or (i%2 != 0 and not (cur>next)):
                arr[i], arr[i+1] = arr[i+1], arr[i]
            #elif i%2 != 0 and not (cur>next):
            #    arr[i], arr[i+1] = arr[i+1], arr[i]
            #    pass
                


#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.zigZag(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends