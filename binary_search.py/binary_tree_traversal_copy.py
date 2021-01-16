"""
二叉树先、中、后序遍历、深度（高度）、层次遍历的递归和循环实现
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @staticmethod
    def init_tree(nums):
        root = Node(nums[0])
        _s1 = [root]
        _s2 = []
        for i in range(1, len(nums)):
            if not _s1:
                while _s2:
                    _s1.append(_s2.pop())
            p = _s1.pop()
            if p.left is None:
                p.left = Node(nums[i])
                _s1.append(p)
            elif p.right is None:
                p.right = Node(nums[i])
                _s2.append(p.left)
                _s2.append(p.right)
        return root

    def __repr__(self):
        return 'Node({})'.format(self.val)


def preorder_recursive(node, res):
    if node:
        res.append(node.val)
        preorder_recursive(node.left, res)
        preorder_recursive(node.right, res)


def inorder_recursive(node, res):
    if node:
        inorder_recursive(node.left, res)
        res.append(node.val)
        inorder_recursive(node.right, res)


def postorder_recursive(node, res):
    if node:
        postorder_recursive(node.left, res)
        postorder_recursive(node.right, res)
        res.append(node.val)


def preorder_loop(node, res):
    _s = [node]
    while _s:
        p = _s.pop()
        if p is None:
            continue
        res.append(p.val)
        _s.append(p.right)
        _s.append(p.left)


def inorder_loop(node, res):
    _s = []
    p = node
    while p or _s:
        if p:
            _s.append(p)
            p = p.left
        else:
            p = _s.pop()
            res.append(p.val)
            p = p.right


def postorder_loop(node, res):
    _s = [node]
    _s2 = []
    while _s:
        p = _s.pop()
        if p is None:
            continue
        _s2.append(p)
        _s.append(p.left)
        _s.append(p.right)
    while _s2:
        res.append(_s2.pop().val)


def depth_recursive(node):
    def inner(p):
        if p:
            dl = inner(p.left)
            dr = inner(p.right)
            return 1 + max(dl, dr)
        return 0

    cnt = inner(node) - 1
    return cnt


def depth_loop(node):
    cnt = 0
    _s1 = []
    _s2 = [node]
    while _s2:
        curr = 0
        last = len(_s2)
        while curr < last:
            curr += 1
            p = _s2.pop()
            if p.left:
                _s1.append(p.left)
            if p.right:
                _s1.append(p.right)
        while _s1:
            _s2.append(_s1.pop())
        cnt += 1

    return cnt - 1


def layer_recursive(node, res):
    def inner(p, h):
        if h == -1 or not p:
            return
        if h == 0:
            res.append(p.val)
        inner(p.left, h - 1)
        inner(p.right, h - 1)

    high = depth_recursive(node)
    for i in range(high + 1):
        inner(node, i)


def layer_loop(node, res):
    _s1 = []
    _s2 = [node]
    while _s2:
        curr = 0
        last = len(_s2)
        while curr < last:
            curr += 1
            p = _s2.pop()
            res.append(p.val)
            if p.left:
                _s1.append(p.left)
            if p.right:
                _s1.append(p.right)
        while _s1:
            _s2.append(_s1.pop())


if __name__ == '__main__':
    t = Node.init_tree(range(10))

    res = []
    preorder_recursive(t, res)
    print(res)
    res = []
    preorder_loop(t, res)
    print(res)

    res = []
    inorder_recursive(t, res)
    print(res)
    res = []
    inorder_loop(t, res)
    print(res)

    res = []
    postorder_recursive(t, res)
    print(res)
    res = []
    postorder_loop(t, res)
    print(res)

    depth = depth_recursive(t)
    print(depth)
    depth = depth_loop(t)
    print(depth)

    res = []
    layer_recursive(t, res)
    print(res)

    res = []
    layer_loop(t, res)
    print(res)
