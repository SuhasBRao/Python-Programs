#User function Template for python3
class Solution:
    def isprime(self,n):
        if n<=1:
            return False
        for i in range(2,int(n**0.5)):
            if n%i ==0:
                return False
        return True
        
    def segregatePrimeandNonprime(self,arr, n):
		# code here
        l,r = 0, n-1
        #print(self.isprime(2))
        while l<r:
            while l<r and (self.isprime(arr[l])):
                l +=1
            while l<r and (not self.isprime(arr[r])):
                r-=1
            if l<r:
                if self.isprime(arr[r]) and (not self.isprime(arr[l])):
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
        arr =ob.segregatePrimeandNonprime(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
