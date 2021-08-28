


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class binaryTree():
    def __init__(self):
        self.root = None

    def addChild(self, root,data):
        my_node = Node(data)
        if root == None:
            root = my_node
            return root
        else:
            cur = root
            while cur:
                if data<cur.data:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = my_node
                        break
                elif data > cur.data:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = my_node
                        break
                else:
                    break
        return root

def printLeaves(root):
    cnt = 0
    if(root):
        
        cnt+= printLeaves(root.left)
         
        # Print it if it is a leaf node
        if root.left is None and root.right is None:
            print(root.data),
            cnt = 1
 
        cnt+=printLeaves(root.right)
    return cnt
 
# A function to print all left boundary nodes, except a
# leaf node. Print the nodes in TOP DOWN manner
def printBoundaryLeft(root):
    cnt = 0
    if(root):
        
        if (root.left):
             
            # to ensure top down order, print the node
            # before calling itself for left subtree
            print(root.data)
            cnt =1
            cnt+= printBoundaryLeft(root.left)

        elif(root.right):
            print (root.data)
            cnt =1
            cnt+= printBoundaryLeft(root.right)
    return cnt
        # do nothing if it is a leaf node, this way we
        # avoid duplicates in output
 
 
# A function to print all right boundary nodes, except
# a leaf node. Print the nodes in BOTTOM UP manner
def printBoundaryRight(root):
    cnt = 0
    if(root):
        
        if (root.right):
            cnt =1
            # to ensure bottom up order, first call for
            # right subtree, then print this node
            cnt += printBoundaryRight(root.right)
            print(root.data)
            
         
        elif(root.left):
            cnt =1
            cnt += printBoundaryRight(root.left)
            print(root.data)
            
    return cnt
        # do nothing if it is a leaf node, this way we
        # avoid duplicates in output
 
 
# A function to do boundary traversal of a given binary tree
def printBoundary(root):
    cnt = 1
    if (root):
        print(root.data)
         
        # Print the left boundary in top-down manner
        cnt += printBoundaryLeft(root.left)
 
        # Print all leaf nodes
        cnt+= printLeaves(root.left)
        cnt += printLeaves(root.right)
 
        # Print the right boundary in bottom-up manner
        cnt += printBoundaryRight(root.right)
    return cnt

def levelOrder(root):
    cur = root
    q = [root]
    while q:
        cur = q[0]
        print(cur.data, end=' ')
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
        q.pop(0)
    

if __name__ =="__main__":
    tree = binaryTree()
    root = tree.addChild(tree.root,20)
    root = tree.addChild(root,8)
    root = tree.addChild(root, 4)
    root = tree.addChild(root, 12)
    root = tree.addChild(root, 10)
    root = tree.addChild(root, 14)
    root = tree.addChild(root, 22)
    root = tree.addChild(root, 25)


    levelOrder(root)
    print()
    print('Count of outer nodes:',(printBoundary(root)))



