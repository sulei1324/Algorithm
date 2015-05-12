__author__ = 'Su Lei'

def collatz(n, a=[]):
    a = a + [n]
    return len(a) if 1 == n else collatz(n / 2 if n % 2 == 0 else 3 * n + 1, a)
