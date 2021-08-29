#User function Template for python3

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def enqueue(self,X):
        # code here
        self.s1.append(X)
        
    def dequeue(self):
        # code here
        if len(self.s1) == 0 and len(self.s2) == 0:
            return -1
        
        elif len(self.s2) == 0 and len(self.s1)>0:
            while len(self.s1):
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        else:
            return self.s2.pop()
        
#{ 
#  Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        ob=Queue()
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                ob.enqueue(a[i+1])
                i+=1
            else:
                print(ob.dequeue(),end=" ")
            i+=1

        print()
# } Driver Code Ends