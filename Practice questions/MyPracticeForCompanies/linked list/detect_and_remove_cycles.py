'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def remove(self,loop_node,head):
        if loop_node:
            ptr1 = loop_node
            ptr2 = loop_node
             
            # Count the number of nodes in loop
            k = 1
            while(ptr1.next != ptr2):
                ptr1 = ptr1.next
                k += 1
     
            # Fix one pointer to head
            ptr1 = head
             
            # And the other pointer to k nodes after head
            ptr2 = head
            for i in range(k):
                ptr2 = ptr2.next
     
            # Move both pointers at the same place
            # they will meet at loop starting node
            while(ptr2 != ptr1):
                ptr1 = ptr1.next
                ptr2 = ptr2.next
     
            # Get pointer to the last node
            while(ptr2.next != ptr1):
                ptr2 = ptr2.next
     
            # Set the next node of the loop ending node
            # to fix the loop
            ptr2.next = None
            
    
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        slow_ptr = head
        fast_ptr = head
        loop_node = None
        while (slow_ptr and fast_ptr and fast_ptr.next):
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if slow_ptr == fast_ptr:
                loop_node = slow_ptr
                break
        self.remove(loop_node,head)
        
        
            


#{ 
#  Driver Code Starts
# driver code:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,num):
        if self.head is None:
            self.head=Node(num)
            self.tail=self.head
        else:
            self.tail.next=Node(num)
            self.tail=self.tail.next
    
    def isLoop(self):
        if self.head is None:
            return False
        
        fast=self.head.next
        slow=self.head
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast=fast.next.next
            slow=slow.next
        
        return True
    
    def loopHere(self,position):
        if position==0:
            return
        
        walk=self.head
        for _ in range(1,position):
            walk=walk.next
        self.tail.next=walk
    
    def length(self):
        walk=self.head
        ret=0
        while walk:
            ret+=1
            walk=walk.next
        return ret

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=tuple(int(x) for x in input().split())
        pos=int(input())
        
        ll = linkedList()
        for i in arr:
            ll.add(i)
        ll.loopHere(pos)
        
        Solution().removeLoop(ll.head)
        
        if ll.isLoop() or ll.length()!=n:
            print(0)
            continue
        else:
            print(1)

# } Driver Code Ends