#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def reverse(self, head):
        cur = head
        prev = None
        next = None
        while cur.next:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        cur.next = prev
        return cur

    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        nw_head = LinkedList()
        carry =0
        first_rev = self.reverse(first)
        second_rev = self.reverse(second)
        ptr1 = first_rev
        ptr2 = second_rev

        head = nw_head
        while ptr1 and ptr2:
            sum = ptr1.data + ptr2.data + carry
            carry = int(sum/10)
            
            head.insert(sum%10)

            ptr1 = ptr1.next
            ptr2 = ptr2.next
        while ptr1:
            val = ptr1.data + carry
            carry = int(val/10)
            head.insert(val%10)
            
            ptr1 = ptr1.next
        
        
        while ptr2:
            val = ptr2.data + carry
            carry = int(val/10)
            head.insert(val%10)
            
            ptr2 = ptr2.next
            
        if carry >0:
            head.insert(carry)
        
        nw_head = self.reverse(nw_head.head)
        #printList(nw_head)
        return nw_head

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends