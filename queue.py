__author__ = 'Su Lei'
import numpy as np
import random as rd

class queue():
    def __init__(self, n):
        self.q = [None] * n
        self.head = 0
        self.tail = 0
        self.length = 0

    def isEmpty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def reachEnd(self):
        if self.tail == len(self.q):
            return True
        else:
            return False


    def add(self, m):
        if self.reachEnd():
            print "reach the end"
            return
        else:
            self.q[self.tail] = m
            self.tail += 1
            self.length += 1

    def delete(self):
        if self.isEmpty():
            print "empty"
            return
        else:
            self.q[self.head] = None
            self.head += 1
            self.length -= 1

    def print_queue(self):
        l = self.length
        for j in xrange(l):
            p = self.q[j]
            print p




a = queue(20)
for i in range(20):
    a.add([rd.randint(0, 100), rd.randint(0, 100)])
a.print_queue()