"""
桶排序
2020-12-06: 08:49.19;12:04.67;04:25.56;03:00.90;
"""
from sort import validatetool


def sort(data):
    def qs(d, low, high):
        if low < high:
            pi = part(d, low, high)
            qs(d, low, pi - 1)
            qs(d, pi + 1, high)

    def part(d, low, high):
        i = low
        p = d[high]
        for j in range(low, high):
            if d[j] < p:
                d[j], d[i] = d[i], d[j]
                i += 1
        d[i], d[high] = d[high], d[i]
        return i

    minv = min(data)
    maxv = max(data)
    l = len(data)
    res = []
    br = (maxv - minv) // l
    bs = [[] for _ in range(l + 1)]
    for i in data:
        bs[(i - minv) // br].append(i)
    for b in bs:
        qs(b, 0, len(b) - 1)
        for i in b:
            res.append(i)
    return res


if __name__ == '__main__':
    validatetool.validate(sort)
