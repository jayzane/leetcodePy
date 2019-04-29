"""
algorithm of comparing two str and reverse str
"""
from typing import *

MAX_STR_LEN = 50000


class Solution:
    """
    给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
    示例 1:
    输入: "aba"
    输出: True
    示例 2:
    输入: "abca"
    输出: True
    解释: 你可以删除c字符。
    注意:
    字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
    """

    def validPalindrome(self, s: str) -> bool:
        pass


def validate_palindrome_back(s: str) -> bool:
    """
    TODO: error answer
    :param s: limited length
    :return:
    """
    if not s or len(s) > MAX_STR_LEN:
        return False
    del_count: int = 1  # max deleted char
    index1: int = 0
    index2: int = len(s) - 1
    res: bool = True
    while index1 < index2:
        if s[index1] != s[index2]:
            valid_flag: int = is_valid_with_skip(s, index1, index2)
            if valid_flag != 0 and del_count < 1:
                return False
            elif valid_flag > 0:
                index1 += 1
                del_count -= 1
            elif valid_flag < 0:
                index2 -= 1
                del_count -= 1
            else:
                return False
        index1 += 1
        index2 -= 1

    return res


def is_valid_with_skip_back(text: str, index1: int, index2: int) -> int:
    """
    :param text:
    :param index1:
    :param index2:
    :return: 0 invalid, 1 valid with left index + 1, -1 valid with right index - 1
    """
    if index2 - index1 == 1:
        return 1
    elif text[index1 + 1] == text[index2]:
        return 1
    elif text[index1] == text[index2 - 1]:
        return -1
    else:
        return 0


def validate_palindrome_back_two(s: str) -> bool:
    """
    :param s: limited length
    :return:
    """
    if not s or len(s) > MAX_STR_LEN:
        return False
    index1: int = 0
    index2: int = len(s) - 1
    while index1 < index2:
        if s[index1] != s[index2]:
            return is_valid_with_skip(s, index1 + 1, index2) or is_valid_with_skip(s, index1, index2 - 1)
        index1 += 1
        index2 -= 1
    return True


def is_valid_with_skip_back_two(s: str, index1: int, index2: int) -> bool:
    """
    skip one to validate left text
    """
    while index1 < index2:
        if s[index1] != s[index2]:
            return False
        index1 += 1
        index2 -= 1
    return True


def validate_palindrome(s: str) -> bool:
    """
    :param s: limited length
    :return:
    """
    if not s or len(s) > MAX_STR_LEN:
        return False
    s_reverse: str = s[::-1]
    if s == s_reverse:
        return True
    for i in range(len(s)):
        if s[i] != s_reverse[i]:  # s[1] != s[9 - 1 - 1]
            s_slice_one: str = s[:i] + s[i + 1:]  # skip left char
            if s_slice_one == s_slice_one[::-1]:
                return True
            else:
                s_slice_two: str = s_reverse[:i] + s_reverse[i + 1:]  # skip right char
                return s_slice_two == s_slice_two[::-1]
    return True

slice
if __name__ == '__main__':
    print(validate_palindrome('abc'))
    print(validate_palindrome('aba'))
    print(validate_palindrome('abea'))
    print(validate_palindrome('abbea'))
    print(validate_palindrome(
        'aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga'))
    print(validate_palindrome(''))
    print(validate_palindrome(None))
    print(validate_palindrome('a' * (MAX_STR_LEN + 1)))
