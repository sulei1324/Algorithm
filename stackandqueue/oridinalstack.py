__author__ = 'Su Lei'
import random

class Stack():
    def __init__(self):
        self.data = []
        self.length = 0
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def clearStack(self):
        self.__init__()

    def push2(self, v):
        self.data.append(v)
        self.length += 1
        self.top += 1

    def pop2(self):
        if not self.isEmpty():
            t = self.data[self.top]
            self.top -= 1
            self.length -= 1
            # t = self.data.pop()
            return t
        else:
            print "Empty Stack"
            return None

    def stackLength(self):
        return self.length

    def getTop(self):
        if not self.isEmpty():
            return self.data[self.top]
        else:
            print "Empty stack"
            return None

    def printStack(self):
        if not self.isEmpty():
            for i in xrange(self.length):
                print self.data[i]
        else:
            print "Empty Stack"
            return None

a = Stack()
for i in xrange(100):
    a.push2(random.randint(1, 100))

a.printStack()
print "-------------------------------------------------"

for i in xrange(100):
    print a.pop2(), a.length

print a.pop2()