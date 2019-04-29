from typing import *


class Solution:
    """
    假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
    注意：
    你可以假设胃口值为正。
    一个小朋友最多只能拥有一块饼干。
    示例 1:
    输入: [1,2,3], [1,1]
    输出: 1
    解释:
    你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
    虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
    所以你应该输出1。
    示例 2:
    输入: [1,2], [1,2,3]
    输出: 2
    解释:
    你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
    你拥有的饼干数量和尺寸都足以让所有孩子满足。
    所以你应该输出2.
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        pass


def find_content_children(g: List[int], s: List[int]) -> int:
    """
    :param g: 胃口
    :param s: 饼干大小
    :return:
    >>> find_content_children([1,2,3], [1,1])
    1
    >>> find_content_children([1,2], [1,2,3])
    2
    >>> find_content_children([1,2,3], [3])
    1
    >>> find_content_children([10, 9, 8, 7], [5, 6, 7, 8])
    2
    """
    g.sort()
    s.sort()
    index_g: int = 0
    index_s: int = 0
    children_content: int = 0
    while index_g < len(g) and index_s < len(s):
        if g[index_g] <= s[index_s]:
            children_content += 1
            index_g += 1
        index_s += 1
    return children_content


def find_content_children_with_share(g: List[int], s: List[int]) -> int:
    """
    :param g: 胃口
    :param s: 饼干大小
    :return:
    >>> find_content_children_with_share([1,2,3], [1,1])
    1
    >>> find_content_children_with_share([1,2], [1,2,3])
    2
    >>> find_content_children_with_share([1,2,3], [3])
    2
    """
    g.sort()
    s.sort()
    index_g: int = 0
    index_s: int = 0
    children_content: int = 0
    while index_g < len(g) and index_s < len(s):
        if g[index_g] == s[index_s]:
            children_content += 1
            index_g += 1
            index_s += 1
        elif g[index_g] > s[index_s]:
            g[index_g] = g[index_g] - s[index_s]
            index_s += 1
        else:
            children_content += 1
            s[index_s] = s[index_s] - g[index_g]
            index_g += 1
    return children_content


if __name__ == '__main__':
    import doctest

    doctest.testmod()
