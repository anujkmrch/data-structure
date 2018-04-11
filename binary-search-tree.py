'''
Auto adjust binary tree
'''

###### Node class start ######
class Node(object):
    """docstring for Node."""

    def __init__(self, arg,name):
        super(Node, self).__init__()
        self.left = None
        self.right = None
        self.root = arg
        self.name = name

    # add value to the binary search tree
    # at correct position according to the weight
    def addvalue(self,arg,name):
        if arg < self.root:
            if self.left == None:
                self.left = Node(arg,name)
                return
            self.left.addvalue(arg,name)

        if arg >self.root:
            if self.right == None:
                self.right = Node(arg,name)
                return
            self.right.addvalue(arg,name)

    ## Method to return the tree value
    ## according to the weight
    def getValue(self,arg):
        if arg < self.root:
            return self.left.getValue(arg)

        if arg > self.root:
            return self.right.getValue(arg)

        return self
###### Node class end ######

root = Node(6,"A")
root.addvalue(5,"B")
root.addvalue(4,"F")
root.addvalue(3,"D")
root.addvalue(2,"J")
root.addvalue(1,"I")
root.addvalue(9,"C")
root.addvalue(7,"G")
root.addvalue(8,"K")
root.addvalue(10,"H")

##demo loop to search the weight value
for i in range(0,13):
    try:
        print("Element with weight {0} has value : {1}".format(i,root.getValue(i).name))
    except Exception as e:
        print("Weight \"{}\" has no value".format(i))
