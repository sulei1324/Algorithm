__author__ = 'Su Lei'

def canPut(x, y, A):
    i = 0
    while A[i] is not None:
        j = A[i]
        if j is y or (abs(i - x) is abs(j - y)):
            return False
        i += 1
    return True
    pass


def putIntoColumn(i, n, A):
    global a
    if i >= n:
        a += 1
        print A
    else:
        for j in xrange(n):
            if canPut(i, j, A):
                A[i] = j
                putIntoColumn(i+1, n, A)
                A[i] = None


def queens(n):
    A = [None] * n
    putIntoColumn(0, n, A)


a = 0
queens(4)
print a

