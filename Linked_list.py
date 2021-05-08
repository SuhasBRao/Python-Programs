'''
This program implements a singly linked list using Python language.
'''
class Node:
    # This class creates a node with data and a link field
    def __init__(self, data = None,next = None):
        self.data = data
        self.next = next

class linkedList:
    # This class creates a singly linked list with certain methods
    def __init__(self):
        self.head = None
    
    def insert_at_beg(self,data):
        # This function is used to insert node at the beginning of the linked list
        temp_node = Node(data)
        temp_node.next = self.head
        self.head = temp_node
    
    def insert_at_end(self,data):
        # This function is used to insert node at the end of the singly linked list
        temp_node = Node(data)
        ptr = self.head
        if ptr == None:
            self.head = temp_node
        else:
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = temp_node

    def insert_values(self, values : [list]):
        # inserts multiple values at the same time
        for item in values:
            self.insert_at_end(item)
        
    def get_len(self):
        # prints the lenght of the linkedlist
        count = 0
        ptr = self.head
        while ptr:
            count += 1
            ptr = ptr.next 
        return count
    

    def insert_at_pos(self,pos,data):
        # The function is used to insert node at a specified position
        temp_node = Node(data)
        ptr = self.head
        if pos == 0:
            # if position entered is zero then the node created is directly 
            # attached to head node
            temp_node.next = self.head
            self.head = temp_node
        else:
            # else the ptr is made to traverse upto the postion just before the 
            # entered postition and then the nodes are attached
            while pos > 1 and ptr.next != None:
                ptr = ptr.next
                pos -= 1
            temp_node.next = ptr.next
            ptr.next = temp_node

    def remove_at(self,index):
        # removes the node at a particular position
        if index < 0 or index > self.get_len():
            print('Invalid index!')
            return
        if index == 0:
            self.head = self.head.next
            return
        pos = 0
        ptr = self.head
        while ptr:
            ptr = ptr.next
            pos += 1
            if pos == index - 1:
                ptr.next = ptr.next.next
                break
        
    def display_list(self):
        # Funtion is used to display the singly linked list created
        if self.head == None:
            print('List is empty!')
            return
        else:
            ptr = self.head
            while ptr != None:
                print(f'{ptr.data}-->',end = '')
                ptr = ptr.next
            print()
            return

# Alter the below segments to create a linked list with required data field
if __name__ == '__main__':
    mylist = linkedList()   # create an instance of the class
    
    mylist.insert_at_end(11)
    mylist.insert_at_beg(5) # insert 5 at beginning
    mylist.insert_at_beg(89)  # insert 89 at beginning

    mylist.insert_at_pos(99, 0)
    mylist.insert_values(['I','am','sUHAS','B','Rao'])
    mylist.display_list()
    mylist.remove_at(3)
    mylist.display_list()
    mylist.get_len()