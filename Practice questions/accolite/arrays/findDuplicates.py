
class Solution:
    
    def duplicates(self, arr, n):
        for i in range(len(arr)):
            #print(arr[i]%n)
            arr[arr[i]%n] += n 
        nw = []
    	# code here
        for i in range(0, n):
            #print(arr[i]/n)
            if (arr[i]/n) >= 2:
                nw.append(i)
        return nw if nw else [-1]
    	    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends