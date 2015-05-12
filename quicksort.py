__author__ = 'Su Lei'
import random as rd

# a = range(10)
# refer = 0
# rd.shuffle(a)
a = [5, 8, 3, 0, 1, 6, 9, 7, 2, 4]
refer = 0

def quicksort(left, right):
    print left, right
    if left > right:
        return
    r = a[left + refer]
    i = left
    j = right
    while i != j:

        while a[j] >= r and i < j :
            j -= 1
        while a[i] <= r and i < j :
            i += 1
        if i < j :
            # print a[i], a[j]
            a[i] = a[j] - a[i]
            a[j] -= a[i]
            a[i] += a[j]
        # print a

    a[left + refer] = a[i]
    a[i] = r
    quicksort(left, i-1)
    quicksort(i+1, right)

quicksort(0, len(a) - 1)
print a
