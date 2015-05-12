__author__ = 'Su Lei'

import random

class Node():
    def __init__(self, v):
        self.data = v
        self.next = None

class LinkedStack():
    def __init__(self):
        self.top = None
        self.length = 0

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    def clearStack(self):
        self.__init__()

    def push2(self, v):
        n = Node(v)
        n.next = self.top
        self.top = n
        self.length += 1

    def pop2(self):
        if not self.isEmpty():
            t = self.top.data
            self.top = self.top.next
            self.length -= 1
            return t
        else:
            print "Empty"

    def traceStack(self):                                               # the order is the same as pop()
        if not self.isEmpty():
            p = self.top
            while p is not None:
                print p.data
                p = p.next
        else:
            print "Empty"

a = LinkedStack()
for i in xrange(100):
    a.push2(random.randint(1, 100))


a.traceStack()
print "-------------------------------------"

for i in xrange(100):
    print a.pop2()

a.traceStack()

