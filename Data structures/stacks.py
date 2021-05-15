'''
This program implements stack datastructure using collections.deque
'''
from collections import deque

class Stack:
    "Creates a stack using collections.deque"
    def __init__(self) -> None:
        self.mystorage = deque()
    
    def push(self, data):
        # inserts element at the end of the stack
        return self.mystorage.append(data)
    
    def pop(self):
        # removes top element of the stack
        return self.mystorage.pop()
    
    def peek(self):
        # returns top element of the stack
        return self.mystorage[-1]
    
    def __len__(self):
        # returns the len of the stack
        return len(self.mystorage)

    def isEmpty(self):
        # returns true if stack is empty else false
        return True if self.mystorage.__len__() == 0 else False

    def display(self):
        print(self.mystorage)

if __name__ == '__main__':
    mystack = Stack()
    mystack.push(5)
    mystack.push(9)
    mystack.display()
    mystack.pop()
    print(len(mystack))
    mystack.pop()

    print(mystack.isEmpty())
    print(mystack.__doc__)