"""
数组的插入、删除、下标访问
栈的数组、链表实现
队列的数组、链表实现
循环队列
"""


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __repr__(self):
        return 'Node({})'.format(self.val)


class Array:
    def __init__(self, size=10):
        self._size = size
        self._array = [None] * size
        self._cnt = 0

    def find(self, index):
        if index >= self._size or index < 0:
            return False
        return self._array[index]

    def insert(self, index, val):
        if index >= self._size or index < 0 or self._cnt == self._size:
            return False
        for i in range(self._cnt - 1, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = val
        self._cnt += 1

    def delete(self, index):
        if index >= self._size or index < 0:
            return False
        for i in range(index + 1, self._cnt):
            self._array[i - 1] = self._array[i]
        self._cnt -= 1

    def __repr__(self):
        return 'cnt:{},{}'.format(self._cnt, str(self._array))


class ArrayStack:
    def __init__(self, size=10):
        self._size = 10
        self._array = [None] * 10
        self._cnt = 0

    def push(self, val):
        if self._cnt == self._size:
            return False
        self._array[self._cnt] = val
        self._cnt += 1

    def pop(self):
        if self._cnt == 0:
            return False
        val = self._array[self._cnt - 1]
        self._cnt -= 1
        return val

    def __repr__(self):
        return 'cnt:{},{}'.format(self._cnt, str(self._array))


class ListStack:
    def __init__(self):
        self._head = None

    def push(self, val):
        new_node = Node(val)
        if not self._head:
            self._head = new_node
            return
        new_node.next = self._head
        self._head = new_node

    def pop(self):
        if not self._head:
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


class ArrayQueue:
    def __init__(self, size=10):
        self._size = size
        self._array = [None] * size
        self._head = 0
        self._tail = 0

    def push(self, val):
        if self._tail == self._size:
            if self._head == 0:
                return False
            for i in range(self._head, self._tail):
                self._array[i - self._head] = self._array[i]
            self._tail -= self._head
            self._head = 0

        self._array[self._tail] = val
        self._tail += 1

    def pop(self):
        if self._head == self._tail:
            return False
        val = self._array[self._head]
        self._head += 1
        return val

    def __repr__(self):
        return 'h:{},t:{},{}'.format(self._head, self._tail, self._array)


class ListQueue:
    def __init__(self):
        self._head = None
        self._tail = None

    def push(self, val):
        new_node = Node(val)
        if not self._head:
            self._head = self._tail = new_node
            return
        self._tail.next = new_node
        self._tail = new_node

    def pop(self):
        if not self._head:
            return False
        val = self._head.val
        self._head = self._head.next
        if not self._head:
            self._tail = None
        return val

    def __repr__(self):
        vals = []
        p = self._head
        while p:
            vals.append(p)
            p = p.next
        return str(vals)


class LoopArrayQueue:
    def __init__(self, size=10):
        self._size = size
        self._array = [None] * size
        self._head = 0
        self._tail = 0

    def push(self, val):
        if (self._tail + 1) % self._size == self._head:
            return False
        self._array[self._tail] = val
        self._tail = (self._tail + 1) % self._size

    def pop(self):
        if self._head == self._tail:
            return False
        val = self._array[self._head]
        self._head = (self._head + 1) % self._size
        return val

    def __repr__(self):
        return 'h:{},t:{},{}'.format(self._head, self._tail, self._array)


if __name__ == '__main__':
    a1 = Array(size=10)
    for n in range(20):
        a1.insert(n, n)
    print(a1)
    v1 = a1.find(5)
    print(v1)
    v2 = a1.find(19)
    print(v2)
    a1.delete(7)
    a1.delete(19)
    print(a1)
    print('---------')
    s1 = ArrayStack(size=10)
    for n in range(20):
        s1.push(n)
    print(s1)
    v1 = s1.pop()
    print(v1)
    v2 = None
    for _ in range(20):
        v2 = s1.pop()
    print(v2)
    print(s1)

    s1 = ListStack()
    for n in range(20):
        s1.push(n)
    print(s1)
    v1 = s1.pop()
    print(v1)
    print(s1)
    v2 = None
    for _ in range(20):
        v2 = s1.pop()
    print(v2)
    print(s1)
    print('---------')
    q1 = ArrayQueue(size=10)
    for n in range(20):
        q1.push(n)
    print(q1)
    v1 = q1.pop()
    print(v1)
    print(q1)
    v2 = None
    for _ in range(20):
        v2 = q1.pop()
    print(v2)
    print(q1)
    for n in range(3):
        q1.push(-n)
    print(q1)

    q1 = ListQueue()
    for n in range(20):
        q1.push(n)
    print(q1)
    v1 = q1.pop()
    print(v1)
    print(q1)
    v2 = None
    for _ in range(20):
        v2 = q1.pop()
    print(v2)
    print(q1)
    for n in range(3):
        q1.push(-n)
    print(q1)

    print('--------')
    q1 = LoopArrayQueue(size=10)
    for n in range(20):
        q1.push(n)
    print(q1)
    v1 = q1.pop()
    print(v1)
    print(q1)
    v2 = None
    for _ in range(20):
        v2 = q1.pop()
    print(v2)
    print(q1)
    for n in range(3):
        q1.push(-n)
    print(q1)
