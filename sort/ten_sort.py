"""
十大计数
2020-12-08: 56:44.05;27:50.42;
"""
from sort import validatetool


def sort10(data):
    # 堆
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


def sort2(data):
    # 冒泡
    l = len(data)
    for i in range(l):
        for j in range(l - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def sort4(data):
    # 希尔
    l = len(data)
    gap = l // 2
    while gap > 0:
        for i in range(l):
            val = data[i]
            j = i - 1
            while j >= 0 and val < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = val
        gap //= 2
    return data


def sort8(data):
    # 计数
    l = len(data)
    maxv = max(data)
    minv = min(data)
    tmp = [0 for _ in range(maxv - minv + 1)]
    res = [0 for _ in range(l)]
    for i in data:
        tmp[i - minv] += 1
    for i in range(1, len(tmp)):
        tmp[i] += tmp[i - 1]
    for i in data:
        res[tmp[i - minv] - 1] = i
        tmp[i - minv] -= 1
    return res


def sort6(data):
    # 归并
    def ms(d):
        l = len(d)
        if l <= 1:
            return d
        m = l // 2
        left = ms(d[:m])
        right = ms(d[m:])
        return merge(left, right)

    def merge(left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res

    return ms(data)


def sort3(data):
    # 插入
    l = len(data)
    for i in range(l):
        val = data[i]
        j = i - 1
        while j >= 0 and val < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = val
    return data


def sort9(data):
    # 基数
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


def sort1(data):
    # 选择
    l = len(data)
    for i in range(l):
        index = i
        for j in range(i, l):
            if data[j] < data[index]:
                index = j
        data[i], data[index] = data[index], data[i]
    return data


def sort5(data):
    # 快速
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
                d[i], d[j] = d[j], d[i]
                i += 1
        data[i], data[high] = d[high], d[i]
        return i

    qs(data, 0, len(data) - 1)
    return data


def sort7(data):
    # 桶
    l = len(data)
    maxv = max(data)
    minv = min(data)
    br = (maxv - minv) // l
    bs = [[] for _ in range(l + 1)]
    res = []
    for i in data:
        bs[(i - minv) // br].append(i)
    for b in bs:
        sort5(b)
        res.extend(b)
    return res


if __name__ == '__main__':
    local_copy = locals().copy()
    for name, func in local_copy.items():
        if callable(func) and name.startswith('sort'):
            validatetool.validate(func)
