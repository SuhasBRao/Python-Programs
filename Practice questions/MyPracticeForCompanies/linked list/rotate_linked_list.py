# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    

    def rotate(self, head, k):
        # code here
        kth_node = None
        new_head = None
        ptr = head
        while k>1:
            ptr = ptr.next
            k-=1
            
        if ptr ==  None:
            new_head = head
            return new_head
         
        kth_node = ptr
        new_head = kth_node.next
        kth_node.next = None
        
        ptr = new_head
        if ptr == None:
            return head
            
        while ptr.next:
            ptr = ptr.next
        ptr.next = head

        return new_head

#{ 
#  Driver Code Starts
# driver

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = Solution().rotate(lis.head,k)
        printList(head)
# } Driver Code Ends