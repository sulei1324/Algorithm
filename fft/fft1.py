__author__ = 'Su Lei'

import numpy as np
import math


def reverseOrder(s, n):
    t = np.zeros_like(s)
    m = 0
    i = 1
    l = len(s)
    while True:
        if i is n:
            break
        else:
            i *= 2
            m += 1
    for i in xrange(l):
        b = []
        j = i
        q = 0
        while j is not 0:
            b.append(j % 2)
            j /= 2
        if len(b) < m:
            for k in xrange(m - len(b)):
                b.append(0)
        for k in range(m):
            j = b.pop()
            if j is not 0:
                for p in xrange(k):
                    j *= 2
            q += j
        t[i] = s[q]
    return t




def W(n, k):
    a = 2 * math.pi / n
    r = math.cos(a * k) - 1j * math.sin(a * k)
    return r


def fft1(s):
    l = len(s)
    s1 = reverseOrder(s, l)
    i = 1
    t = np.copy(s1)
    while i < l:
        g = l / (i * 2)
        d = l / (g * 2)
        for j in xrange(g):
            s = (l / g) * j
            for k in xrange(d):
                sd = s + k
                se = s + k + i
                t1 = t[sd]
                t2 = t[se]
                w = W(2 * i, k)
                t[sd] = t1 + t2 * w
                t[se] = t1 - t2 * w
        i *= 2
    return t


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8], dtype=np.complex)
N = a.size
a1 = reverseOrder(a, N)
print fft1(a)
print np.fft.fft(a)



