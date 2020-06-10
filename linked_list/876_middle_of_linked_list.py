"""
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。
示例 1：
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：
输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
"""

from common.init_data import ListNode, algorithm_func_exec, linked_examples


class Solution:
    """
    两次遍历
    时间复杂度：O(n)
    """

    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        p = head
        while p:
            count += 1
            p = p.next
        # 由于存在两个中间结点时选择后一个，刚好奇数、偶数情况一致
        mid = count // 2 + 1
        p = head
        # 从mid数到1停止
        while mid > 1:
            p = p.next
            mid -= 1
        return p


class SolutionA:
    """
    快慢指针，快指针走两步，慢指针指示快指针走了多少次"两步"，这样就获取到了中间点
    时间复杂度: O(n)，其实走一半就停下来了
    """
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    sol = SolutionA()
    algorithm_func_exec(linked_examples, sol.middleNode)
