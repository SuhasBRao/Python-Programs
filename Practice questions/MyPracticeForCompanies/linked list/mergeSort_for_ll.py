#User function Template for python3

'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''
from sys import platform


class Solution:
    #Function to sort the given linked list using Merge Sort.
    def merge(self,head1,head2):
        merged = Node(-1)
        
        temp = merged
        # While head1 is not null and head2
        # is not null
        while (head1 != None and head2 != None):
            if (head1.data < head2.data):
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next
        
        # While head1 is not null
        while (head1 != None):
            temp.next = head1
            head1 = head1.next
            temp = temp.next
        
        # While head2 is not null
        while (head2 != None):
            temp.next = head2
            head2 = head2.next
            temp = temp.next
     
        return merged.next
    
    def getMiddle(self,head):
        
        slow = head
        fast = head.next
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeSort(self, head):
        if head.next == None or head == None:
            return head
        
        mid = self.getMiddle(head)
        nexttomiddle = mid.next
        
        mid.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(nexttomiddle)
        
        fhead = self.merge(left,right)
        return fhead

        

        
        

#{ 
#  Driver Code Starts
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends