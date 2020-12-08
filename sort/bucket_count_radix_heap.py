"""
桶、计数、基数、堆排序
2020-12-07: 39:46.45;13:22.93;11:01.96;11:48.41;
2020-12-08: 09:29.66;10:22.80
"""
from sort import validatetool

# 基数
def sort4(data):
    i = 0
    j = len(str(max(data)))
    while i < j:
        bs = [[] for _ in range(19)]
        for d in data:
            s = abs(d) // (10 ** i) % 10
            if d< 0:
                s = 9 -s
            else:
                s = 9 + s
            bs[s].append(d)
        data.clear()
        for b in bs:
            data.extend(b)
        i += 1
    return data

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
            if d[j] < p:
                d[i],d[j] = d[j],d[i]
                i += 1
        d[i],d[high] =d[high],d[i]
        return i

    l = len(data)
    maxv = max(data)
    minv = min(data)
    br = (maxv - minv) // l
    bs = [[] for _ in range(l + 1)]
    res = []
    for i in data:
        bs[(i - minv) // br].append(i)
    for b in bs:
        qs(b, 0, len(b) - 1)
        res.extend(b)
    return res


# 计数
def sort1(data):
    l = len(data)
    maxv = max(data)
    minv = min(data)
    tmp = [0 for _ in range(maxv - minv + 1)]
    res = [0 for _ in range(l)]
    for i in data:
        tmp[i -minv] += 1
    for i in range(1, len(tmp)):
        tmp[i] += tmp[i - 1]
    for i in data:
        res[tmp[i - minv] - 1] = i
        tmp[i - minv] -= 1
    return res



# 堆
def sort2(data):
    def hs(d):
        l = len(d)
        er = (l - 1) // 2
        for i in range(er, -1, -1):
            bd(d, i, l-1)
        for i in range(l - 1, 0, -1):
            d[i],d[0] = d[0],d[i]
            bd(d, 0, i - 1)

    def bd(d, root, end):
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and d[child + 1] > d[child]:
                child += 1
            if d[child] > d[root]:
                d[child],d[root] = d[root], d[child]
                root = child
            else:
                break
    hs(data)
    return data



if __name__ == '__main__':
    local_copy = locals().copy()
    for name, func in local_copy.items():
        if callable(func) and name.startswith('sort'):
            validatetool.validate(func)
