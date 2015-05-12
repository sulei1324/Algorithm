__author__ = 'Su Lei'

class Queue():
    def __init__(self, l):
        self.data = [None] * l
        self.head = 0
        self.tail = 0

    def isEmpty(self):
        if self.head is self.tail:
            return True
        else:
            return False

    def getQueuePeople(self):
        return (self.tail - self.head + len(self.data)) % len(self.data)

    def append2(self, v):
        if (self.tail + 1 + len(self.data)) % len(self.data) is self.head:
            print "Full"
            return None
        self.data[self.tail] = v
        self.tail = (self.tail + 1) % len(self.data)

    def shift2(self):
        if self.tail == self.head:
            print "Empty"
            return None
        t = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % len(self.data)
        return t

a = Queue(2)
for i in xrange(1):
    a.append2(i)

for i in xrange(2):
    print a.shift2()

