#User function Template for python3


# m is maximum of number zeroes allowed 
# to flip, n is size of array 
def findZeroes(arr, n, m) :
    # code here
    max_l = 0
    si , ei = 0,n-1
    no_zeros = 0
    prev_si = 0
    while si<=ei:
        while no_zeros < m and si<=ei:
            #print(si)
            if arr[si] == 0: no_zeros += 1
            #print(si)
            si += 1
            
        #print(si)
        #si-=1
        max_l = max(si - prev_si, max_l)
        #print(max_l)
        prev_si = si-1
        no_zeros = 0

    return max_l

#{ 
#  Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends