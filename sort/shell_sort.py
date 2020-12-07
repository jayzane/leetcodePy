"""
希尔排序
2020-12-06: 11:02.30;
"""
from sort import validatetool


def sort(data):
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
    validatetool.validate(sort)
