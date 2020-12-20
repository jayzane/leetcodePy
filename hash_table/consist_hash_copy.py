"""
一致性哈希算法: 哈希表槽位数（大小）的改变平均只需要对K/n 个关键字重新映射, K是关键字的数量，n是槽位数量
2020-12-20: 39:08.59;
"""
from hash_table.tools import get_hash
from hash_table.hash_table_with_linked_list_copy import HashTable


class Node:
    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return 'Node({})'.format(self.name)


class ConsistHash:
    def __init__(self, k=1000, replicas=3):
        self._k = k
        self._replicas = replicas
        self._hash_table = HashTable()
        self._sorted_keys = []

    def _hash(self, key):
        return get_hash(key, self._k)

    def _get_pos(self, hash_code):
        if not self._sorted_keys:
            return None, None
        for i in range(len(self._sorted_keys)):
            k = self._sorted_keys[i]
            if hash_code < k:
                return self._hash_table.get(k), i
        return self._hash_table.get(self._sorted_keys[0]), 0

    def add_node(self, key, node):
        for i in range(self._replicas):
            new_key = '{}#{}'.format(key, i)
            hash_code = self._hash(new_key)
            self._hash_table.put(hash_code, node)
            self._sorted_keys.append(hash_code)
            self._sorted_keys.sort()

    def get_node(self, key):
        hash_code = self._hash(key)
        node, _ = self._get_pos(hash_code)
        return node

    def delete_node(self, key):
        for i in range(self._replicas):
            new_key = '{}#{}'.format(key, i)
            hash_code = self._hash(new_key)
            if not self._hash_table.get(hash_code):
                continue
            self._hash_table.delete(hash_code)
            self._sorted_keys.remove(hash_code)

    def __repr__(self):
        return 'ConsistHash({})'.format([self._hash_table.get(k) for k in self._sorted_keys])


if __name__ == '__main__':
    ch = ConsistHash()
    for n in range(10):
        ch.add_node(str(n + 100), Node(str(n + 100)))
    print(ch)
    ch.delete_node('102')
    print(ch)
    val1 = ch.get_node('102')
    print(val1)
    val2 = ch.get_node('103')
    print(val2)
