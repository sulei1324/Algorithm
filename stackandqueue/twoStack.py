__author__ = 'Su Lei'

import random

class TwoStack():
    def __init__(self, l):
        self.data = [None] * l
        self.top1 = -1
        self.top2 = l
        self.length1 = 0
        self.length2 = 0

    def isEmpty(self, n):
        if n == 1:
            if self.top1 == -1:
                return True
            else:
                return False
        elif n == 2:
            if self.top2 == -1:
                if self.top2 == len(self.data):
                    return True
                else:
                    return False

    def clearStack(self, n):
        if n == 1:
            self.top1 = -1
        elif n == 2:
            self.top2 = l
        elif n == 3:
            self.top1 = -1
            self.top2 = l

    def isFull(self):
        if self.top2 - self.top1 is 1:
            return True
        else:
            return False

    def push2(self, n, v):
        if not self.isFull():
            if n == 1:
                self.top1 += 1
                self.data[self.top1] = v
                self.length1 += 1
            elif n == 2:
                self.top2 -= 1
                self.data[self.top2] = v
                self.length2 += 1
        else:
            print "Full"

    def pop2(self, n):
        if n is 1:
            if not self.isEmpty(1):
                t = self.data[self.top1]
                self.top1 -= 1
                self.length1 -= 1
                return t
            else:
                print "stack 1 is empty"
                return
        elif n is 2:
            if not self.isEmpty(2):
                t = self.data[self.top2]
                self.top2 += 1
                self.length2 -= 1
                return t
            else:
                print "stack 2 is empty"
                return

    def getLength(self, n):
        if n == 1:
            return self.length1
        elif n == 2:
            return self.length2

    def printStack(self):
        for i in xrange(len(self.data)):
            print self.data[i]

a = TwoStack(100)
for i in xrange(50):
    a.push2(1, i)
    a.push2(2, i)

a.printStack()
print a.isFull()

