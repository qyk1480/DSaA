def selectSort(alist):
    for j in range(len(alist)-1):
        min = j
        for i in range(j+1, len(alist)):
            if alist[i] < alist[min]:
                min = i
        alist[j], alist[min] = alist[min], alist[j]
    return alist


a = [91, 43, 52, 12, 73, 44, 10, 21]
print(selectSort(a))
