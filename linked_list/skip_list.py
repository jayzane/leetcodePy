"""
跳表
Redis的有序集合会用到
特点：
查找、删除、插入：O(log(n))
空间: O(n)
与红黑树比较:
查找、删除、插入都是O(log(n))
但是跳表 按照区间查找数据（比如查找值在[100, 356]之间的数据）比红黑树效率高
2020-12-18: 36.09.60;19.04.14;07:46.69;
"""
import random


class SkipListNode:
    def __init__(self, val, high):
        self.val = val
        self.deeps = [None] * high

    def __repr__(self):
        return 'Node(val={},deep={})'.format(self.val, len(self.deeps) - 1)


class SkipList:
    _max_high = 4

    def __init__(self):
        self._high = 1
        self._head = SkipListNode(None, self._max_high)

    def random_high(self, p=0.25):
        high = 1
        while high < self._max_high and random.random() < p:
            high += 1
        return high

    def find(self, val):
        curr = self._head
        for i in range(self._high - 1, -1, -1):
            while curr.deeps[i] and curr.deeps[i].val < val:
                curr = curr.deeps[i]
        if curr.deeps[i] and curr.deeps[i].val == val:
            return curr.deeps[i]

    def insert(self, val):
        if self._high == 1:
            high = self._high = self._high + 1
        else:
            high = self.random_high()
            if high > self._high and self._high < self._max_high:
                high = self._high = self._high + 1
        curr = self._head
        new_node = SkipListNode(val, high)
        for i in range(high - 1, -1, -1):
            while curr.deeps[i] and curr.deeps[i].val < val:
                curr = curr.deeps[i]
            new_node.deeps[i] = curr.deeps[i]
            curr.deeps[i] = new_node

    def delete(self, val):
        curr = self._head
        for i in range(self._high - 1, -1, -1):
            while curr.deeps[i] and curr.deeps[i].val < val:
                curr = curr.deeps[i]
            if curr.deeps[i] and curr.deeps[i].val == val:
                curr.deeps[i] = curr.deeps[i].deeps[i]

    def __repr__(self):
        vals = []
        for i in range(self._high - 1, -1, -1):
            val = []
            curr = self._head.deeps[i]
            while curr:
                val.append(str(curr.val))
                curr = curr.deeps[i]
            vals.append('-->'.join(val))
        return str(vals)


if __name__ == '__main__':
    s_list = SkipList()
    for n in range(20):
        s_list.insert(n)
    pi = s_list.find(8)
    print(pi)
    print(s_list)
    s_list.delete(10)
    print(s_list)
    s_list.delete(7)
    print(s_list)
    s_list.delete(5)
    print(s_list)
