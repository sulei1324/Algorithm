__author__ = 'Su Lei'

def swap1(n, l):
    t1 = l[n]
    t2 = l[n+1]
    t3 = t1
    t1 = t2
    t2 = t3
    l[n] = t1
    l[n+1] =t2
    pass


def swap2(n, l):
    t1 = l[n]
    t2 = l[n+1]
    t1 = t2 - t1
    t2 = t2 - t1
    t1 = t2 + t1
    l[n] = t1
    l[n+1] = t2

def swap3(n,l):
    t1 = l[n]
    t2 = l[n+1]
    t1 = t1 ^ t2
    t2 = t1 ^ t2
    t1 = t1 ^ t2
    l[n] = t1
    l[n+1] = t2

def bubblesort(li):
    l = len(li)
    flag = 0
    for i in xrange(l-1):
        flag = 0
        for j in xrange(l-1-i):
            if li[l-j-2] < li[l-j-1]:
                flag = 1
                swap1(l-2-j, li)
        if (i != 0) and (flag == 0):
            break
        print li


li = [1, 5, 3, 9, 2, 44, 32]
bubblesort(li)
