"""
冒泡、插入、选择排序
2020-12-05: 20.03.59;11:04.33;06:18.13;12:15.51;03:52.58;03:07.01;
"""
from sort import validatetool


# 选择
def sort1(data):
    l = len(data)
    for i in range(l):
        index = i
        for j in range(i + 1, l):
            if data[j] < data[index]:
                index = j
        data[i], data[index] = data[index], data[i]
    return data


# 插入
def sort2(data):
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


# 冒泡
def sort3(data):
    l = len(data)
    for i in range(l):
        for j in range(l - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


if __name__ == '__main__':
    validatetool.validate(sort1)
    validatetool.validate(sort2)
    validatetool.validate(sort3)
