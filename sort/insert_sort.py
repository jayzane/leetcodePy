"""
插入排序
2020-12-05: 04:45.59;03:28.51;01:05.48;01:01.21;00:54.13
"""
from sort import validatetool


def sort(data):
    l = len(data)
    if l < 1:
        return data
    for i in range(1, l):
        val = data[i]
        for j in range(i - 1, -1, -1):
            if val < data[j]:
                data[j + 1] = data[j]
            else:
                data[j + 1] = val
                break
        else:
            data[0] = val
    return data


if __name__ == '__main__':
    validatetool.validate(sort)
