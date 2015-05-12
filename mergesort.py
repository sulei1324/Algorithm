__author__ = 'Su Lei'


def mergesort(Arr, Brr):
    iA = 0
    iB = 0
    Rrr = [0] * (len(Arr) + len(Brr))
    if len(Arr) is 0 or len(Brr) is 0:
        print Arr + Brr
        return Arr + Brr
    for i in xrange((len(Arr) + len(Brr))):
        if Arr[iA] > Brr[iB]:
            Rrr[i] = Brr[iB]
            iB += 1
        else:
            Rrr[i] = Arr[iA]
            iA += 1
        if iA >= len(Arr):
            Rrr[i + 1:len(Rrr)] = Brr[iB:len(Brr)]
            break
        elif iB >= len(Brr):
            Rrr[i + 1:len(Rrr)] = Arr[iA:len(Arr)]
            break
    print Rrr
    return Rrr

def iterbody(arr, n):
    if 2**(n - 1) >= len(arr):
        return
    else:
        for i in xrange(0, len(arr), 2 ** n):
            As = i
            Ae = i + 2**(n-1) if (i + 2**(n-1)) < (len(arr)) else len(arr)
            Bs = Ae
            Be = i + 2 ** n if (i + 2 ** n) < (len(arr)) else len(arr)
            Arr = arr[As:Ae]
            Brr = arr[Bs:Be] if Bs < len(arr) else []
            print Arr, Brr
            arr[As:Be] = mergesort(Arr, Brr)
        iterbody(arr, n + 1)

t = [10, 21, 13, 4, 11, 33, 5, 192, 84]
iterbody(t, 1)
print t



