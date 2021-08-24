"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def rev(self, head):
        if head == None:
            return None
        cur = head
        next = None
        prev = None
        while cur.next:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        cur.next = prev
        #printList(cur)
        return cur

    def reverse(self,head, k):
        ptr1 = head
        ptr2 = head
        val = k
        new = None
        while ptr1 and ptr2:
            while k>1 and ptr1.next:
                ptr1 = ptr1.next
                k -= 1
            new_head = ptr1.next
            ptr1.next = None
            
            rev = self.rev(ptr2)
            if new == None: new = rev
            else:
                ptr1 = new
                while ptr1.next:
                    ptr1 = ptr1.next
                ptr1.next = rev
            
            ptr2 = new_head
            ptr1 = new_head
            k = val

        return new
            

        # Code here
        pass

#{ 
#  Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        printList(llist.head)
        t -= 1




# } Driver Code Ends