'''
Problem-statement --> https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
'''
import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node):
    while node:
        
        if node:
            #fptr.write(sep)
            print(node.data)
        node = node.next
        
       
        

        
# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    ptr1,ptr2 = head1,head2
    new_list = SinglyLinkedList()
    while True:
        if ptr1.data <= ptr2.data:
            #print(ptr1.data)
            new_list.insert_node(ptr1.data)
            ptr1 = ptr1.next
            if ptr1 == None:
                while ptr2 != None:
                    new_list.insert_node(ptr2.data)
                    ptr2 = ptr2.next
                break
        else:
            new_list.insert_node(ptr2.data)
            ptr2 = ptr2.next
            if ptr2 == None:
                while ptr1 != None:
                    new_list.insert_node(ptr1.data)
                    ptr1 = ptr1.next
                break
    print('##################')
    print_singly_linked_list(new_list.head)



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        mergeLists(llist1.head, llist2.head)
        #llist3 = mergeLists(llist1.head, llist2.head)

        #print_singly_linked_list(llist2.head)
    