from typing import *


class Solution:
    """
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



    示例:

    输入："23"
    输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    说明:
    尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
    """

    def letter_combinations(self, digits: str) -> List[str]:
        pass


def letter_combinations(digits: str) -> List[str]:
    """
    :param digits:
    :return:
    >>> letter_combinations('23')
    ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    """

    digit_map: Dict[str, str] = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    if not digits:
        return []
    elif len(digits) == 1:
        return list(digit_map[digits])
    first: str = digits[0]
    others: str = digits[1:]
    res: List[str] = []
    for i in digit_map[first]:
        for j in letter_combinations(others):
            res.append(i + j)
    return res


if __name__ == '__main__':
    import doctest

    doctest.testmod()
