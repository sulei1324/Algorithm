__author__ = 'Su Lei'
import sys

class Node():
    def __init__(self, v):
        self.data = v
        self.leftChild = None
        self.rightChild = None


class Tree():
    pre = None
    def __init__(self, n):
        self.root = n
        self.nodeNum = 1

    def insertNode(self, n, f):
        if f.leftChild is None:
            f.leftChild = n
        elif f.rightChild is None:
            f.rightChild = n
        else:
            print 'can not'
            return None
        return 0

    def trace1(self, p):
        if p is None:
            return
        else:
            sys.stdout.write(p.data)
            self.trace1(p.leftChild)
            self.trace1(p.rightChild)

    def trace2(self, p):
        if p is None:
            return
        else:

            self.trace2(p.leftChild)
            self.pre = p
            print p.data, '    ---'
            print self.pre.data
            self.trace2(p.rightChild)

    def trace3(self, p):
        if p is None:
            return
        else:
            self.trace3(p.leftChild)
            self.trace3(p.rightChild)
            sys.stdout.write(p.data)



t1 = Node('A')
t2 = Node('B')
t3 = Node('C')
t4 = Node('D')
t5 = Node('E')
t6 = Node('F')

a = Tree(t1)
a.insertNode(t2, t1)
a.insertNode(t3, t1)
a.insertNode(t4, t2)
a.insertNode(t5, t2)
a.insertNode(t6, t5)
a.trace2(a.root)

