def binarySearch(alist, item):
    """二分查找，递归"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binarySearch(alist[:mid], item)
        else:
            return binarySearch(alist[mid+1:], item)
    return False


def binarySearch2(alist, item):
    """二分查找，非递归"""
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    a = [5, 10, 12, 21, 43, 44, 52, 73, 91]
    print(binarySearch(a, 52))
    print(binarySearch2(a, 52))
