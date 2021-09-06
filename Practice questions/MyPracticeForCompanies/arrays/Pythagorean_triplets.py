#User function Template for python3
class Solution:
    sqrd_arr = []
    res = []
    def isPythagoreanTriplet(self, target):
        myhash = set()
        
        for ele in self.sqrd_arr:
            dif = target - ele
            if dif in myhash:
                return True
            myhash.add(ele)
        return False
    
    def checkTriplet(self,arr, n):
    	# code here
        sqr = lambda x: x**2
        self.sqrd_arr = list(map(sqr, arr))
        
        for ele in arr:
            is_it = self.isPythagoreanTriplet(ele**2)
            self.res.append(is_it)
            if any(self.res):
                return any(self.res)
        
        return False
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends