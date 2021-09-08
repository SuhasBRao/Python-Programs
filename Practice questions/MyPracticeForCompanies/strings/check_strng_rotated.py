#User function Template for python3


class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        
        if ( str1 == str2 and len(str1)>2  ) or ( len(str1)!=len(str2) ):
            return 0
        
        ns1 = str1[2:] + str1[:2]
        ns2 = str1[-2::1] + str1[:-2]
        
        return str2==ns1 or str2 == ns2
        #print(ns1, ns2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        if(Solution().isRotated(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends