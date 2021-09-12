#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        no = 0
        multi = 1
        nstr = string
        if string[0]=='-':
            nstr = string[1:]
        
        for i in nstr[::-1]:
            
            if i.isalpha() or i == '-':
                return -1
            no = no + int(i)*multi
            multi *= 10
            
        if string[0] == '-':
            no = 0 -no
        return no
        # Code here

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends