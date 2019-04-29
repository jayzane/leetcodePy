from typing import *


class Solution:
    """
    定一个只包含小写字母的有序数组letters 和一个目标字母 target，寻找有序数组里面比目标字母大的最小字母。
    数组里字母的顺序是循环的。举个例子，如果目标字母target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。
    示例:
    输入:
    letters = ["c", "f", "j"]
    target = "a"
    输出: "c"
    输入:
    letters = ["c", "f", "j"]
    target = "c"
    输出: "f"
    输入:
    letters = ["c", "f", "j"]
    target = "d"
    输出: "f"
    输入:
    letters = ["c", "f", "j"]
    target = "g"
    输出: "j"
    输入:
    letters = ["c", "f", "j"]
    target = "j"
    输出: "c"
    输入:
    letters = ["c", "f", "j"]
    target = "k"
    输出: "c"
    注:
    letters长度范围在[2, 10000]区间内。
    letters 仅由小写字母组成，最少包含两个不同的字母。
    目标字母target 是一个小写字母。
    """

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        pass


def next_greatest_letter(letters: List[str], target: str) -> str:
    """
    :param letters:
    :param target:
    :return:
    >>> next_greatest_letter(['c', 'c'], 'c')
    'c'
    >>> next_greatest_letter(['d'], 'c')
    'd'
    >>> next_greatest_letter(['c', 'f', 'j'], 'd')
    'f'
    >>> next_greatest_letter([], 'd')
    ''
    >>> next_greatest_letter(['c', 'f', 'j'], 'k')
    'c'
    >>> next_greatest_letter(['c', 'f', 'j'], 'a')
    'c'
    >>> next_greatest_letter(['c', 'f', 'j'], 'z')
    'c'
    """
    if not letters:
        return ''
    # elif target < letters[0] or target >= letters[-1]:
    #     return letters[0]
    left: int = 0
    len_letters: int = len(letters)
    right: int = len_letters - 1
    while left <= right:
        mid: int = (left + right) // 2
        if letters[mid] > target:
            while mid > left and letters[mid - 1] == letters[mid]:
                mid -= 1
            right = mid - 1
        else:
            while mid < right and letters[mid + 1] == letters[mid]:
                mid += 1
            if mid < right and letters[mid] == target:
                return letters[mid + 1]
            left = mid + 1
    return letters[left] if left < len_letters else letters[0]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
