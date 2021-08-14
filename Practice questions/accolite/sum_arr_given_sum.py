#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    
    def subArraySum(self,arr, n, s): 
        si,ei = 0, 1
        cur_sum = arr[si]
       #Write your code here
        while ei<=n-1:
            while cur_sum <s and ei <=n-1:
                cur_sum += arr[ei]
                ei += 1
            while cur_sum >s and si<ei :
                cur_sum -= arr[si]
                si += 1
            if cur_sum == s:
                break
        return [si+1,ei] if cur_sum == s else [-1] 



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends