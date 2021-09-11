#User function Template for python3

class Solution:

    def longestCommonPrefix(self, arr, n):
        # code here
        arr.sort(key=len)
        i = 0 
        res = arr[0]
        #while i<len(arr[0]) and arr[0][i] == arr[-1][i]:
        #    res +=arr[0][i]
            
        #    i+=1
        
        for j in range(1, n-1):
            i = 0
            while i<len(arr[j]) and i < len(res) and arr[j][i] == res[i]:
                i+=1
            
            if i < len(res):
                res = res[:i]
            
        return res if res != '' else -1
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends