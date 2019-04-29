from typing import *
import math
import operator
import collections


class Solution:
    """
    给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

    示例 1:

    输入: n = 12
    输出: 3
    解释: 12 = 4 + 4 + 4.
    示例 2:

    输入: n = 13
    输出: 2
    解释: 13 = 4 + 9.
    """

    def numSquares(self, n: int) -> int:
        pass


def num_squares(n: int) -> int:
    """
    error
    :param n:
    :return:
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    start: int = 1
    min_n: int = float('inf')
    n_sq: float = math.sqrt(n)
    while 0 < start <= n_sq:
        other: int = n - start
        if other < 0:
            break
        start_sq: float = math.sqrt(start)
        other_sq: float = math.sqrt(other)
        if int(start_sq) == start_sq:
            start_n = 1
        else:
            start_n: int = num_squares(start)

        if int(other_sq) == other_sq:
            other_n = 1
        else:
            other_n: int = num_squares(other)
        min_n = min(min_n, start_n + other_n)
        start += 1
    return 0 if min_n == float('inf') else min_n


def num_squares_dp(n: int) -> int:
    """
    到达n的前一点最少的次数+1，到达n的前一点是通过遍历生成的平方数得到
    :param n:
    :return:
    >>> num_squares_dp(12)
    3
    >>> num_squares_dp(13)
    2
    """
    squares_less_n: List[int] = generate_squares(n)
    record: Dict[int, int] = {0: 0}
    for i in range(1, n + 1):
        min_n: int = float('inf')
        for s in squares_less_n:
            if s > i:
                break
            min_n = min(min_n, record[i - s] + 1)
        record[i] = min_n
    return record[n]


# def num_squares_graph(n: int) -> int:
#     """
#     广度优先搜索
#     :param n:
#     :return:
#     >>> num_squares_graph(12)
#     3
#     >>> num_squares_graph(13)
#     2
#     >>> num_squares_graph(7618)
#     2
#     """
#     squares_less_n: List[int] = generate_squares(n)
#     level: int = 0  # 从n点开始数层数
#     queue = collections.deque([n])  # 这层的点有哪些
#     marked: List[int] = []  # 标记以及走过这一点了，避免重复计算后面又重新遇见的情况
#     while queue:
#         size: int = len(queue)
#         level += 1
#         while size > 0:
#             curr: int = queue.popleft()
#             for s in squares_less_n:
#                 next_node: int = curr - s
#                 if next_node < 0:
#                     break
#                 elif next_node == 0:
#                     return level
#                 if next_node in marked:
#                     continue
#                 marked.append(next_node)
#                 queue.append(next_node)
#             size -= 1
#     return n


def num_squares_graph_double(n: int) -> int:
    """
    广度优先搜索，双端优化
    :param n:
    :return:
    >>> num_squares_graph_double(12)
    3
    >>> num_squares_graph_double(13)
    2
    >>> num_squares_graph_double(7618)
    2
    """
    squares_less_n: List[int] = generate_squares(n)
    curr_set: Set[int] = {0}
    end_set: Set[int] = {n}
    level: int = 0
    marked: Set[int] = {0}  # 标记以及走过这一点了，避免重复计算后面又重新遇见的情况
    op_map: Dict = {
        'add': operator.add,
        'sub': operator.sub
    }
    op: str = 'add'
    while curr_set:
        level += 1
        tmp_set: Set(int) = set()
        for curr in curr_set:
            for s in squares_less_n:
                next_node: int = op_map[op](curr, s)
                if next_node < 0 or next_node > n:
                    break
                elif next_node in end_set:
                    return level
                if next_node in marked:
                    continue
                marked.add(next_node)
                tmp_set.add(next_node)
        if len(tmp_set) <= len(end_set):
            curr_set = tmp_set
        else:
            curr_set = end_set
            end_set = tmp_set
            op = {'add': 'sub', 'sub': 'add'}[op]
    return n


def generate_squares(n: int) -> List[int]:
    """
    n的平方比n-1的平方多2n-1，是由平方差公式得到
    2n-1的序列为1,3,5,7
    :param n:
    :return:
    >>> generate_squares(7)
    [1, 4]
    """
    square: int = 1
    diff: int = 3
    res: List[int] = []
    while square <= n:
        res.append(square)
        square += diff
        diff += 2
    return res


# 四平方和定理
# def numSquares(self, n: int) -> int:
#     while n % 4 == 0:
#         n /= 4
#     if n % 8 == 7:
#         return 4
#     a = 0
#     while a**2 <= n:
#         b = int((n - a**2)**0.5)
#         if a**2 + b**2 == n:
#             return (not not a) + (not not b)
#         a += 1
#     return 3

if __name__ == '__main__':
    import doctest

    doctest.testmod()
