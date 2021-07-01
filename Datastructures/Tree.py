'''
The below program implements tree datstructure in python using a class.
'''
class treeNode:
    # class that defines A General tree and performs prints the tree.
    def __init__(self,data, designation):
        # asks for name and designation of the employee
        self.data = data
        self.designation = designation
        self.child = []
        self.parent = None
    
    def addChild(self,child):
        # this function adds child and sets the current node as parent for the child
        self.child.append(child)
        child.parent = self

    def getlevel(self):
        # this function gets the level of a node in a tree
        level = 0
        if self.parent:
            p = self.parent
            while p != None:
                level += 1
                p = p.parent
        
        return level

    def showTree(self, req):
        # This function displayes the tree according to the user input.
        # REMARK: checkout CODEBASICS tutorial on youtube for problem statement
        idnt =  '' if not self.parent else  '  '*self.getlevel() + '|-->'
        
        if req == 'name':
            print(idnt + self.data)
        elif req =='designation':
            print(idnt + self.designation)
        elif req == 'both':
            print(f'{idnt} {self.data}  {(self.designation)}')

        for children in self.child:
            
            children.showTree(req)

if __name__ == '__main__':
    # Main part of the program
    root = treeNode('1','CEO')
    
    two = treeNode('2','CTO')
    two.addChild(treeNode('4','Manageer'))
    two.addChild(treeNode('6','Manager'))

    three = treeNode('3','HR head')
    three.addChild(treeNode('6','HR manager'))
    three.addChild(treeNode('9','Policy Manager'))


    root.addChild(two)
    root.addChild(three)


    root.showTree('designation')
