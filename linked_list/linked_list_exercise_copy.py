"""
单链表反转
链表中环的检测
两个有序的链表合并
删除链表倒数第 n 个结点
求链表的中间结点
2020-12-13:
"""

from linked_list import Node


def reverse_linked_list(node):
    prev = None
    while node:
        prev, node.next, node = node, prev, node.next
    return prev


def has_cycle(node):
    if not node or not node.next:
        return False
    low = node
    fast = node.next
    while fast and fast.next:
        if low is fast:
            return True
        low = low.next
        fast = fast.next.next
    return False


def merge_two_sorted_list(node1, node2):
    new_h = h = Node(0)
    while node1 and node2:
        if node1.val < node2.val:
            add_n = node1
            node1 = node1.next
        else:
            add_n = node2
            node2 = node2.next
        h.next = add_n
        h = h.next
    if node1:
        h.next = node1
    if node2:
        h.next = node2
    return new_h.next


def remove_nth_node_from_end(node, n):
    if n <= 0 and not node:
        return node
    new_h = node
    node = dummy_head = Node(0)
    dummy_head.next = new_h
    count = -1
    help_dict = {}
    while node:
        count += 1
        help_dict[count] = node
        node = node.next
    if count >= n:
        pre_cnt = count - n
        help_dict[pre_cnt].next = help_dict[pre_cnt].next.next
    return dummy_head.next


def get_middle_of_linked_list(node):
    if not node and not node.next:
        return node
    slow = fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == '__main__':
    nums_reverse = [4, 3, 7, 9]
    answer_nums = [9, 7, 3, 4]
    h_reverse = Node.init_list(nums_reverse)
    sol_reverse = reverse_linked_list(h_reverse)
    answer_reverse = Node.init_list(answer_nums)
    assert Node.compare(sol_reverse, answer_reverse) is True, 'Func reverse_linked_list failed'
    print('Func reverse_linked_list success')

    nums_cycle = [4, 3, 7, 9]
    answer = True
    h_cycle = Node.init_list(nums_cycle)
    h_cycle.next.next.next = h_cycle.next.next
    sol_cycle = has_cycle(h_cycle)
    assert sol_cycle is answer, 'has_cycle failed'
    print('Func has_cycle success')

    nums1_sorted = [1, 5, 7, 9]
    nums2_sorted = [2, 4, 8, 11]
    h1_sorted = Node.init_list(nums1_sorted)
    h2_sorted = Node.init_list(nums2_sorted)
    sol_sorted = merge_two_sorted_list(h1_sorted, h2_sorted)
    answer_nums = sorted(nums1_sorted + nums2_sorted)
    answer_sorted = Node.init_list(answer_nums)
    assert Node.compare(sol_sorted, answer_sorted), 'Func merge_two_sorted_list failed'
    print('Func merge_two_sorted_list success')

    nums_remove = [1, 6, 3, 8, 9]
    answer_nums = [1, 3, 8, 9]
    h_remove = Node.init_list(nums_remove)
    sol_remove = remove_nth_node_from_end(h_remove, 4)
    answer_remove = Node.init_list(answer_nums)
    assert Node.compare(sol_remove, answer_remove), 'Func remove_nth_node_from_end failed'
    print('Func remove_nth_node_from_end success')

    nums_middle = [1, 6, 3, 8, 9]
    answer = 3
    h_middle = Node.init_list(nums_middle)
    sol_middle = get_middle_of_linked_list(h_middle)
    assert sol_middle.val == answer, 'Func get_middle_of_linked_list failed'
    print('Func get_middle_of_linked_list success')
