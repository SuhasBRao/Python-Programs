#User function Template for python3
class Solution:
    
    def segregateEvenOdd(self,arr, n):
		# code here
        l,r = 0, n-1
        
        while l<r:
            while l<r and (arr[l]%2 == 0):
                l+=1
            while l<r and (arr[r]%2 != 0):
                r-=1
            if l<r:
                if arr[l]%2!=0 and arr[r]%2 ==0:
                    arr[l],arr[r] = arr[r],arr[l]
                    l+=1
                    r-=1
                    
        arr = sorted(arr[:l]) + sorted(arr[l:])        
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        arr =ob.segregateEvenOdd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
