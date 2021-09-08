#User function Template for python3
class Solution:
    def removeDups(self, S):
        hash = set(S)
        #print(hash)
        for val in hash:

            #print(pos)
            
            if S.count(val) >1:
                pos = S.index(val)
                #print(S[pos+1:])
                S = S[:pos] + val + S[pos + 1:].replace(val,'',(S.count(val) - 1))
            #print(S) 
        return S 
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer)


# } Driver Code Ends