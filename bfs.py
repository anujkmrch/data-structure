'''
Auto adjust binary tree
'''

###### Node class start ######
class Node(object):
    """docstring for Node."""

    def __init__(self, weight,name,parent=None):
        super(Node, self).__init__()
        self.left = None
        self.right = None
        self.weight = weight
        self.name = name
        self.parent=parent
    '''
      method to add left element to the current node
     '''
    def addLeft(self, node):
            self.left = node

#    method to add right element to the current node
    def addRight(self, node):
        self.right = node

######  Node class end ######

'''
                                  (5,A) #Root Node
                                /      \
                               /        \
                              /          \
                       #left(4,B)        (6,C)#right
                            /   \          /    \
                           /     \        /      \
              #left_left(2,D)  (3,F)     (8,G)    (9,H)#right_right
                        /  \  #left_right   \#right_left
                       /    \                \
      #left_left_left(0,I)  (1,J)             (10,K)#right_left_right
                            #left_left_right

'''

#Root node
root = Node(5,"A",None)

#Left node of root node
left = Node(4,"B",root)

#Right node of root's left node
left_right = Node(3,"F",left)

left_left = Node(2,"D",left)

left_left_right = Node(1,"J",left_left)

left_left_left = Node(0,"I",left_left)

right = Node(6,"C",root)

right_left = Node(8,"G",right)

right_left_right = Node(10,"K",right_left)

right_right = Node(9,"H",right)

left_left.addLeft(left_left_left)

left_left.addRight(left_left_right)

left.addLeft(left_left)

left.addRight(left_right)

right_left.addRight(right_left_right)

right.addLeft(right_left)

right.addRight(right_right)

root.addLeft(left)

root.addRight(right)


def levelOrder(root):

    if root == None:
        return None

    queue = []
    queue.insert(0,root)

    while len(queue) > 0:
        current = queue.pop()

        if current.left != None:
            queue.insert(0,current.left)

        if current.right != None:
            queue.insert(0,current.right)

        print current.name,current.weight

# levelOrder(root)

def BFS(root,search):
    if root == None:
        return None

    queue   = []
    queue.insert(0,root)

    while len(queue) > 0:
        current = queue.pop()
        if current.name == search:
            return current

        if current.left != None:
            queue.insert(0,current.left)

        if current.right != None:
            queue.insert(0,current.right)

    return None

'''
We are using preOrder traversal for DFS
'''

def DFS(root,search):
    if root == None:
        return None

    if root.name == search:
        return root

    result = DFS(root.left,search)

    if result != None:
        return result

    result = DFS(root.right,search)

    if result != None:
        return result

    return result

search = "K"

print ("--- We are searching \"{0}\" by DFS ---".format(search))
item = DFS(root,search)
if item:
    print item.name,item.weight
else:
    print "No found"

print ("--- We are searching \"{0}\" BFS ---".format(search))
item = BFS(root,search)
if item:
    print item.name,item.weight
else:
    print "No found"
