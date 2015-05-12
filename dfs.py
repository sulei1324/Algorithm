__author__ = 'Su Lei'


def print_num(n):
    global total_a
    total_a += 1
    s = ""
    for i in n:
        s += "%d" % i
    print s


def print_equation(n):
    print "%d%d%d + %d%d%d = %d%d%d" % (n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7], n[8])

def a(s):
    if s == digit:
        if num[0]*100 + num[1]*10 + num[2] + num[3]*100 + \
                        num[4]*10 + num[5] == num[6]*100 + num[7]*10 + num[8]:
            print_equation(num)
        return
    for i in xrange(digit):
        if map_i[i] == 0:
            num[s] = i + 1
            map_i[i] = 1
            a(s+1)
            map_i[i] = 0


digit = 9
map_i = [0] * digit
num = [0] * digit
total_a = 0
step = 0
a(step)
print total_a



