"""
希尔、归并、快速排序
2020-12-06: 12:51.26;08:01.44;
"""
from sort import validatetool


# 快速
def sort1(data):
    def quick_sort(d, low, high):
        if low < high:
            pi = partition(d, low, high)
            quick_sort(d, low, pi - 1)
            quick_sort(d, pi + 1, high)

    def partition(d, low, high):
        p = d[high]
        i = low
        for j in range(low, high):
            if d[j] < p:
                d[i], d[j] = d[j], d[i]
                i += 1
        data[i], data[high] = data[high], data[i]
        return i

    quick_sort(data, 0, len(data) - 1)
    return data


# 归并
def sort2(data):
    def merge_sort(d):
        l = len(d)
        if l <= 1:
            return d
        m = l // 2
        left = merge_sort(d[:m])
        right = merge_sort(d[m:])
        return merge(left, right)

    def merge(left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:]
        res += right[j:]
        return res

    return merge_sort(data)


# 希尔
def sort3(data):
    l = len(data)
    gap = l // 2
    while gap > 0:
        for i in range(gap, l):
            val = data[i]
            j = i - gap
            while j >= 0 and val < data[j]:
                data[j + gap] = data[j]
                j -= gap
            data[j + gap] = val
        gap //= 2
    return data


if __name__ == '__main__':
    validatetool.validate(sort1)
    validatetool.validate(sort2)
    validatetool.validate(sort3)
