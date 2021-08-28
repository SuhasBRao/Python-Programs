#User function Template for python3
class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        #CODE HERE
        mystack = self.s
        if mystack == []:
            mystack.append(x)
            self.minEle = x
        else:
            if x >= self.minEle:
                mystack.append(x)
            if x < self.minEle:
                mystack.append( 2*x - self.minEle)
                self.minEle = x

    def pop(self):
        #CODE HERE
        mystack = self.s
        if mystack== []:
            return -1
        else:
            if mystack[-1] >= self.minEle:
                val = mystack.pop()
                
                
            if mystack[-1] < self.minEle:
                val = mystack.pop()
                self.minEle = 2*self.minEle - val
                val = (val + self.minEle)//2
            return val
        

    def getMin(self):
        #CODE HERE
        if self.s == []: return -1
        else: return self.minEle

#{ 
#  Driver Code Starts
#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

# } Driver Code Ends