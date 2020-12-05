"""
选择排序
2020-12-05: 9:15.65;2:21.00;1:17.56;1:02.98;2:06.27;0:48.95;
"""
from sort import validatetool


def sort(data):
    l = len(data)
    for i in range(l):
        index = i
        for j in range(i + 1, l):
            if data[j] < data[index]:
                index = j
        data[i], data[index] = data[index], data[i]
    return data


if __name__ == '__main__':
    validatetool.validate(sort)
