#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,a, m, n): 
        # code here 
        k = 0
        l = 0
        res = []
        ''' k - starting row index
            m - ending row index
            l - starting column index
            n - ending column index
            i - iterator '''
        
        while (k < m and l < n):
    
            # Print the first row from
            # the remaining rows
            for i in range(l, n):
                #print(a[k][i], end=" ")
                res.append(a[k][i])
            k += 1
    
            # Print the last column from
            # the remaining columns
            for i in range(k, m):
                #print(a[i][n - 1], end=" ")
                res.append(a[i][n-1])
            n -= 1
    
            # Print the last row from
            # the remaining rows
            if (k < m):
    
                for i in range(n - 1, (l - 1), -1):
                    #print(a[m - 1][i], end=" ")
                    res.append(a[m-1][i])
                m -= 1
    
            # Print the first column from
            # the remaining columns
            if (l < n):
                for i in range(m - 1, k - 1, -1):
                    #print(a[i][l], end=" ")
                    res.append(a[i][l])
                l += 1

            #print(m,n,k,l)
            
            #print(res)
        return res
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends