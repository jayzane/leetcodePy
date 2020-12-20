"""
链表法哈希表
2020-12-19: 51:19.01;17:12.86;
2020-12-20: 11:16.00;
"""
from hash_table.tools import get_hash


class HTListNode:
    def __init__(self, key=None, val=None, next_n=None):
        self.key = key
        self.val = val
        self.next = next_n

    def __repr__(self):
        return 'HTListNode(key={},val={},next_n={})'.format(self.key, self.val,
                                                            (self.next.key, self.next.val) if self.next else None)


class HashTable:
    load_factor = 0.75
    init_capacity = 4

    def __init__(self):
        self.array = [None] * self.init_capacity
        self.use = 0

    def _hash(self, key):
        return get_hash(key, len(self.array))

    def _resize(self):
        old_array = self.array
        old_size = len(self.array)
        self.array = [None] * old_size * 2
        self.use = 0
        for i in range(old_size):
            old_curr = old_array[i]
            if old_curr is None or old_curr.next is None:
                continue
            hash_code = self._hash(old_curr.key)
            if self.array[hash_code] is None:
                self.array[hash_code] = HTListNode()
                self.use += 1
            curr = self.array[hash_code]
            while curr.next:
                curr = curr.next
            curr.next = HTListNode(old_curr.key, old_curr.val, curr.next)

    def put(self, key, val):
        hash_code = self._hash(key)
        new_code = HTListNode(key, val)
        if self.array[hash_code] is not None:
            curr = self.array[hash_code]
            while curr.next:
                curr = curr.next
                if curr.key == key:
                    curr.val = val
                    return
                curr.next = new_code
        else:
            self.array[hash_code] = HTListNode()
            self.use += 1
            self.array[hash_code].next = new_code
            if self.use >= (len(self.array) * self.load_factor):
                self._resize()

    def get(self, key):
        hash_code = self._hash(key)
        curr = self.array[hash_code]
        if curr is None or curr.next is None:
            return
        while curr.next:
            curr = curr.next
            if curr.key == key:
                return curr.val

    def delete(self, key):
        hash_code = self._hash(key)
        curr = self.array[hash_code]
        if curr is None or curr.next is None:
            return
        while curr.next:
            pre = curr
            curr = curr.next
            if curr.key == key:
                pre.next = pre.next.next

    def __repr__(self):
        return 'HashTable(array={})'.format(self.array)


if __name__ == '__main__':
    ht = HashTable()
    for n in range(10):
        ht.put(str(n + 100), n)
    print(ht)
    for k in ['102', '103', '104', '105', '106']:
        ht.delete(k)
    print(ht)
    ht.delete('1')
    print(ht)
    val1 = ht.get('107')
    print(val1)
