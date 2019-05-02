from typing import *


class Solution:
    """
    给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
    你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
    字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
    示例 1:
    s = "abc", t = "ahbgdc"
    返回 true.
    示例 2:
    s = "axc", t = "ahbgdc"
    返回 false.
    后续挑战 :
    如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        pass


def is_subsequence(s: str, t: str) -> bool:
    """
    :param s:
    :param t:
    :return:
    >>> is_subsequence('abc', 'adbgc')
    True
    >>> is_subsequence('abc', 'adgc')
    False
    >>> is_subsequence('leeeeetcode', 'lyyyyyyyeeeeyyyyyyyyyetcoyyyyyyyyyde')
    True
    >>> is_subsequence('axc', 'ahbgdc')
    False
    >>> is_subsequence('acb', 'ahbgdc')
    False
    """
    last: int = 0
    for s1 in s:
        last = t.find(s1, last) + 1
        if last == 0:  # not found
            return False
    return True


if __name__ == '__main__':
    import doctest

    doctest.testmod()