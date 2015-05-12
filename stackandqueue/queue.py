__author__ = 'Su Lei'


class Node():
    def __init__(self, v):
        self.data = v
        self.next = None


class Queue():
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head
        self.length = 0

    def insertNode(self, v):
        p = self.tail
        n = Node(v)
        p.next = n
        self.tail = n
        self.length += 1

    def shift2(self):
        p = self.head
        if self.length >= 1:
            p = p.next
            t = p.data
            self.head.next = p.next
            self.length -= 1
            return t
        else:
            print "Empty"
            return None

    def isEmpty(self):
        if self.length is 0:
            return True
        else:
            return False


a = Queue()
