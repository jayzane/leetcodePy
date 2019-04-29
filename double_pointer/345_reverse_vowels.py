from typing import *


class Solution:
    """
    编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
    示例 1:
    输入: "hello"
    输出: "holle"
    示例 2:
    输入: "leetcode"
    输出: "leotcede"
    说明:
    元音字母不包含字母"y"。
    """

    def reverseVowels(self, s: str) -> str:
        pass


def reverse_vowels_back(s: str) -> str:
    if not s:
        return ''
    length: int = len(s)
    if length < 2:
        return s
    index1: int = 0
    index2: int = length - 1
    s_list: List[str] = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    while index1 < index2:
        while s_list[index1] not in vowels and index1 < index2:
            index1 += 1
        while s_list[index2] not in vowels and index1 < index2:
            index2 -= 1
        if index1 < index2:
            tmp: str = s_list[index1]
            s_list[index1] = s_list[index2]
            s_list[index2] = tmp
        index1 += 1
        index2 -= 1
    return ''.join(s_list)


def reverse_vowels_back_two(s: str) -> str:
    if not s:
        return ''
    length: int = len(s)
    index1: int = 0
    index2: int = length - 1
    s_list: List[str] = list(s)
    vowels: str = 'aeiouAEIOU'
    while index1 < index2:
        while s_list[index1] not in vowels and index1 < index2:
            index1 += 1
        while s_list[index2] not in vowels and index1 < index2:
            index2 -= 1
        if index1 < index2:
            tmp: str = s_list[index1]
            s_list[index1] = s_list[index2]
            s_list[index2] = tmp
        index1 += 1
        index2 -= 1
    return ''.join(s_list)


def reverse_vowels(s: str) -> str:
    """
    Firstly get vowels index, then change each other in the symmetry.
    :param s:
    :return:
    """
    if not s:
        return ''
    vowels: str = 'aeiouAEIOU'
    s_list: List[str] = list(s)
    vowel_index: List[int] = [i for i in range(len(s_list)) if s_list[i] in vowels]
    len_vowel_index: int = len(vowel_index)
    mid: int = len_vowel_index // 2  # even and odd are the same
    for i in range(mid):
        s_list[vowel_index[i]], s_list[vowel_index[-i - 1]] = s_list[vowel_index[-i - 1]], s_list[vowel_index[i]]
    return ''.join(s_list)


if __name__ == '__main__':
    print(reverse_vowels('hello'))
    print(reverse_vowels('xaj'))
    print(reverse_vowels('leetcode'))
    print(reverse_vowels('hEllo'))
    print(reverse_vowels('eeeeeeeeeeeeeeeeeeeeeeeee'))
    print(reverse_vowels(''))
    print(reverse_vowels(None))
    print(reverse_vowels('a'))
