"""
使用哈希表、双向链表实现LRU（Least Recently Used）
2020-12-19: 27:15.42;
"""
from hash_table import HashTable


class DNode:
    def __init__(self, key=None, val=None, prev=None, next_n=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next_n

    def __repr__(self):
        return 'DNode(key={},val={})'.format(self.key, self.val)


class LRUHashTable:

    def __init__(self, capacity=4):
        self._length = 0
        self._capacity = capacity
        self._head = DNode()
        self._tail = DNode()
        self._head.next = self._tail
        self._tail.prev = self._head
        self._hash_table = HashTable()

    def _add_node(self, node):
        node.next = self._head.next
        node.prev = self._head
        self._head.next.prev = node
        self._head.next = node

    def _delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def delete(self, key):
        node = self._hash_table.get(key)
        if node is None:
            return
        self._hash_table.delete(key)
        self._delete_node(node)
        self._length -= 1

    def _move_head(self, node):
        self._delete_node(node)
        self._add_node(node)

    def _pop_tail(self):
        node = self._tail.prev
        self._delete_node(node)
        return node

    def add(self, key, val):
        old_node = self._hash_table.get(key)
        if old_node is not None:
            old_node.val = val
            self._move_head(old_node)
            return
        node = DNode(key, val)
        if self._length + 1 > self._capacity:
            self._pop_tail()
            self._length -= 1
        self._length += 1
        self._add_node(node)
        self._hash_table.put(key, node)

    def get(self, key):
        node = self._hash_table.get(key)
        if node is None:
            return
        self._move_head(node)
        return node.val

    def __repr__(self):
        vals = []
        curr = self._head
        while curr:
            vals.append(str(curr))
            curr = curr.next
        return str(vals)


if __name__ == '__main__':
    lru = LRUHashTable()
    for i in range(10):
        lru.add(str(i + 100), i)
    print(lru)
    lru.add('103', 30)
    print(lru)
    lru.delete('103')
    print(lru)
    val1 = lru.get('101')
    print(val1)
    print(lru)
    val2 = lru.get('109')
    print(val2)
    print(lru)
