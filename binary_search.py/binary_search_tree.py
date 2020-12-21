"""
二叉搜索树
2020-12-21: 37:26.34;09:45.54;
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node(val={})'.format(self.val)


class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        p = self.root
        while p:
            if p.val < val:
                if p.right:
                    p = p.right
                else:
                    p.right = Node(val)
                    break
            else:
                if p.left:
                    p = p.left
                else:
                    p.left = Node(val)
                    break

    def find(self, val):
        p = self.root
        while p:
            if p.val < val:
                p = p.right
            elif p.val > val:
                p = p.left
            else:
                return p

    def delete(self, val):
        p = self.root
        pp = None
        while p and p.val != val:
            pp = p
            if p.val < val:
                p = p.right
            elif p.val > val:
                p = p.left
        if p is None:
            return
        if p.left is not None and p.right is not None:
            min_pp = None
            min_p = p.right
            while min_p and min_p.left:
                min_pp = min_p
                min_p = min_p.left
            p.val = min_p.val
            p = min_p
            pp = min_pp
        if p.left:
            child = p.left
        else:
            child = p.right
        if pp is None:
            self.root = child
        elif pp.left is p:
            pp.left = child
        else:
            pp.right = child

    def __repr__(self):
        vals = []

        def _b(n):
            if n:
                _b(n.left)
                vals.append(str(n))
                _b(n.right)

        _b(self.root)
        return str(vals)


if __name__ == '__main__':
    t = BSTree()
    for d in [10, 5, 39, 3, 66, 6]:
        t.insert(d)
    print(t)
    n1 = t.find(3)
    print(n1)
    t.delete(39)
    print(t)
