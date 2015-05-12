__author__ = 'Su Lei'

import random

class LinearList():
    def __init__(self):
        self.head = node(0)

    def isEmpty(self):
        if self.head.d == 0:
            return True
        else:
            return False

    def clearList(self):
        self.head.next = None
        self.head.d = 0

    def insertList(self, i, v):
        if i < 0 or i > self.head.d + 1:
            print "out of range"
            return
        j = 1
        p = self.head
        while j < i:
            p = p.next
            j += 1
        self.head.d += 1
        n = node(v)
        n.next = p.next
        p.next = n




    def deleteList(self, i):
        if i < 0 or i > self.head.d:
            print "out of range"
            return
        j = 1
        p = self.head
        while j < i:
            p = p.next
            j += 1
        self.head.d -= 1
        s = p.next
        p.next = p.next.next
        s.next = None


    def getElement(self, i):
        if i < 0 or i > self.head.d:
            print "out of range"
            return
        j = 1
        p = self.head
        while j < i:
            p = p.next
            j += 1
        return p.next.d

    def locateElement(self, v):
        p = self.head
        flag = 0
        i = 0
        while p is not None:
            if p.d is v:
                flag = 1
                break
            p = p.next
            i += 1

        if flag == 1:
            return i
        else:
            return -1

    def listLength(self):
        return self.head.d

class node():
    def __init__(self, v):
        self.d = v
        self.next = None


a = LinearList()
for i in xrange(100):
    a.insertList(i, random.randint(0, 10))

print a.getElement(40)
