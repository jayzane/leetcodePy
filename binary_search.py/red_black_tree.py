"""
LLRB 左倾红黑树 left-lean red black tree
"""

RED = True
BLACK = False


class Nil:
    def __init__(self):
        self.val = False
        self.left = None
        self.right = None
        self.color = BLACK

    def __bool__(self):
        return False

    def is_red(self):
        return self.color is RED

    def is_nil(self):
        return True

    def __repr__(self):
        return 'Nil'


class Node:
    def __init__(self, val, color=RED):
        # key val 一样
        self.val = val
        self.left = Nil()
        self.right = Nil()
        self.color = color

    def is_red(self):
        return self.color is RED

    def is_nil(self):
        return False

    def __repr__(self):
        return 'Node({},{})'.format(self.val, 'red' if self.is_red() else 'black')


class LeftLeanRedBlackTree:
    def __init__(self):
        self.root = Nil()

    def search(self, val):
        p = self.root
        while p and p.val != val:
            if val < p.val:
                p = p.left
            else:
                p = p.right
        return p.val

    def insert(self, val):
        def _insert(p):
            if not p:
                return new_node
            if val < p.val:
                p.left = _insert(p.left)
            elif val > p.val:
                p.right = _insert(p.right)
            else:
                p.val = val
            p = self.fix_up(p)
            return p

        new_node = Node(val)
        self.root = _insert(self.root)
        self.root.color = BLACK

    def fix_up(self, p):
        if p.right.is_red():
            p = self.rotate_left(p)
        if p.left.is_red() and p.left.left.is_red():
            p = self.rotate_right(p)
        if p.left.is_red() and p.right.is_red():
            self.color_flip(p)
        return p

    def delete(self, val):
        def _delete(p):
            if not p:
                return Nil()
            if val < p.val:
                if not p.left.is_red() and not p.left.left.is_red():
                    p = self.move_red_left(p)
                p.left = _delete(p.left)
            else:
                if p.left.is_red():
                    p = self.rotate_right(p)
                if val == p.val and not p.right:
                    return Nil()
                if not p.right.is_red() and not p.right.left.is_red():
                    p = self.move_red_right(p)
                if val == p.val:
                    p.val = self.get_min(p.right)
                    p.right = self._delete_min(p.right)
                else:
                    p.right = _delete(p.right)
            return self.fix_up(p)

        self.root = _delete(self.root)
        self.root.color = BLACK

    def get_min(self, p):
        while p and p.left:
            p = p.left
        return p.val

    def _delete_min(self, p):
        if not p.left:
            return Nil()
        if not p.is_red() and not p.left.is_red():
            p = self.move_red_left(p)
        p.left = self._delete_min(p.left)
        return self.fix_up(p)

    def delete_min(self):
        self.root = self._delete_min(self.root)
        self.root.color = BLACK

    def move_red_left(self, p):
        self.color_flip(p)
        if p.right.left.is_red():
            p.right = self.rotate_right(p.right)
            p = self.rotate_left(p)
            self.color_flip(p)
        return p

    def move_red_right(self, p):
        self.color_flip(p)
        if p.left.left.is_red():
            p = self.rotate_right(p)
            self.color_flip(p)
        return p

    def color_flip(self, p):
        p.color = not p.color
        p.left.color = not p.left.color
        p.right.color = not p.right.color

    def rotate_left(self, p):
        x = p.right
        p.right = x.left
        x.left = p
        x.color = x.left.color
        x.left.color = RED
        return x

    def rotate_right(self, p):
        x = p.left
        p.left = x.right
        x.right = p
        x.color = x.right.color
        x.right.color = RED
        return x

    def __repr__(self, p='root', level=0):
        if p == 'root':
            p = self.root
        ret = '\t' * level + repr(p) + '\n'
        if p.left is not None:
            ret += self.__repr__(p.left, level + 1)
        if p.right is not None:
            ret += self.__repr__(p.right, level + 1)
        return ret


if __name__ == '__main__':
    llrb = LeftLeanRedBlackTree()
    for i in range(10):
        llrb.insert(i)
    print(llrb)

    v1 = llrb.search(6)
    print(v1)

    v1 = llrb.search(16)
    print(v1)

    llrb.delete_min()
    print(llrb)

    llrb.delete(7)
    print(llrb)
