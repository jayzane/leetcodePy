"""
二叉树排序
2020-12-09: 16:12.99;05:30.08;02:39.92;
2020-12-10: 06:03.32;02:41.62;
"""
from sort import validatetool


def sort(data):
    class N:
        def __init__(self, v):
            self.v, self.l, self.r = v, None, None

    def insert(n, v):
        if n:
            if n.v < v:
                if n.r:
                    insert(n.r, v)
                else:
                    n.r = N(v)
            else:
                if n.l:
                    insert(n.l, v)
                else:
                    n.l = N(v)

    def ino(n, res):
        if n:
            ino(n.l, res)
            res.append(n.v)
            ino(n.r, res)

    l = len(data)
    if l <= 1:
        return data
    r = N(data[0])
    res = []
    for i in range(1, l):
        insert(r, data[i])
    ino(r, res)
    return res


if __name__ == '__main__':
    validatetool.validate(sort)
