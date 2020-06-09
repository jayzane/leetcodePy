import copy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    给定一个链表，判断链表中是否有环。
    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
    example1:
    输入：head = [3,2,0,-4], pos = 1
    输出：true
    解释：链表中有一个环，其尾部连接到第二个节点。
    example2:
    输入：head = [1,2], pos = 0
    输出：true
    解释：链表中有一个环，其尾部连接到第一个节点。
    example3:
    输入：head = [1,2], pos = 0
    输出：true
    解释：链表中有一个环，其尾部连接到第一个节点。
    """

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pass


def has_cycle_back(head: ListNode) -> bool:
    """
    O(n2)
    :param head: ListNode
    :return: bool
    >>> has_cycle_back(node4)
    True
    >>> has_cycle_back(node11)
    True
    >>> has_cycle_back(node21)
    False
    """
    # 一切算法转暴力枚举
    index1 = 0
    node = head
    while node:
        node_next = node.next
        node_tmp = head
        for _ in range(index1):
            if node_tmp is node_next:
                return True
            node_tmp = node_tmp.next
        node = node_next
        index1 += 1
    return False


def has_cycle(head: ListNode) -> bool:
    """
    O(n)
    :param head: ListNode
    :return: bool
    >>> has_cycle(node4)
    True
    >>> has_cycle(node11)
    True
    >>> has_cycle(node21)
    False
    """
    # 使用try-except也太geek了点儿
    # 可以这样写
    # low, fast = head, head
    # while fast and fast.next:
    #     low, fast = low.next, fast.next.next
    #     if low == fast:
    #         return True
    # return False
    try:
        slow = head.next
        fast = head.next.next
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except AttributeError:
        return False


def has_cycle_hash(head: ListNode) -> bool:
    """
    使用哈希表
    时间复杂：O(n)
    空间复杂: O(n)
    :param head: ListNode
    :return: bool
    >>> has_cycle(node4)
    True
    >>> has_cycle(node11)
    True
    >>> has_cycle(node21)
    False
    """
    if head is None or head.next is None:
        return False
    hash_map = set()
    p = head
    while p:
        if p in hash_map:
            return True
        hash_map.add(p)
        p = p.next


if __name__ == '__main__':
    import doctest

    # 输入：head = [0, 1, 2, 3], pos = 1
    node1 = ListNode(3)
    node2 = ListNode(2)
    node2.next = node1
    node3 = ListNode(1)
    node3.next = node2
    node4 = ListNode(0)
    node4.next = node3
    node1.next = node3

    # 输入：head = [1, 2], pos = 0
    node11 = ListNode(1)
    node12 = ListNode(2)
    node11.next = node12
    node12.next = node11

    # 输入：head = [1, 2], pos = -1
    node21 = ListNode(1)
    node22 = ListNode(2)
    node21.next = node22

    doctest.testmod()
