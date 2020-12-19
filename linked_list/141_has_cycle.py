"""
给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        low_i = head
        fast_i = head.next
        while fast_i and fast_i.next:
            if low_i is fast_i:
                return True
            low_i = low_i.next
            fast_i = fast_i.next.next
        return False


if __name__ == '__main__':
    sol = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    h = n1
    h.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    print(sol.hasCycle(h))
