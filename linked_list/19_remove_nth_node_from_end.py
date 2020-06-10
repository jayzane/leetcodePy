"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
"""
from common.init_data import ListNode, init_list_node, print_list_node, algorithm_func_multi_exec, linked_examples


class Solution:
    """
    一次遍历
    使用哈希表记录每个位置对应的结点，再将对应结点的前驱点接上其后继点
    时间复杂度:O(n)，n是链表长度
    空间复杂度:O(n)
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # n有效检验
        if n <= 0:
            return head
        p = head
        hash_map = {}
        count = 0
        while p:
            count += 1
            hash_map[count] = p
            p = p.next
        # n有效检验
        if n > count:
            return head
        # 删除点的前驱点
        prev_cnt = count - n
        # 只有一个结点，并且被删除
        if count == 1:
            return None
        elif prev_cnt == 0:
            # 删除头结点
            return hash_map[prev_cnt + 1 + 1]
        hash_map[prev_cnt].next = hash_map[prev_cnt].next.next  # 包括了删除尾结点的情况
        return head


class SolutionA:
    """
    优化Solution，使用哨兵结点
    时间复杂度:O(n)
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # n有效检验
        if n <= 0 or head is None:  # head为空表情况
            return head
        pre_head = ListNode(-1)
        pre_head.next = head
        p = pre_head
        hash_map = {}
        count = -1
        while p:
            count += 1
            hash_map[count] = p
            p = p.next
        # n有效检验
        if n > count:
            return head
        # 删除点的前驱点
        prev_cnt = count - n
        # 使用哨兵，减少了一些判断
        hash_map[prev_cnt].next = hash_map[prev_cnt].next.next
        return pre_head.next


class SolutionB:
    """
    两次遍历，删除倒数n个结点相当于删除第l-n个结点
    时间复杂度:O(n)
    空间复杂度:O(1)
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # n有效检验
        if n <= 0:
            return head
        pre_head = ListNode(-1)
        pre_head.next = head
        p = pre_head
        count = -1
        # 计数
        while p:
            count += 1
            p = p.next
        # n有效检验
        if n > count:
            return head
        p = pre_head
        count = count - n  # 这个是删除点的前驱点
        while count > 0:
            count -= 1
            p = p.next
        p.next = p.next.next
        return pre_head.next


class SolutionC:
    """
    使用双指针，第一个指针在n+1个位置开始，第二个指针在头开始，同时移动，最后第一个指针到底NULL，此时第二个指针所在位置则是被删除
    结点的前驱点
    时间复杂度：O(n)
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # n有效检验
        if n <= 0:
            return head
        pre_head = ListNode(-1)
        pre_head.next = head
        first = second = pre_head
        m = n + 1
        # 第一个指针先走n+1
        while m > 0:
            first = first.next
            m -= 1
            if first is None and m > 0:
                # n太大了
                return head
        # 第一个指针肯定先走完
        while first:
            first = first.next
            second = second.next
        # 此时第二指针为删除点的前驱点
        second.next = second.next.next
        return pre_head.next


if __name__ == '__main__':
    sol = SolutionC()
    args_list = [(1, ), (1, ), (2, ), (2, )]
    algorithm_func_multi_exec(linked_examples, sol.removeNthFromEnd, args_list)
