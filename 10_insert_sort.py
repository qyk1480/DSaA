def insertSort(alist):
    for j in range(1, len(alist)):
        i = j
        # while i > 0:
        for i in range(i, 0, -1):
            if alist[i] < alist[i-1]:
                alist[i-1], alist[i] = alist[i], alist[i-1]
                # i -= 1
            else:
                break

    return alist


a = [91, 43, 52, 12, 73, 44, 10, 21]
print(insertSort(a))
