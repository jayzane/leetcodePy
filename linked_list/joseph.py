"""
约瑟夫问题:
n个人，一个人紧接着下一个人，指定一个人开始，每数k下，干掉一个，现在如果其中有m(m<k)个人不想被干掉，他们应该站在第几个位置？
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def joseph(n, k, m):
    ret = []
    # 几个参数有效范围，限定为整数
    if not (0 < m < k <= n and n > 1):
        return []
    # 初始化循环链表
    head = ListNode(1)
    i = 2
    p = head
    while i <= n:
        new_node = ListNode(i)
        p.next = new_node
        p = new_node
        i += 1
    p.next = head
    # 执行既定规则
    left = n  # 剩余人数
    prev = p
    p = head
    while left >= k:
        count = 1 # 计数
        while count <= k:
            if count == k:
                prev.next = prev.next.next  # 干掉
            count += 1
            prev = p
            p = p.next
        left -= 1
    # 查看幸存的人
    first = p
    second = None
    while first is not second:
        ret.append(p.val)
        p = p.next
        second = p

    return ret


if __name__ == '__main__':
    ret = joseph(2, 2, 1)
    print(ret)
    ret = joseph(40, 3, 2)
    print(ret)
    ret = joseph(40, 3, 7)
    print(ret)
