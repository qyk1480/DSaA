def mergeSort(alist):
    n = len(alist)
    if n <= 1:
        return alist

    mid = n // 2
    lli = mergeSort(alist[:mid])
    rli = mergeSort(alist[mid:])

    lp = rp = 0
    result = []

    while lp < len(lli) and rp < len(rli):
        if lli[lp] < rli[rp]:
            result.append(lli[lp])
            lp += 1
        else:
            result.append(rli[rp])
            rp += 1
    result += lli[lp:]
    result += rli[rp:]
    return result


if __name__ == '__main__':
    a = [91, 43, 52, 12, 73, 44, 10, 21, 5]
    print(mergeSort(a))
