__author__ = 'Su Lei'




class Node():
    def __init__(self, v, r = None):
        self.value = v
        self.right = r

class Linkedlist():
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __getitem__(self, key):
        if self.length == 0:
            print "empty"
        elif key <= 0 or key > self.length:
            raise AttributeError
        else:
            return self.getItem(key)

    def getItem(self, index):
        i = 0
        p = self.head
        while i < index-1:
            p = p.right
            i += 1
        return p.value


    def emptyLinkedlist(self):
        self.__init__()

    def appendNode(self,n):
        if self.length == 0:
            self.head = n
            self.tail = n
        else:
            self.tail.right = n
            self.tail = n
        self.length += 1

    def delLastNode(self):
        if self.length > 1:
            for i in xrange(1, self.length, 1):
                if i == 1:
                    nbl = self.head
                else:
                    nbl = nbl.right
            self.tail = nbl
            nbl.right = None
            self.length -= 1
        elif self.length == 1:
            self.emptyLinkedlist()




n1 = Node(1)
n2 = Node(10)
n3 = Node(100)
l1 = Linkedlist()
l1.appendNode(n1)
l1.appendNode(n2)
l1.appendNode(n3)
print l1.head.value, l1.length

print l1[3]



