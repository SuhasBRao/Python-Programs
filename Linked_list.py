'''
This program implements a singly linked list using Python language.
'''
class Node:
    def __init__(self, data = None,next = None):
        self.data = data
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beg(self,data):
        temp_node = Node(data)
        temp_node.next = self.head
        self.head = temp_node
    
    def insert_at_end(self,data):
        temp_node = Node(data)
        ptr = self.head
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = temp_node


    def display_list(self):
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

if __name__ == '__main__':
    mylist = linkedList()   # create an instance of the class

    mylist.insert_at_beg(5) # insert 5 at beginning
    mylist.insert_at_beg(89)  # insert 89 at beginning
    mylist.display_list()
    mylist.insert_at_end(0) # insert 0 at end
    
    mylist.display_list()