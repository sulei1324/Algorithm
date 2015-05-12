__author__ = 'Su Lei'

class Node():
    def __init__(self, v):
        self.data = v
        self.pre = None
        self.nex = None

    def printNode(self):
        print self, self.data, self.pre, self.nex

class DoubleLink():
    def __init__(self):
        self.head = Node(0)
        self.head.pre = self.head
        self.head.nex = self.head

    def insertNode(self, i, v):
        if i < 1 or i > self.head.data + 1:
            print "out of range"
            return
        p_node = self.head
        n = Node(v)
        j = 1
        while j < i:
            p_node = p_node.nex
            j += 1
        n.nex = p_node.nex
        n.pre = p_node
        p_node.nex.pre = n
        p_node.nex = n
        self.head.data += 1

    def deleteNode(self, i):
        if i < 1 or i > self.head.data:
            print "out of range"
            return
        p_node = self.head


    def printLink(self):
        p_node = self.head
        l = p_node.data
        i = 0
        while i <= l:
            p_node.printNode()
            p_node = p_node.nex
            i += 1

a = DoubleLink()
a.insertNode(1, 2)
a.insertNode(2, 20)
a.printLink()
