def shellSort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i >= gap:
                if alist[i] < alist[i-gap]:
                    alist[i-gap], alist[i] = alist[i], alist[i-gap]
                    i -= gap
                else:
                    break
        gap //= 2
    return alist


a = [91, 43, 52, 12, 73, 44, 10, 21, 5]
print(shellSort(a))
