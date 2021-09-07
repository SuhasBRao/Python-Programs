#User function Template for python3

class Solution:
    longest_string = ''

    def find_palindromes_in_sub_string(self, S, j, k):
        
        while j >= 0 and k < len(S):
            if S[j] != S[k]:
                self.longest_string = max( self.longest_string, S[j],key=len)
                break
            self.longest_string = max( self.longest_string, S[j:k+1], key=len)
           

            j -= 1
            k += 1

        


    
    def longestPalin(self, S):
        if len(S) == 1:
            return S
        for i in range(0, len(S)):
            self.find_palindromes_in_sub_string(S, i - 1, i + 1)
            self.find_palindromes_in_sub_string(S, i, i + 1)
        #print(count)
        return self.longest_string
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends