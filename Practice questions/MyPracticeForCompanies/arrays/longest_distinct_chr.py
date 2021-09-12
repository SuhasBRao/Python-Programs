#User function Template for python3

class Solution:

    def longestSubstrDistinctChars(self, S):
        max_cnt = 0
        si = 0
        i = 0
        n = len(S)
        while i<n:
            cnt1 = len(S[si:i+1])
            cnt2 = len(set(S[si:i+1]))

            if cnt1 == cnt2:
                max_cnt = max(max_cnt, cnt1)
            else:
                si +=1 
            
            i+=1
        return max_cnt
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends