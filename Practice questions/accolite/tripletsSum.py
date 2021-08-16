
#User function Template for python3
class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.

    def findPairs(self,arr,x,ele):
		# code here
        s = set()
        for i in range(len(arr)):
            if arr[i] != ele:
                temp = x - arr[i]
                if temp in s:
                    return True
                s.add(arr[i])
        return False 

    def find3Numbers(self,A, n, X):
        isposible = []
        for ele in A:
            target = X - ele
            isposible.append(self.findPairs(A,target, ele))
            if any(isposible):
                return True
        return False
        
            
        # Your Code Here
        pass

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends