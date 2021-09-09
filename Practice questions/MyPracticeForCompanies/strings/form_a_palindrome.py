#User function Template for python3

class Solution:
    def getCount(self,s,l,h):
        if l>h:
            return 0
        if l == h:
            return 0

        if s[l] == s[h]:
            return self.getCount(s,l+1, h-1)
        else:
            return min(self.getCount(s, l+1,h), self.getCount(s, l, h-1)) + 1
        
    def countMin(self, s):
        pass
        val = self.getCount(s,0, len(s)-1)
        return val
#{  
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()
        

        solObj = Solution()

        print(solObj.countMin(Str))
# } Driver Code Ends