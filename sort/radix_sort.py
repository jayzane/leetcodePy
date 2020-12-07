"""
基数排序
2020-12-07:18:03.25;02:18.81;01:48.08;
"""
from sort import validatetool


def sort(data):
    i = 0
    j = len(str(max(data)))
    while i < j:
        buckets = [[] for _ in range(19)]
        for d in data:
            s = abs(d) // (10 ** i) % 10
            if d >= 0:
                s = 9 + s
            else:
                s = 9 - s
            buckets[s].append(d)
        data.clear()
        for b in buckets:
            for x in b:
                data.append(x)
        i += 1
    return data


if __name__ == '__main__':
    validatetool.validate(sort)
