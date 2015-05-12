__author__ = 'Su Lei'

def equationWith9Nums():
    book = [0] * 9
    iters = [1] * 9
    for iters[0] in range(1,10):
        for iters[1] in range(1,10):
            for iters[2] in range(1,10):
                for iters[3] in range(1,10):
                    for iters[4] in range(1,10):
                        for iters[5] in range(1,10):
                            for iters[6] in range(1,10):
                                for iters[7] in range(1,10):
                                    for iters[8] in range(1,10):
                                        for i in range(9):
                                            book[iters[i]-1] = 1
                                        n = 0
                                        for i in range(9):
                                            n += book[i]
                                        if (n == 9) and (iters[0] * 100 + iters[1] * 10 + iters[2] +
                                            iters[3] * 100 + iters[4] * 10 + iters[5] == iters[6] * 100 + iters[7] * 10 + iters[8]):
                                            print "%d%d%d + %d%d%d = %d%d%d" %(iters[0], iters[1], iters[2], iters[3], iters[4], iters[5], iters[6], iters[7], iters[8])
                                        book = [0] * 9

equationWith9Nums()


