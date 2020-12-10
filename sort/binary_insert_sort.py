"""
折半插入排序
2020-12-09:15:03.51;03:05.42;01:20.25;01:31.53;01:18.20;
"""
from sort import validatetool


def sort(data):
    l = len(data)
    for i in range(1, l):
        val = data[i]
        low = 0
        high = i - 1
        while low <= high:
            m = (low + high) // 2
            if data[m] > val:
                high = m - 1
            else:
                low = m + 1
        for j in range(i - 1, low - 1, -1):
            data[j + 1] = data[j]
        data[low] = val
    return data


if __name__ == '__main__':
    sort([1, 2])
    # validatetool.validate(sort)
