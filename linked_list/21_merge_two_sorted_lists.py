"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
from common.init_data import init_list_node, print_list_node


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """使用双指针，l1和l2没被污染
    时间复杂度：O(n+m)
    空间复杂度：O(n+m)
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        p1, p2 = l1, l2
        head = h = None
        while p1 and p2:
            if p1.val < p2.val:
                val = p1.val
                p1 = p1.next
            else:
                val = p2.val
                p2 = p2.next
            if h is None:
                h = ListNode(val)
                head = h
            else:
                h.next = ListNode(val)
                h = h.next
            # 下面两个循环，不算嵌套循环，因为在大循环里只会执行一次
            if p1 is None:
                while p2:
                    h.next = ListNode(p2.val)
                    h = h.next
                    p2 = p2.next
            if p2 is None:
                while p1:
                    h.next = ListNode(p1.val)
                    h = h.next
                    p1 = p1.next
        return head


class SolutionA:
    """递归处理，l1和l2变量被污染了
    if l1[0] < l2[0]: l1[0] + merge(l1[1:], l2)
    else: l2[0] + merge(l1, l2[1:])
    时间复杂度：O(n+m)
    空间复杂度：O(n+m)
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if l1.val < l2.val:
            # self.mergeTwoLists(l1.next, l2) 假设已经合并好了
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class SolutionB:
    """对Solution优化，加一个哨兵结点；结束循环条件：其中一个链表迭代完成
    l1, l2被污染
    时间复杂度：O(n)
    空间复杂度: O(1)
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_head = ListNode(-1)  # 哨兵用处在于不用判断l1[0]和l2[0]谁大谁小
        prev = pre_head
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                prev = l1
                l1 = l1.next
            else:
                prev.next = l2
                prev = l2
                l2 = l2.next
        if l1 is None:
            # 因为是有序的，剩下的l2肯定都比l1大，将剩下的l2接到prev后面
            prev.next = l2
        else:
            prev.next = l1
        return pre_head.next


if __name__ == '__main__':
    sol = SolutionB()
    l1 = init_list_node([1, 2, 4])
    l2 = init_list_node([1, 3, 4])
    ret = sol.mergeTwoLists(l1, l2)
    print_list_node(ret)
