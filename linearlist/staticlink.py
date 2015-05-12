__author__ = 'Su Lei'
import random

class Node():
    def __init__(self, v):
        self.data = v
        self.cur2next = -1

class StaticLink():
    def __init__(self, l):
        self.list = []
        for i in xrange(l):
            n = Node(None)
            if i in range(1, l-1):
                n.cur2next = i + 1
            self.list.append(n)
        self.list[0].cur2next = 1
        self.list[0].data = l
        self.list[l-1].cur2next = -1
        self.list[l-1].data = 0

    def insertNode(self, i, v):

        l = self.list[0].data
        if i < 1:
            print "out of range"
            return
        p_cur = l - 1
        j = 1
        while p_cur is not -1 and j < i:
            p_cur = self.list[p_cur].cur2next
            j += 1
        if p_cur is not -1:                                           # if p_cur == -1, i >= (j = self.list[l-1].data + 2)
            unused_cur = self.list[0].cur2next
            self.list[unused_cur].data = v
            self.list[0].cur2next = self.list[unused_cur].cur2next
            self.list[unused_cur].cur2next = self.list[p_cur].cur2next
            self.list[p_cur].cur2next = unused_cur
            self.list[l-1].data += 1
        else:
            print "can not put into more"
            return

    def isEmpty(self):
        l = self.list[0].data
        if self.list[l-1].data is 0:
            return True
        else:
            return False

    def clearList(self):
        l = self.list[0].data
        self.__init__(l)

    def deleteNode(self, i):
        if i < 1:
            print "out of range"
            return
        l = self.list[0].data
        p_cur = l - 1
        j = 1                                                   # make sure p_cur will cursor before the i node
        while p_cur is not -1 and j < i:                      # if p_cur == -1 then i >= (j == self.list[l-1].data + 2)
            p_cur = self.list[p_cur].cur2next
            j += 1
        if p_cur is not -1 and i <= self.list[l-1].data:
            temp_cur = self.list[p_cur].cur2next
            self.list[temp_cur].data = None
            self.list[p_cur].cur2next = self.list[temp_cur].cur2next
            self.list[temp_cur].cur2next = self.list[0].cur2next
            self.list[0].cur2next = temp_cur
            self.list[l-1].data -= 1
        else:
            print "can not delete"
            return

    def printList(self):
        l = self.list[0].data
        for i in xrange(l):
            print i, self.list[i].data, self.list[i].cur2next

    def traceNodeWithValue(self):
        l = self.list[0].data
        p_cur = self.list[l-1].cur2next
        print self.list[l-1].data, self.list[l-1].cur2next
        while p_cur is not -1:
            # print self.list[p_cur].data, self.list[p_cur].cur2next
            p_cur = self.list[p_cur].cur2next
        print "next: ", self.list[0].cur2next

    def isFull(self):
        l = self.list[0].data
        if self.list[l-1].data is l - 2:
            return True
        else:
            return False


a = StaticLink(102)

for i in xrange(1, 51):
    a.insertNode(i, i)


a.deleteNode(18)
a.deleteNode(1)
a.printList()


