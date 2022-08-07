'''
This program implements a singly linked list using Python language.
'''
class Node:
    def __init__(self, data = None,next = None):
        self.data = data
        self.nextElement = next

class linkedList:
    
    def __init__(self):
        self.headOfList = None
    
    def insertAtStart(self,data):
        nodeToBeInserted = Node(data)
        nodeToBeInserted.nextElement = self.headOfList
        self.headOfList = nodeToBeInserted
        print("Done inserting. List Updated!")
        
        
    def insertAtEnd(self,data):
        nodeToBeInserted = Node(data)
        currentNode = self.headOfList
        
        if currentNode == None:
            self.headOfList = nodeToBeInserted
        else:
            while currentNode.nextElement != None:
                currentNode = currentNode.nextElement
                
            currentNode.nextElement = nodeToBeInserted
        print("Done inserting. List Updated!")
        
    
    def insertMutipleElementsAtEnd(self, values : list):
        # inserts multiple values at the same time
        for item in values:
            self.insertAtEnd(item)
        print("Done inserting. List Updated!")
        
        
    def lengthOfList(self):
        # prints the lenght of the linkedlist
        numberOfElements = 0
        currentNode = self.headOfList
        while currentNode != None:
            numberOfElements += 1
            currentNode = currentNode.nextElement 
        return numberOfElements
    

    def insertDataAt(self,data, index):
        # The function is used to insert node at a specified index
        nodeToBeInserted = Node(data)
        pointerToElementJustBefore = self.headOfList
        if index == 0:
            # nodeToBeInserted.next = self.headOfList
            # self.headOfList = nodeToBeInserted
            self.insertAtStart(data)
        else:
            # else the ptr is made to traverse upto the postion just before the 
            # entered postition and then the nodes are attached
            while index > 1 and pointerToElementJustBefore.nextElement != None:    
                pointerToElementJustBefore = pointerToElementJustBefore.nextElement
                index -= 1
                
            nodeToBeInserted.nextElement = pointerToElementJustBefore.nextElement
            pointerToElementJustBefore.nextElement = nodeToBeInserted
        
        print("Done inserting. List Updated!")
        

    def removeElementAt(self,index):
        
        if index < 0 or index > self.lengthOfList():
            print('Invalid index!')
            return
        if index == 0:
            # To remove element at index 0 means to remove head of list
            # we simply change the head of list to point to the next element
            self.headOfList = self.headOfList.nextElement
            return
        
        currentPosition = 0
        currentNode = self.headOfList
        while currentNode != None:
            currentNode = currentNode.nextElement
            currentPosition += 1
            if currentPosition == index - 1:
                currentNode.nextElement = currentNode.nextElement.nextElement
                break
        print("Element Removed at index " + str(index))
    
    def isDataPresent(self, val):
        # method to check whether element is present in ll
        currentNode = self.headOfList
        countTheOccurence = 0
        while currentNode != None:
            if currentNode.data == val:
                countTheOccurence += 1
                break
            currentNode = currentNode.nextElement
        return True if countTheOccurence>=1 else False

    def insertValueAfterData(self,data,val):
        
        nodeToBeInserted = Node(val)
        currentNode = self.headOfList
        if self.isDataPresent(data):
            print('present')
            while currentNode != None:
                if currentNode.data == data:
                    break
                currentNode = currentNode.nextElement

            nodeToBeInserted.nextElement = currentNode.nextElement
            currentNode.nextElement = nodeToBeInserted
        else:
            while currentNode.nextElement != None:
                currentNode = currentNode.nextElement

            nodeToBeInserted.nextElement = currentNode.nextElement
            currentNode.nextElement = nodeToBeInserted
        print("Done inserting. List Updated!")
        
    def showLinkedList(self):
        # Funtion is used to display the singly linked list created
        if self.headOfList == None:
            print('List is empty!')
            return
        else:
            currentNode = self.headOfList
            while currentNode != None:
                print(f'({currentNode.data})-->',end = '')
                currentNode = currentNode.nextElement
            print()
            return

# Alter the below segments to create a linked list with required data field
if __name__ == '__main__':
    mylist = linkedList()   # create an instance of the class
    print(mylist.__doc__)

    mylist.insertAtEnd(5)
    mylist.insertAtStart(8)
    mylist.insertAtStart(10)

    print(mylist.isDataPresent(12))

    mylist.showLinkedList()

    mylist.insertValueAfterData(5, 0)
    mylist.showLinkedList()
    
    mylist.insertMutipleElementsAtEnd([4,3,2])
    
    mylist.showLinkedList()
    
    mylist.insertDataAt(9, 5)
    mylist.showLinkedList()
    
    mylist.removeElementAt(mylist.lengthOfList() - 1)
    mylist.showLinkedList()
