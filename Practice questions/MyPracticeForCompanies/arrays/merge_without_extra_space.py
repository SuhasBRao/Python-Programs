#User function Template for python3
'''
The solution is yet to be improved

'''
class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        ptr1 = 0
        ptr2 = 0
        while ptr1<len(arr1):
            if arr1[ptr1] >= arr2[ptr2]:
                tmp = arr1[ptr1]
                
                arr1[ptr1] = arr2[ptr2]
                
                j = ptr2
                
                while arr2[j]<tmp and j < len(arr2)-1:
                    j+=1
                if j >= len(arr2)-1:
                    arr2.pop(0)
                    arr2.append(tmp)
                elif j == 0: arr2[j] = tmp
                else:
                    arr2.insert(j, tmp)
                    arr2.pop(ptr2)
                    #arr2[j-1] = tmp
                    
                
            ptr1 +=1
        #print(arr1, arr2)
                

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends