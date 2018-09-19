def quickSort(alist, first, last):
    if first >= last:
        return

    mid = alist[first]
    low = first
    high = last

    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid

    quickSort(alist, first, low-1)
    quickSort(alist, low+1, last)


if __name__ == '__main__':
    a = [91, 43, 52, 12, 73, 44, 10, 21, 5]
    quickSort(a, 0, len(a)-1)
    print(a)
