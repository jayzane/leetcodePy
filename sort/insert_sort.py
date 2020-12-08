"""
插入排序
2020-12-05: 04:45.59;03:28.51;01:05.48;01:01.21;00:54.13
2020-12-06: 0:55.39;0:50.86;
"""
from sort import validatetool


def sort(data):
    l = len(data)
    for i in range(l):
        val = data[i]
        j = i - 1
        while j >= 0 and val < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = val
    return data


if __name__ == '__main__':
    validatetool.validate(sort)
