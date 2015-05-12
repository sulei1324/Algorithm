__author__ = 'Su Lei'

map_i = [[0, 0, 1, 0],
         [0, 0, 0, 0],
         [0, 0, 1, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 1]]

h = len(map_i)
w = len(map_i[0])
data_i = []
for i1 in xrange(h):
    data_i.append([0]*w)

class Node():
    def __init__(self, x, y, h, s):
        self.x = x
        self.y = y
        self.head = h
        self.step = s

queue = [None] * w * h
head = 0
tail = 0
step = 0
ini_location = [0, 0]
dest_location = [3, 2]
queue[head] = Node(ini_location[0], ini_location[1], head, step)
tail += 1

def sfs(x, y):
    global head, tail
    flag = 0
    next_i = ((0, 1), (1, 0), (0, -1), (-1, 0))
    while head != tail:
        x = queue[head].x
        y = queue[head].y
        for i in next_i:
            nx = i[0] + x
            ny = i[1] + y
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if map_i[nx][ny] == 0 and data_i[nx][ny] == 0:
                nN = Node(nx, ny, head, queue[head].step + 1)
                queue[tail] = nN
                tail += 1
                data_i[nx][ny] = 1
            if nx == dest_location[0] and ny == dest_location[1]:
                flag = 1
                break
        if flag == 1:
            break
        head += 1

sfs(ini_location[0], ini_location[1])
for i2 in xrange(tail):
    print queue[i2].x, queue[i2].y, queue[i2].head, queue[i2].step, i2



