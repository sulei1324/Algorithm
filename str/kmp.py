__author__ = 'Su Lei'

def kmp(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    next_a = getNext(s2)

def getNext(s):
    l = len(s)
    nx = [None] * l
    nx[0] = 0
    nx[1] = 0
    j = 0
    i = 1
    while i < l - 1:
        if j is 0 or s[i] is s[j]:
            j += 1
            i += 1
            nx[i] = j

        else:
            j = nx[j]

    return nx

a = 'axtaxa'
print getNext(a)