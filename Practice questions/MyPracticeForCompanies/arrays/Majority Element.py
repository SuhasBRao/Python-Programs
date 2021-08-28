#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        A.sort()    # sorting the array makes similar elements adjacent to each other
        cnt =0
        prev = None
        major = None
        for i in A:
            if i == prev:
                cnt +=1
            else:
                cnt = 1
            if cnt > N/2:
                major = i
                break
            prev = i
        return major if major else -1
        #Your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends