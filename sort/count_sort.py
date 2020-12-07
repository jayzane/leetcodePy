"""
计数排序
2020-12-06: 06:39.10;01:56.83;01:19.87;
"""
from sort import validatetool


def sort(data):
    minv = min(data)
    maxv = max(data)
    tmp = [0 for _ in range(maxv - minv + 1)]
    res = [0 for _ in range(len(data))]
    for i in data:
        tmp[i - minv] += 1
    for i in range(1, len(tmp)):
        tmp[i] += tmp[i -1]
    for i in data:
        res[tmp[i - minv] - 1] = i
        tmp[i - minv] -= 1
    return res


if __name__ == '__main__':
    validatetool.validate(sort)
