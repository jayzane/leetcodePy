from typing import *


class Solution:
    """
    给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。
    如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。
    示例 1:
    输入:
    s = "abpcplea", d = ["ale","apple","monkey","plea"]
    输出:
    "apple"
    示例 2:
    输入:
    s = "abpcplea", d = ["a","b","c"]
    输出:
    "a"
    说明:
    所有输入的字符串只包含小写字母。
    字典的大小不会超过 1000。
    所有输入的字符串长度不会超过 1000。
    """

    def findLongestWord(self, s: str, d: List[str]) -> str:
        pass


def find_longest_word_back(s: str, d: List[str]) -> str:
    """
    :param s:
    :param d:
    :return:
    >>> find_longest_word_back('abpcplea', ['ale','apple','monkey','plea'])
    'apple'
    >>> find_longest_word_back('abpcplea', ['a', 'b', 'c'])
    'a'
    >>> find_longest_word_back('abc', ['education', 'b', 'c'])
    'b'
    >>> find_longest_word_back('bab', ['ba','ab','a','b'])
    'ab'
    >>> find_longest_word_back('', [''])
    ''
    >>> find_longest_word_back('', ['a', 'b', 'c'])
    ''
    >>> find_longest_word_back('apple', [''])
    ''
    """
    last_word_back: str = ''
    if not s:
        return ''
    for word in d:
        index_w: int = 0
        len_w: int = len(word)
        len_last: int = len(last_word_back)
        if not word or len_w > len(s):
            continue
        for i in s:
            if i == word[index_w]:
                if index_w == len_w - 1:
                    if len_w > len_last or (len_w == len_last and word < last_word_back):
                        last_word_back = word
                    break
                index_w += 1
    return last_word_back


def find_longest_word(s: str, d: List[str]) -> str:
    """
    :param s:
    :param d:
    :return:
    >>> find_longest_word('abpcplea', ['ale','apple','monkey','plea'])
    'apple'
    >>> find_longest_word('abpcplea', ['a', 'b', 'c'])
    'a'
    >>> find_longest_word('abc', ['education', 'b', 'c'])
    'b'
    >>> find_longest_word('bab', ['ba','ab','a','b'])
    'ab'
    >>> find_longest_word('', [''])
    ''
    >>> find_longest_word('', ['a', 'b', 'c'])
    ''
    >>> find_longest_word('apple', [''])
    ''
    """
    if not s:
        return ''
    d.sort(key=lambda x: (-len(x), x))
    for word in d:
        if not word:
            continue
        index_w: int = 0
        flag: bool = True
        for i in word:
            index_w = s.find(i, index_w) + 1
            if index_w == 0:
                flag = False
                break
        if flag:
            return word
    return ''


if __name__ == '__main__':
    import doctest

    doctest.testmod()
