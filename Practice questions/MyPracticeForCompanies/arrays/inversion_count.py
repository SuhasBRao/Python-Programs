class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    inv_cnt = 0

    def merge_Sort(self,arr):
        if len(arr) == 1:
            return arr
        mid = len(arr)//2
        left_sub_array = self.merge_Sort(arr[:mid])
        right_sub_array = self.merge_Sort(arr[mid:])
        
        i,j,k = [0]*3
        nw= []
        while i<len(left_sub_array) and j< len(right_sub_array):
            if left_sub_array[i] <= right_sub_array[j]:
                nw.append(left_sub_array[i])
                i += 1
            else:
                self.inv_cnt += mid - i
                nw.append(right_sub_array[j])
                j += 1
        
        while j<len(right_sub_array):
            nw.append(right_sub_array[j])
            j+=1
        while i<len(left_sub_array):
            nw.append(left_sub_array[i])
            i+=1
        
        return nw

    def inversionCount(self, arr, n):
        # Your Code Here
        sorted = self.merge_Sort(arr)
        
        return self.inv_cnt

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends