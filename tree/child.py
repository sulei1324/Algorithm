__author__ = 'Su Lei'

class Node():
    def __init__(self, l):
        self.location = l
        self.nextSibling = None

class TreeNode():
    def __init__(self, v):
        self.data = v
        self.firstChild = None

class Tree():
    def __init__(self, tn):
        self.validIndex = []
        self.data = []
        self.data.append(tn)
        self.node_num = 1
        self.root = tn


    def insertNode(self, tn, ftn):
        if len(self.validIndex) is not 0:
            i = self.validIndex.pop()
            self.data[i] = tn
        else:
            self.data.append(tn)
            i = len(self.data) - 1
        self.node_num += 1
        p = ftn.firstChild
        n = Node(i)
        if p is None:
            ftn.firstChild = n
        else:
            while p.nextSibling is not None:
                p = p.nextSibling
            p.nextSibling = n

    def indexOf(self, tn):
        p = self.root
        i = 0
        while p is not tn and i < len(self.data):
            p = self.data[i]
            i += 1
        if i < len(self.data) or (i is len(self.data) and self.data[i - 1] is tn):
            return i - 1
        else:
            return -1

    def findFather(self, tn):
        l = len(self.data)
        flag = 0
        for i in xrange(l):
            p = self.data[i]
            if p is not None and p.firstChild is not None:
                son_p = p.firstChild
                while son_p is not None:
                    son_l = son_p.location
                    if self.data[son_l] is tn:
                        flag = 1
                        break
                    else:
                        son_p = son_p.nextSibling
            if flag is 1:
                return i
        return None


    def deleteNode(self, tn):
        n = self.indexOf(tn)
        if n is -1:
            return None
        fn_index = self.findFather(tn)
        if fn_index is None:
            print "can not"
            return None
        else:
            p = self.data[fn_index].firstChild
            b = p
            while p is not None:
                if self.data[p.location] is tn:
                    b.nextSibling = p.nextSibling
                    p = None
                    break
                b = p
                p = p.nextSibling

        if tn.firstChild is None:
            self.validIndex.append(n)
            tn = None
            self.node_num -= 1
        else:
            p = tn.firstChild
            while p is not None:
                l = p.location
                self.validIndex.append(l)
                self.data[l] = None
                self.node_num -= 1
                np = p.nextSibling
                p = None
                p = np
            self.validIndex.append(n)
            self.data[n] = None
            self.node_num -= 1

    def traceTree(self):
        l = len(self.data)
        for i in xrange(l):
            p = self.data[i]
            if p is not None:
                print 'location: ', i, 'value: ', p.data
                if p.firstChild is not None:
                    j = 1
                    q = p.firstChild
                    while q is not None:
                        print 'child: ', j, 'location: ', q.location, 'value: ', self.data[q.location].data
                        q = q.nextSibling
                        j += 1
            else:
                print 'location: ', i, ' is None'
        print self.validIndex
        print '--------------------------------------------------------'



t1 = TreeNode('A')
t2 = TreeNode('B')
t3 = TreeNode('C')
t4 = TreeNode('D')
t5 = TreeNode('E')
t6 = TreeNode('F')
a = Tree(t1)
a.insertNode(t2, t1)
a.insertNode(t3, t1)
a.insertNode(t4, t2)
a.insertNode(t5, t2)
a.insertNode(t6, t5)

a.traceTree()
a.deleteNode(t5)
a.traceTree()

