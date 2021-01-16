"""
使用数组、链表分别实现栈
2020-12-22: 22:40.23;
"""


class ArrayStack:

    def __init__(self, size=10):
        self._size = 10
        self._array = [None] * size
        self._cnt = 0

    def push(self, val):
        if self._cnt == self._size:
            return False
        self._array[self._cnt] = val
        self._cnt += 1
        return True

    def pop(self):
        if self._cnt == 0:
            return False
        val = self._array[self._cnt - 1]
        self._cnt -= 1
        return val

    def __repr__(self):
        return str(self._array)


class ListStack:
    def __init__(self):
        self._head = None

    def push(self, val):
        new_node = Node(val)
        if self._head is None:
            self._head = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        return True

    def pop(self):
        if self._head is None:
            return False
        val = self._head.val
        self._head = self._head.next
        return val

    def __repr__(self):
        vals = []
        p = self._head
        while p:
            vals.append(p)
            p = p.next
        return str(vals)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.val)


if __name__ == '__main__':
    a_stack = ArrayStack(10)
    l_stack = ListStack()
    for i in range(10):
        a_stack.push(i)
        l_stack.push(i)
    print(a_stack)
    print(l_stack)

    for _ in range(3):
        a_v = a_stack.pop()
        print('a_stack pop: {}'.format(a_v))
        l_v = l_stack.pop()
        print('l_stack pop: {}'.format(l_v))

    print(a_stack)
    print(l_stack)
