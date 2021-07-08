class Node:
    def __init__(self,data):
        self.info = data
        self.right = None
        self.left = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
    
def topView(root):
    #Write your code here
    if(root == None):
        return
    q = []
    m = dict()
    hd = 0
    root.level = hd
 
    # push node and horizontal
    # distance to queue
    q.append(root)
 
    while(len(q)):
        root = q[0]
        hd = root.level
 
        # count function returns 1 if the
        # container contains an element
        # whose key is equivalent to hd,
        # or returns zero otherwise.
        if hd not in m:
            m[hd] = root.info
        if(root.left):
            root.left.level = hd - 1
            q.append(root.left)
 
        if(root.right):
            root.right.level = hd + 1
            q.append(root.right)
 
        q.pop(0)
        
    for i in sorted(m):
        print(m[i], end=" ")
    

if __name__ == "__main__":
    print('No of nodes in tree:')
    t = int(input())
    print('Enter tree node data:')
    
    arr = list(map(int, input().split()))

    tree = BinarySearchTree()
    for i in range(t):
        node = arr[i]
        tree.create(node)
    
    topView(tree.root)
        

        
        
        