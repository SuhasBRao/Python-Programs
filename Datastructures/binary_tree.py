'''
The program implements binary tree in python.

'''
class treeNode:

    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
        self.parent= None

    def addChild(self,node):
        if node.data == self.data:
            return 
        
        if node.data < self.data:
        
            if self.left:
                self.left.addChild(node)
            else:
                self.left = node
                node.parent = self
   
        if node.data > self.data:
            
            if self.right:
                
                self.right.addChild(node)
            else:
                self.right = node
                node.parent = self
            
    def find_min(self):
        
        if self.left is None:
            return self.data
        
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        
        return self.right.find_max()

        
    def getlevel(self):
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
        
        if self.left:
            #print(self.left)
            
                #print(child.data)
            self.left.inOrderTraverse()
        
        
        #if self.data == 18:
        #    print('###########')
        #    print(self.parent.data)
        #    print('###########')
        
        print(idnt + str(self.data))
        
        if self.right:
            #print(self.right)
            
            self.right.inOrderTraverse()
       

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
   