'''
The program implements binary tree in python.

'''
class treeNode:

    def __init__(self, data):
        self.data = data 
        self.leftChild = None
        self.rightChild = None
        self.parent= None

    def addChild(self,node):
        if node.data == self.data:
            return 
        
        if node.data < self.data:
        
            if self.leftChild:
                self.leftChild.addChild(node)
            else:
                self.leftChild = node
                node.parent = self
   
        if node.data > self.data:
            
            if self.rightChild:
                
                self.rightChild.addChild(node)
            else:
                self.rightChild = node
                node.parent = self
            
    def findMin(self):
        
        if self.leftChild is None:
            return self.data
        
        return self.leftChild.find_min()

    def findMax(self):
        if self.rightChild is None:
            return self.data
        
        return self.rightChild.find_max()

        
    def getLevel(self):
        # this function gets the level of a node in a tree
        level = 0
        if self.parent:
            p = self.parent
            while p != None:
                level += 1
                p = p.parent
        
        return level
    
    # We will implement in-order traversal
    def inOrderTraverse(self):
        idnt =  '' if not self.parent else  '   '*self.getlevel() + '|---->'
        
        if self.leftChild:
            #print(self.left)
            
                #print(child.data)
            self.left.inOrderTraverse()
        
        
        #if self.data == 18:
        #    print('###########')
        #    print(self.parent.data)
        #    print('###########')
        
        print(idnt + str(self.data))
        
        if self.rightChild:
            #print(self.right)
            
            self.rightChild.inOrderTraverse()
       

if __name__ == '__main__':
    root = treeNode(5)

    child1 = treeNode(2)
    child2 = treeNode(19)

    root.addChild(child1)
    root.addChild(child2)
    

    root.addChild(treeNode(-4))
    root.addChild(treeNode(3))
  
    root.addChild(treeNode(9))
    root.addChild(treeNode(21))
    root.addChild(treeNode(18))
    root.addChild(treeNode(10))
    
    root.addChild(treeNode(25))
    
    
    root.inOrderTraverse()
    print(child2.left.find_min())
   