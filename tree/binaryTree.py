__author__ = 'Su Lei'

class Node():
    def __init__(self, v):
        self.data = v
        self.rightChild = None
        self.leftChild = None
        self.childNum = 0

class Tree():
    def __init__(self, n):
        self.root = n
        self.nodeNum = 1

    def insertNode(self, n, f):
        if f.childNum is 2:
            print 'can not'
            return
        if f.childNum is 0:
            f.leftChild = n
            f.childNum += 1
            self.nodeNum += 1
        else:
            f.rightChild = n
            f.childNum += 1
            self.nodeNum += 1

    def traceTree(self):
        p = self.root
        f_stack = [p]
        i = 0
        print self.nodeNum
        while i < self.nodeNum:
            if p is not None:
                print p.data
                if p.leftChild is not None:
                    f_stack.append(p)
                    p = p.leftChild
                    i += 1
                    continue
                elif p.rightChild is not None:
                    p = p.rightChild
                    i += 1
                    continue
            p = f_stack.pop()
            p = p.rightChild
            if p is not None:
                i += 1

    def traceTree2(self):
        p = self.root
        f_stack = []
        i = 0
        while i < self.nodeNum:
            if p is not None:
                while p.leftChild is not None:
                    f_stack.append(p)
                    p = p.leftChild
                print p.data
                i += 1
            if len(f_stack) is not 0:
                p = f_stack.pop()
                i += 1
                print p.data
                p = p.rightChild

    def traceTree3(self):
        p = self.root
        l = self.nodeNum
        i = 0
        f_stack = []
        l_stack = []
        r_stack = []
        while i < l:
            if p not in l_stack:
                while p.leftChild is not None:
                    f_stack.append(p)
                    l_stack.append(p)
                    p = p.leftChild
                print p.data
                i += 1
                j = len(f_stack)
                p = f_stack[j - 1]
            elif p not in r_stack:
                r_stack.append(p)
                q = p.rightChild
                if q is not None and q.leftChild is not None:
                    p = q
                    continue
                elif q is not None:
                    print q.data
                    i += 1
            else:
                if p not in f_stack:
                    print p.data
                    i += 1
                if len(f_stack) is not 0:
                    p = f_stack.pop()


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
a.traceTree3()