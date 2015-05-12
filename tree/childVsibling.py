__author__ = 'Su Lei'

class Node():
    def __init__(self, v):
        self.data = v
        self.firstChild = None
        self.rightSibling = None
        self.depth = 0

class Tree():
    def __init__(self, n):
        self.root = n
        self.node_num = 1
        n.depth = 1

    def insertNode(self, n, f):
        p = f.firstChild
        if p is None:
            f.firstChild = n
        else:
            s = p
            q = p.rightSibling
            while q is not None:
                s = q
                q = q.rightSibling
            s.rightSibling = n
        n.depth = f.depth + 1

    def traceTree(self):
        p = self.root
        f_stack = []
        f_stack.append(p)
        while len(f_stack) is not 0:
            if p is not None:
                print p.data, p.depth
                if p.firstChild is not None:
                    f_stack.append(p)
                    p = p.firstChild
                    continue
                elif p.rightSibling is not None:
                    p = p.rightSibling
                    continue
            q = f_stack.pop()
            p = q.rightSibling

    def findFather(self, n):
        p = self.root
        f_stack = []
        flag = 0
        while True:
            if p is not None:
                if p is n:
                    flag = 1
                    break
                if p.firstChild is not None:
                    f_stack.append(p)
                    p = p.firstChild
                    continue
                elif p.rightSibling is not None:
                    p = p.rightSibling
                    continue
            if len(f_stack) is 0:
                break
            else:
                q = f_stack.pop()
                p = q.rightSibling

        if flag is 1 and len(f_stack) is not 0:
            return f_stack.pop()
        else:
            print 'can not find'
            return None

    def deleteNode(self, n):
        f = self.findFather(n)
        if f is None:
            return None
        else:
            p = f.firstChild
            s = p
            if p is n:
                f.firstChild = n.rightSibling
            else:
                while p is not n:
                    s = p
                    p = p.rightSibling
                s.rightSibling = p.rightSibling
            del n
            return 0



