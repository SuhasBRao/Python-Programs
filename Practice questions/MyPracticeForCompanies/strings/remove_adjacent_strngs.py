#User function Template for python3

class Solution:
    def remove (self, S):
		#code here
        si = 0
        ei = 1
        while ei<len(S):
            while ei<len(S) and S[ei] == S[si]:
                ei +=1
            if ei-si>1:
                S = S.replace(S[si:ei], '?'*(ei - si))
            
            si =ei
            ei = si+1
            #print(S)
        S= S.replace('?','')
        return S
		       
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.remove(S))


# } Driver Code Ends