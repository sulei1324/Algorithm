__author__ = 'Su Lei'


def count_score(i, j, x, y):
    n = 0
    while game_map[i][j] != '#':
        if game_map[i][j] == 'G':
            n += 1
        i += x
        j += y
    return n

game_map = ['#############',
       '#GG.GGG#GGG.#',
       '###.#G#G#G#G#',
       '#.......#..G#',
       '#G#.###.#G#G#',
       '#GG.GGG.#.GG#',
       '#G#.#G#.#.###',
       '##G...G.....#',
       '#G#.#G###.#G#',
       '#...G#GGG.GG#',
       '#G#.#G#G#.#G#',
       '#GG.GGG#G.GG#',
       '#############']

score = 0
tx = 0
ty = 0
for i in range(len(game_map)):
    for j in range(len(game_map[0])):
        if game_map[i][j] == '.':
            n = 0
            n += count_score(i, j, 1, 0)
            n += count_score(i, j, -1, 0)
            n += count_score(i, j, 0, 1)
            n += count_score(i, j, 0, -1)
            if n > score:
                score = n
                tx = i
                ty = j

print score, tx, ty





