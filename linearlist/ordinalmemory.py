__author__ = 'Su Lei'

import random

# linear list with ordinal memory structure
class LinearList():

    def __init__(self):
        self.list = []
        self.length = 0

    def __getitem__(self, item):
        return self.list[item]

    def __getattr__(self, item):
        item = 50
        return self.list[item]

    def clearList(self):
        self.list = []
        self.length = 0

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def getElement(self, i):
        if i < 0 or i > self.length - 1:
            print "has no element"
            return -1
        else:
            return self.list[i]

    def locateElement(self, v):
        try:
            return self.list.index(v)
        except:
            return -1

    def listInsert(self, i, v):
        if i < 0 or i > self.length:
            print "wrong location"
            return
        else:
            self.list.insert(i, v)
            self.length += 1

    def listDelete(self, i):
        if i < 0 or i > self.length - 1:
            print "wrong location"
            return
        else:
            self.length -= 1
            return self.list.pop(i)

    def listLength(self):
        return self.length

a = LinearList()
for i in xrange(100):
    a.listInsert(i, random.randint(0, 10))


print a.s

a.clearList()

print a.list