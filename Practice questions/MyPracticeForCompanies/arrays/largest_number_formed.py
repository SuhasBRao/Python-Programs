#User function Template for python3
class Solution:
    
    def printLargest(self,l):
        from itertools import permutations
	    # code here
        lst = []
        for i in permutations(l, len(l)):
            # provides all permutations of the list values,
            # store them in list to find max
            lst.append("".join(map(str,i)))
        return max(lst)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends