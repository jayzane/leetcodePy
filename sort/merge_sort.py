"""
归并排序
2020-12-06: 22:04.35;07:54.77;02:46.99;01:50.48;
"""
from sort import validatetool


def sort(data):
    def ms(d):
        l = len(d)
        if l <= 1:
            return d
        m = l // 2
        left = ms(d[:m])
        right = ms(d[m:])
        return merge(left, right)

    def merge(l, r):
        i = 0
        j = 0
        res = []
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        res += l[i:]
        res += r[j:]
        return res

    return ms(data)



if __name__ == '__main__':
    validatetool.validate(sort)
