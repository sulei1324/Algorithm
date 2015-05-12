__author__ = 'Su Lei'
import string

class Stack():
    def __init__(self):
        self.data = []
        self.length = 0

    def push2(self, v):
        self.data.append(v)
        self.length += 1

    def pop2(self):
        if self.length is not 0:
            self.length -= 1
            return self.data.pop()
        else:
            print "Empty"
            return None

    def getLastElm(self):
        if self.length is not 0:
            return self.data[self.length - 1]
        else:
            return None

def stackOp(su, op):
    spop = ''
    t = su.getLastElm()
    if op is ')':
        t = su.pop2()
        while t is not '(':
            spop += t + ' '
            t = su.pop2()
        return spop
    elif op is '(':
        pass
    else:
        while t is not None and t is not '(':
            if cmpOp(op, t) > 0:
                su.push2(op)
                return ''
            else:
                spop += su.pop2() + ' '
                t = su.getLastElm()
    su.push2(op)
    return spop


def cmpOp(op1, op2):
    if op1 in '*/' and op2 in '*/':
        return 0
    elif op1 in '*/' and op2 in '+-':
        return 1
    elif op1 in '+-' and op2 in '+-':
        return 0
    elif op1 in '+-' and op2 in '*/':
        return -1


def doRPN(st):
    l = len(st)
    sout = ''
    a = Stack()
    for i in xrange(l):
        t = st[i]

        if t in string.digits:
            if (i is not l - 1 and st[i+1] not in string.digits) or i is l - 1:
                sout += t + ' '
            else:
                sout += t
        else:
            if t in '+-*/()':
                sout += stackOp(a, t)
        print sout, a.data
    while a.length is not 0:
        sout += a.pop2() + ' '
    return sout

def doOperation(sin):
    a = Stack()
    l = len(sin)
    r = 0
    for i in xrange(l):
        print a.data
        if sin[i] not in '+-*/':
            a.push2(sin[i])
        else:
            r = 0
            i2 = a.pop2()
            i1 = a.pop2()
            i2 = int(i2)
            i1 = int(i1)
            if sin[i] is '+':
                r += i1 + i2
            elif sin[i] is '-':
                r += i1 - i2
            elif sin[i] is '*':
                r += i1 * i2
            else:
                r += i1 / i2
            a.push2(r)
    return r


s = '91+(3-1)*3+10/2'
s = doRPN(s).strip().split()
print doOperation(s)






