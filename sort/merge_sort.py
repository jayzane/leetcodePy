"""
归并排序
2020-12-06: 22:04.35;07:54.77;02:46.99;01:50.48;
2020-12-10: 05:11.03;01:31.73;02:45.53;01:59.04;
"""
from sort import validatetool


# TODO:归并的时候借用两次二分，right[0]在left中的位置，left[-1]在right中的位置


def sort(data):
    def ms(d):
        l = len(d)
        if l <= 1:
            return d
        m = l // 2
        left = ms(d[:m])
        right = ms(d[m:])
        return merge(left, right)

    def merge(left, right):
        if not left:
            return right
        if not right:
            return left
        if left[0] < right[0]:
            return [left[0]] + merge(left[1:], right)
        return [right[0]] + merge(left, right[1:])

    res = ms(data)
    return res


if __name__ == '__main__':
    validatetool.validate(sort)
