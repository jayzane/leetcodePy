"""
冒泡排序
2020-12-05: 0:53.06;0:45.17
"""
from sort import validatetool


def sort(data):
    l = len(data)
    for i in range(l):
        for j in range(l - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


if __name__ == '__main__':
    validatetool.validate(sort)
