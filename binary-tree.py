'''
You can check your results from here,
in my case k and i are missing
you may add it to your result
Anuj Kumar <me@anujkch.com>
http://btechsmartclass.com/DS/U3_T4.html
'''

###### Node class start ######
class Node(object):
    """docstring for Node."""

    def __init__(self, weight,name):
        super(Node, self).__init__()
        self.left = None
        self.right = None
        self.weight = weight
        self.name = name
    '''
      method to add left element to the current node
     '''
    def addLeft(self, node):
            self.left = node

#    method to add right element to the current node
    def addRight(self, node):
        self.right = node

######  Node class end ######

#Print in order
def printInOrder(arg):
    if(arg != None):
        printInOrder(arg.left)
        print arg.weight,arg.name
        printInOrder(arg.right)

#Print Pre order tree
def printPreOrder(arg):
    if(arg != None):
        print arg.weight,arg.name
        printPreOrder(arg.left)
        printPreOrder(arg.right)

#Print Post Order binary tree
def printPostOrder(arg):
    if(arg != None):
        printPostOrder(arg.left)
        printPostOrder(arg.right)
        print arg.weight,arg.name


def levelOrderTraversal(root):

    if root == None:
        return None

    queue = []
    queue.insert(0,root)

    while len(queue) > 0:
        current = queue.pop()

        print current.name,current.weight

        if current.left != None:
            queue.insert(0,current.left)

        if current.right != None:
            queue.insert(0,current.right)

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
root = Node(5,"A")

#Left node of root node
left = Node(4,"B")

#Right node of root's left node
left_right = Node(3,"F")

left_left = Node(2,"D")

left_left_right = Node(1,"J")

left_left_left = Node(0,"I")

right = Node(6,"C")

right_left = Node(8,"G")

right_left_right = Node(10,"K")

right_right = Node(9,"H")

left_left.addLeft(left_left_left)

left_left.addRight(left_left_right)

left.addLeft(left_left)

left.addRight(left_right)

right_left.addRight(right_left_right)

right.addLeft(right_left)

right.addRight(right_right)

root.addLeft(left)

root.addRight(right)

print "--- IN ---"
# printInOrder(root)

print "--- PRE ---"
# printPreOrder(root)

print "---POST---"
# printPostOrder(root)

print "---Level Order Traversal---"
print levelOrderTraversal(root)
