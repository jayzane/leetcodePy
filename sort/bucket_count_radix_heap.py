"""
桶、计数、基数、堆排序
2020-12-07: 39:46.45;13:22.93;11:01.96;
"""
from sort import validatetool


# 桶
def sort3(data):
    def qs(d, low, high):
        if low < high:
            pi = part(d, low, high)
            qs(d, low, pi - 1)
            qs(d, pi + 1, high)

    def part(d, low, high):
        i = low
        p = d[high]
        for j in range(low, high):
            if d[j] <= p:
                d[i], d[j] = d[j], d[i]
                i += 1
        d[i], d[high] = d[high], d[i]
        return i

    max_v = max(data)
    min_v = min(data)
    l = len(data)
    br = (max_v - min_v) // l
    bs = [[] for _ in range(l + 1)]
    res = []
    for i in data:
        bs[(i - min_v) // br].append(i)
    for b in bs:
        qs(b, 0, len(b) - 1)
        res.extend(b)
    return res


# 堆
def sort2(data):
    def hs(d):
        l = len(d)
        er = (l - 1) // 2
        for i in range(er, -1, -1):
            bd(d, i, l - 1)
        for i in range(l - 1, 0, -1):
            d[i], d[0] = d[0], d[i]
            bd(d, 0, i - 1)

    def bd(d, root, end):
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and d[child + 1] > d[child]:
                child += 1
            if d[child] > d[root]:
                d[child], d[root] = d[root], d[child]
                root = child
            else:
                break

    hs(data)
    return data


# 基数
def sort4(data):
    i = 0
    j = len(str(max(data)))
    while i < j:
        bs = [[] for _ in range(19)]
        for d in data:
            s = abs(d) // (10 ** i) % 10
            if d < 0:
                s = 9 - s
            else:
                s = 9 + s
            bs[s].append(d)
        data.clear()
        for b in bs:
            data.extend(b)

        i += 1
    return data


# 计数
def sort1(data):
    max_v = max(data)
    min_v = min(data)
    l = len(data)
    tmp = [0 for _ in range(max_v - min_v + 1)]
    res = [0 for _ in range(l)]
    for i in data:
        tmp[i - min_v] += 1
    for i in range(1, len(tmp)):
        tmp[i] += tmp[i - 1]
    for i in data:
        res[tmp[i - min_v] - 1] = i
        tmp[i - min_v] -= 1
    return res


if __name__ == '__main__':
    local_copy = locals().copy()
    for name, func in local_copy.items():
        if callable(func) and name.startswith('sort'):
            validatetool.validate(func)
