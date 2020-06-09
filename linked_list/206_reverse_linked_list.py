"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """遍历旧的链表，依次插入一个新链表的头部
    """

    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        # 时间复杂度O(n^2)
        # 空间复杂度O(1)
        while head:
            node = ListNode(head.val)
            new_head = self.insert(new_head, node)
            head = head.next
        return new_head

    def insert(self, head: ListNode, node: ListNode) -> ListNode:
        if head is None:
            head = node
        else:
            node.next = head
            head = node
        return head


class SolutionA:
    """将链条指向反过来
    1. 记录p.next
    2. p.next指向prev
    3. prev = p
    4. p = 记录的p.next
    """

    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        # 时间复杂度：O(n)
        while head:
            next_tmp = head.next
            head.next = pre
            pre = head
            head = next_tmp
        return pre


class SolutionB:
    """简化版SolutionA"""

    def reverseList(self, head: ListNode) -> ListNode:
        # 时间复杂度：O(n)
        p, prev = head, None
        while p:
            p.next, prev, p = prev, p, p.next
        return prev


class SolutionC:
    """使用递归，假设现在正处于第k个位置，后面k+1到n已经反转好了，则有k.next.next=k，再断掉k.next"""

    def reverseList(self, head: ListNode) -> ListNode:
        # 时间复杂度：O(n)
        # 空间复杂度: O(n)
        # 递归总有一个结束条件
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    h1 = n1
    sol = SolutionC()
    nh1 = sol.reverseList(h1)
    while nh1:
        print('node: %s' % nh1.val)
        nh1 = nh1.next
