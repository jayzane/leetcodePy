"""
some random init data to test
"""
import random
from typing import *

MAX_NUM = 99999999


def random_nums(length: int = 100, sorted_flag: int = 0,
                has_negative: bool = False, has_dup: bool = False,
                max_num: int = 0) -> List[int]:
    """
     Get init nums in list
    :param length:
    :param sorted_flag: 0 is not sorted, -1 is reverse sorted, 1 is sorted
    :param has_negative:
    :param has_dup:
    :param max_num:
    :return:
    """
    max_num = MAX_NUM if max_num == 0 else max_num
    start = -max_num if has_negative else 0
    result = []
    for _ in range(length):
        rand_int = random.randrange(start, max_num)
        while not has_dup and rand_int in result:
            rand_int = random.randrange(start, max_num)
        result.append(rand_int)
    if sorted_flag > 0:
        result.sort()
    elif sorted_flag < 0:
        result.sort(reverse=True)
    return result


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def init_tree(data_list: List[Union[int, str, None]], index) -> Optional[TreeNode]:
    """
    data_list首位为根节点(树)，奇数位为左节点(树), 奇数位为右节点(树)
    :param data_list:
    :param index:
    :return:
    """
    len_data: int = len(data_list)
    if len_data == 0 or index >= len_data:
        return
    if data_list[index] is None:
        return
    root: TreeNode = TreeNode(data_list[index])
    root.left = init_tree(data_list, index * 2 + 1)
    root.right = init_tree(data_list, index * 2 + 2)
    return root


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def init_list_node(data_list: List):
    """
    初始化单向链表
    """
    if not data_list:
        return
    head = ListNode(data_list[0])
    p = head
    for data in data_list[1:]:
        p.next = ListNode(data)
        p = p.next
    return head


def print_list_node(head: ListNode):
    p = head
    l = []
    while p:
        l.append(str(p.val))
        p = p.next
    s = '->'.join(l)
    print(s or None)


def init_list_examples() -> List:
    """产生链表常见的四种例子：空、1个结点、2个结点、大于2个结点"""
    examples = []
    l1 = init_list_node([])
    l2 = init_list_node([1])
    l3 = init_list_node([1, 2])
    l4 = init_list_node([1, 2, 3, 4, 5])
    examples.append(l1)
    examples.append(l2)
    examples.append(l3)
    examples.append(l4)
    return examples


linked_examples = init_list_examples()


def algorithm_func_exec(list_heads: List, func, args=()):
    """
    遍历list_heads并执行func(list_head)，然后输出打印
    """
    for list_head in list_heads:
        if args:
            head = func(list_head, args)
        else:
            head = func(list_head)
        print_list_node(list_head)
        print('>' * 5)
        print_list_node(head)


def algorithm_func_multi_exec(list_heads: List, func, args_list=()):
    """
    遍历list_heads并执行func(list_head)，然后输出打印
    """
    for i, list_head in enumerate(list_heads):
        print_list_node(list_head)
        if args_list:
            head = func(list_head, *args_list[i])
        else:
            head = func(list_head)
        print('>' * 5)
        print_list_node(head)
        print('-' * 20)


if __name__ == '__main__':
    # print(random_nums(10, max_num=100))
    root1 = init_tree([1, 2, 3, 4, None, 8], 0)
    print(root1.val)
