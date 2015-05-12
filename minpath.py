__author__ = 'Su Lei'

import copy

def print_path(m):
    global w, h
    for i1 in xrange(h):
        s = ""
        for j1 in xrange(w):
            if [i1, j1] not in m:
                if map_i[i1][j1] == 1:
                    s += " # "
                else:
                    s += " * "
            else:
                s += " - "
        print s

# map_i = [[0, 0, 0, 1, 0],
#          [0, 1, 0, 1, 0],
#          [1, 0, 0, 0, 0],
#          [0, 0, 1, 0, 1],
#          [0, 0, 0, 0, 0]]

map_i = [[0, 0, 1, 0],
         [0, 0, 0, 0],
         [0, 0, 1, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 1]]

h = len(map_i)
w = len(map_i[0])
data_i = []
for i in xrange(h):
    data_i.append([0]*w)

step = 1
path = []
min_step = 99999
min_path = []


ini_location = [0, 0]
dest_location = [3, 2]

def dfs(l, s):
    print path
    global min_path, min_step
    next_step = ((0, 1), (1, 0), (0, -1), (-1, 0))
    x = l[0]
    y = l[1]
    if x == dest_location[0] and y == dest_location[1]:
        # print_path(path)
        # print path
        if s < min_step:
            min_step = s
            min_path = copy.deepcopy(path)
        return
    for j in next_step:
        nx = j[0] + x
        ny = j[1] + y
        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            continue
        if map_i[nx][ny] != 1 and data_i[nx][ny] == 0:
            s += 1
            data_i[nx][ny] = 1
            path.append([nx, ny])
            dfs([nx, ny], s)
            path.pop()
            data_i[nx][ny] = 0
            s -= 1

data_i[ini_location[0]][ini_location[1]] = 1
path.append(ini_location)
dfs(ini_location, step)


