'''
This program reverses a given singly linked list using python.
'''

def reverseLinkedList(alinkedlist):
    previousNode = None
    nextNode = None
    currentNode = alinkedlist.headOfList

    while currentNode != None:
        nextNode = currentNode.nextElement
        currentNode.nextElement = previousNode
        previousNode = currentNode
        currentNode = nextNode
        
    alinkedlist.headOfList = previousNode

# {
# Driver Code starts
if __name__ == "__main__":
    # write your code here
    import SinglyLinkedList                     # make sure you have SinglyLinkedList.py in same directory
    from sys import stdin
    
    alinkedlist = SinglyLinkedList.linkedList()
    print("Enter elements of linked list : ")
    
    elementsOfLinkedList = list(map(int, stdin.readline().strip().split()))
    
    alinkedlist.insertMutipleElementsAtEnd(elementsOfLinkedList)
    print('Before reversing : ',end = '') 
    alinkedlist.showLinkedList()
    
    reverseLinkedList(alinkedlist)
    
    
    print('After reversing : ',end = '')
    alinkedlist.showLinkedList()

# } Driver Code ends