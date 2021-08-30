#User function Template for python3

class Solution:
    def goals(self,X, Y, Z):
        # code here
        s1, s2 = 0,0
        while Z>1:
            if X%Z == 0:
                X -=1
                s1 +=1
            elif Y%Z == 0:
                Y -=1
                s2 +=1
            else:
                Z -=1
            #print(X,Y,Z)
        return [s1,s2]
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X, Y, Z = [int(a) for a in input().split()]

        ob = Solution()
        c1, c2 = ob.goals(X, Y, Z)
        print(c1, end=" ")
        print(c2)
# } Driver Code Ends