from typing import *


class Solution:
    """
    假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
    给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。
    示例 1:
    输入: flowerbed = [1,0,0,0,1], n = 1
    输出: True
    示例 2:
    输入: flowerbed = [1,0,0,0,1], n = 2
    输出: False
    注意:
    数组内已种好的花不会违反种植规则。
    输入的数组长度范围为 [1, 20000]。
    n 是非负整数，且不会超过输入数组的大小。
    """

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pass


def can_place_flowers_back(flowerbed: List[int], n: int) -> bool:
    """
    :param flowerbed:
    :param n:
    :return:
    >>> can_place_flowers_back([1,0,0,0,1], 1)
    True
    >>> can_place_flowers_back([1,0,0,0,1], 2)
    False
    >>> can_place_flowers_back([0,0,1,0,0], 2)
    True
    >>> can_place_flowers_back([1,0,0,0,0,0,1], 2)
    True
    >>> can_place_flowers_back([0], 1)
    True
    """
    if not flowerbed or n <= 0 or n > len(flowerbed):
        return False
    place_cnt: int = 0
    len_f: int = len(flowerbed)
    for i in range(len_f):
        left_blank: bool = False
        right_blank: bool = False
        if i == 0:
            if flowerbed[0] == 0:
                left_blank = True
            if len_f > 1 and flowerbed[i + 1] == 0:
                right_blank = True
            elif len_f == 1:
                right_blank = True
        elif i == len_f - 1:
            if flowerbed[len_f - 1] == 0:
                right_blank = True
            if len_f > 1 and flowerbed[i - 1] == 0:
                left_blank = True
        else:
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                left_blank = right_blank = True
        if left_blank and right_blank:
            flowerbed[i] = 1
            place_cnt += 1
    return place_cnt >= n


def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    """
    :param flowerbed:
    :param n:
    :return:
    >>> can_place_flowers([1,0,0,0,1], 1)
    True
    >>> can_place_flowers([1,0,0,0,1], 2)
    False
    >>> can_place_flowers([0,0,1,0,0], 2)
    True
    >>> can_place_flowers([1,0,0,0,0,0,1], 2)
    True
    >>> can_place_flowers([0], 1)
    True
    """
    if not flowerbed or n <= 0 or n > len(flowerbed):
        return False
    place_cnt: int = 0
    i: int = 1
    flowerbed.insert(0, 0)  # 在左边建立虚拟空地
    flowerbed.append(0)  # 在右边建立虚拟空地
    len_f: int = len(flowerbed)
    while i < len_f - 1:
        if not flowerbed[i] and not flowerbed[i - 1] and not flowerbed[i + 1]:
            # flowerbed[i] = 1
            place_cnt += 1
            i += 1  # skip to next
        i += 1
    return place_cnt >= n


if __name__ == '__main__':
    import doctest

    doctest.testmod()
