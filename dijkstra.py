__author__ = 'Su Lei'

M = 999999
map_i = [[0, 1, 12, M, M, M],
         [M, 0, 9, 3, M, M],
         [M, M, 0, M, 5, M],
         [M, M, 4, 0, 13, 15],
         [M, M, M, M, 0, 4],
         [M, M, M, M, M, 0]]

num_of_city = len(map_i)


def dijkstra(l):
    d1 = creatDisOfi(l)
    d0[l-1] = 1
    for i in xrange(num_of_city):
        flag = 0
        j = findMinium(d1)
        if j == -1:
            break
        else:
            d0[j] = 1
            print j
            for k in xrange(num_of_city):
                if map_i[j][k] == M:
                    continue
                else:
                    if d1[k] > d1[j] + map_i[j][k]:
                        flag = 1
                        d1[k] = d1[j] + map_i[j][k]
        if flag == 0:
            break
        print d1, d0

    return d1


def findMinium(d):
    k = 0
    im = -1
    for i in xrange(num_of_city):
        if d0[i] == 1:
            continue
        else:
            if k == 0:
                m = d[i]
                im = i
            elif d[i] < m:
                m = d[i]
                im = i
            k += 1
    return im


def creatDisOfi(i):
    d = []
    for j in xrange(num_of_city):
        d.append(map_i[i-1][j])
    return d

d0 = [0] * num_of_city
d = dijkstra(1)

