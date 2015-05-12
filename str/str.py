__author__ = 'Su Lei'
import string


class Str():
    def __init__(self):
        self.data = ''
        self.length = 0

    def appendStr(self, s):
        self.data = self.data + s
        self.length = len(self.data)

    def copyStr(self):
        return self.data

    def clearStr(self):
        self.__init__()

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def strCmp(self, s):
        l1 = self.length
        l2 = len(s)
        if l1 > l2:
            min = l2
        else:
            min = l1

        for i in xrange(min):
            if self.data[i] is not s[i]:
                return self.data[i] > s[i]
        if l1 is l2:
            return 0
        if l1 > l2:
            return False
        else:
            return True

    def substring(self, pos, len):
        if pos > self.length or pos + len > self.length:
            print "Out of range"
            return None
        return self.data[pos:pos+len]

    def indexInStr(self, s):
        x = 0
        l = len(s)
        for i in xrange(self.length):
            if i + l <= self.length and self.data[i] is s[0]:
                flag = 0
                for j in xrange(l):
                    if self.data[i+j] is not s[j]:
                        flag = 1
                        break
                if flag is 1:
                    continue
                else:
                    return i
        return None

    def index2(self, s):
        for i in xrange(len(self.data)):
            temp = self.substring(i, len(s))
            if temp is None:
                break
            tStr = Str()
            tStr.appendStr(temp)
            if tStr.strCmp(s) is 0:
                return i
        return None

    def replace(self, rd, s):
        l = self.length
        s0 = self.data
        i = 0
        showIndex = []
        while i < l:
            if (i + len(rd) <= l) and s0[i] == rd[0]:
                flag = 0
                for j in xrange(len(rd)):
                    if s0[i+j] is not rd[j]:
                        flag = 1
                        break
                if flag is 1:
                    i += 1
                    continue
                else:
                    showIndex.extend([i, i+j])
                    i += j
            i += 1
        if len(showIndex) is 0:
            print 'can not'
            return None
        else:
            print showIndex
            x = ''
            i = 0
            while i < l:
                if i in showIndex[::2]:
                    x += s
                    i = showIndex[showIndex.index(i) + 1] + 1
                else:
                    x += s0[i]
                    i += 1
            return x

    def replace2(self, rd, s):
        l = self.length
        s0 = self.data
        showIndex = []
        for i in xrange(l):
            if i + len(s) <= self.length:
                temp = Str()
                temp.appendStr(s0[i:i+len(s)])
                print temp.data, rd, temp.strCmp(rd)
                if temp.strCmp(rd) is 0:
                    showIndex.extend([i, i+len(s)-1])
        if len(showIndex) is 0:
            print 'can not'
            return None
        else:
            i = 0
            x = ''
            print showIndex
            while i < l:
                if i in showIndex[::2] and (i + len(s) - 1) in showIndex[1::2]:
                    x += s
                    i = i + len(s)
                else:
                    x += s0[i]
                    i += 1
            return x

    def strInsert(self, pos, s):
        s0 = self.data
        x = ''
        i = 0
        if pos < 0 or pos > self.length:
            print 'can not'
            return None
        while i <= self.length:
            if i is pos:
                x += s

            if i is not self.length:
                x += s0[i]
            i += 1
        return x

    def strDelete(self, pos, l):
        if pos < 0 or (pos + l) > self.length:
            print 'out of range'
            return None
        s0 = self.data
        l0 = self.length
        i = 0
        x = ''
        while i < l0:
            if i is pos:
                i += l
                continue
            x += s0[i]
            i += 1
        return x








a = Str()
a.appendStr('vrvvrvvf')
print a.index2('vvr')