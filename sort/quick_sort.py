"""
快算排序
2020-12-06:32:21.82;07:32.25;02:12.94;
"""
from sort import validatetool


def sort(data):
    def quick_sort(d, low, high):
        if low < high:
            pi = partition(d, low, high)
            quick_sort(d, low, pi - 1)
            quick_sort(d, pi + 1, high)

    def partition(d, low, high):
        p = d[high]
        i = low
        for j in range(low, high):
            if d[j] < p:
                d[i], d[j] = d[j], d[i]
                i += 1
        d[i], d[high] = d[high], d[i]
        return i

    quick_sort(data, 0, len(data) - 1)
    return data


if __name__ == '__main__':
    validatetool.validate(sort)
