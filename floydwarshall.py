__author__ = 'Su Lei'
import copy

map_i = [[0, 2, 6, 4],
         [999999, 0, 3, 999999],
         [7, 999999, 0, 1],
         [5, 999999, 12, 0]]

map_j = copy.deepcopy(map_i)
def count_min_path():
    for i in xrange(4):
        for j in xrange(4):
            for k in xrange(4):
                if map_i[j][k] > map_i[j][i] + map_i[i][k]:
                    if j == 2 and k == 1:
                        print i                                                      # reverse of the output is the path
                    map_i[j][k] = map_i[j][i] + map_i[i][k]
                if map_i[j][k] == 999999:
                    map_i[j][k] = 999999
        print map_i

count_min_path()
