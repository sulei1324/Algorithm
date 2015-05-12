__author__ = 'Su Lei'
import numpy as np

def creatSnake(n):
    t = np.zeros((n, n))
    i = 0
    j = n - 1
    con = 1
    t[i][j] = con
    while con < n * n:
        print con, i, j
        while i + 1 < n and not t[i+1][j]:
            i += 1
            con += 1
            t[i][j] = con

        while j - 1 >= 0 and not t[i][j-1]:
            j -= 1
            con += 1
            t[i][j] = con

        while i - 1 >= 0 and not t[i-1][j]:
            i -= 1
            con += 1
            t[i][j] = con

        while j + 1 < n and not t[i][j+1]:
            j += 1
            con += 1
            t[i][j] = con

    return t


a = 8
print creatSnake(a)