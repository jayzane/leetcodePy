"""
堆排序
2020-12-07:15:09.50;10:16.98;12:58.02:05:34.47;02:46.53;
"""
from sort import validatetool


def sort(data):
    def heap_sort(d):
        l = len(d)
        end_root = (l - 1) // 2
        for i in range(end_root, -1, -1):
            build(d, i, l - 1)
        for i in range(l - 1, 0, -1):
            d[i], d[0] = d[0], d[i]
            build(d, 0, i - 1)

    def build(d, root, end):
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

    heap_sort(data)
    return data


if __name__ == '__main__':
    validatetool.validate(sort)
