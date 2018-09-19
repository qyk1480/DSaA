def bubbleSort(alist):
    count = 0
    for j in range(len(alist)-1):
        for i in range(len(alist)-1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            return alist
    return alist


a = [91, 43, 52, 12, 73, 44, 10, 21]
print(bubbleSort(a))
