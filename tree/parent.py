__author__ = 'Su Lei'

class Node():
    def __init__(self, v):
        self.data = v
        self.parent = None

class Tree():
    def __init__(self, n):
        self.node_num = 1
        self.root = n
        self.data = []
        self.data.append(n)

    def insertNode(self, n, f):
        self.data.append(n)
        n.parent = f
        self.node_num += 1

    def deleteNode(self, n):
        l = self.node_num
        flag = 0
        for i in xrange(l):
            if self.data[i] is n:
                flag = 1
                break
        if flag is 1:
            j = 0
            while j < len(self.data):
                if self.data[j].parent is n:
                    del self.data[j]
                    self.node_num -= 1
                    continue
                j += 1
            del self.data[i]
            self.node_num -= 1
            return 0
        else:
            return None

    def delete2(self, n):
        if not self.hasChild(n):
            for i in xrange(len(self.data)):
                if self.data[i] is n:
                    del self.data[i]
                    break
            self.node_num -= 1
            return
        else:
            i = 0
            while i < len(self.data):
                print len(self.data), i
                if self.data[i].parent is n:
                    self.delete2(self.data[i])
                    i = 0
                    continue
                i += 1
            for i in xrange(len(self.data)):
                if self.data[i] is n:
                    del self.data[i]
                    break
            self.node_num -= 1

    def getRoot(self):
        return self.root.data

    def childOf(self, f):
        l = self.node_num
        flag = 0
        for i in xrange(l):
            if self.data[i].parent is f:
                flag = 1
                print self.data[i].data

        if flag is 0:
            print 'no child'
            return None
        else:
            return 0

    def hasChild(self, f):
        l = self.node_num
        flag = 0
        for i in xrange(l):
            if self.data[i].parent is f:
                flag = 1
        if flag is 0:
            return False
        else:
            return True

    def siblingOf(self, n):
        l = self.node_num
        f = n.parent
        flag = 0
        for i in xrange(l):
            if self.data[i].parent is f and self.data[i] is not n:
                flag = 1
                print self.data[i].data
        if flag is 0:
            print 'no silbling'

n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')
n6 = Node('F')
n7 = Node('G')
n8 = Node('H')
n9 = Node('I')
t = Tree(n1)
t.insertNode(n2, n1)
t.insertNode(n3, n1)
t.insertNode(n4, n2)
t.insertNode(n5, n2)
t.insertNode(n6, n2)
t.insertNode(n7, n3)
t.insertNode(n8, n5)
t.insertNode(n9, n5)
t.delete2(n2)
t.childOf(n3)


