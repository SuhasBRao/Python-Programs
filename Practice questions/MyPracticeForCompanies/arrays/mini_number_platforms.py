#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        times = []
        for i in range(n):
            times.append([dep[i], 'd'])
            times.append([arr[i], 'a'])
        
        times = sorted(times, key = lambda x: x[1])
        #print(times)
        times = sorted(times, key = lambda x: x[0])
        #print(times)
        
        result, platforms = 0,0
        for i in range(2*n):
            if times[i][1] == 'a':
                platforms +=1
                result = max(result,platforms)
            else:
                platforms -=1
        return result
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends