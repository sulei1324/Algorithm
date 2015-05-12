__author__ = 'Su Lei'

import math

def count_sticks(n):
    m = 0
    data = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    while n / 10 != 0:
        m += data[(n % 10)]
        n /= 10
    m += data[n]
    return m

total_sticks = 24
max_num = 0
for i in xrange(int(math.ceil((total_sticks - 4) / 4.0))):
    max_num = max_num * 10 + 1

for a in xrange(0, max_num + 1):
    for b in xrange(0, max_num + 1):
        c = a + b
        used_sticks = count_sticks(c) + count_sticks(a) + count_sticks(b)
        if used_sticks + 4 == total_sticks:
            # print "%d + %d = %d" % (count_sticks(a), count_sticks(b), count_sticks(c))
            print "%d + %d = %d" % (a, b, c)
