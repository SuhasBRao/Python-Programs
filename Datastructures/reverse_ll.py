'''
This program reverses a given singly linked list using python.
'''
import Linked_list                      # make sure you have Linked_list.py in same directory
singly_ll = Linked_list.linkedList()
singly_ll.insert_at_end(5)
singly_ll.insert_at_end(8)
singly_ll.insert_at_end(3)
singly_ll.insert_at_end(99)
print('Before reversing : ',end = '') 
singly_ll.display_list()


prev = None
next = None
head = singly_ll.head

while head != None:
    next = head.next
    head.next = prev
    prev = head
    head = next

singly_ll.head = prev
print('After reversing : ',end = '')
singly_ll.display_list()
