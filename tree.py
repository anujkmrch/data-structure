class Node(object):
    """docstring for Node."""
    def __init__(self, weight,name,parent=None):
        super(Node, self).__init__()
        self.weight = weight
        self.name = name
        self.parent = parent
        self.children = []

    # method to add children to current node
    # returns added child node
    def addChild(self, weight,name):
        node = Node(weight,name,self)
        self.children.append(node)
        return node

    # method to get parent of the current node
    def getParent(self):
        return self.parent

## Recursive function to print tree
## mapped by parent or None
def printTree(node):
    print node.weight,node.name, (node.parent.name if node.parent != None else None)
    for child in node.children:
        printTree(child)

## Create root node
root = Node(6,"A")

## Add children to root node
## return the added child of the root node
current = root.addChild(4,"T")

## add child of the current node and grand child of root node
current = current.addChild(3,"G")

## another method to add grand child of root node
current = current.getParent().addChild(5,"H")

current = current.addChild(7,"8")
current = current.getParent().getParent().addChild(5,"H")

printTree(root)
