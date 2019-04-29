from typing import *
import collections


class Solution:
    """
    给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
    此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
    注意:
    不能使用代码库中的排序函数来解决这道题。
    示例:
    输入: [2,0,2,1,1,0]
    输出: [0,0,1,1,2,2]
    进阶：
    一个直观的解决方案是使用计数排序的两趟扫描算法。
    首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
    你能想出一个仅使用常数空间的一趟扫描算法吗？
    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass


def sort_colors_back(nums: List[int]) -> None:
    """
    :param nums:
    :return:
    >>> ns = [2,0,2,1,1,0]
    >>> sort_colors_back(ns)
    >>> ns
    [0, 0, 1, 1, 2, 2]
    """
    hash_map: dict = collections.defaultdict(int)
    for n in nums:
        hash_map[n] += 1
    index: int = 0
    for i in range(3):
        for j in range(hash_map[i]):
            nums[index] = i
            index += 1


def sort_colors(nums: List[int]) -> None:
    """
    :param nums:
    :return:
    >>> ns = [2,0,2,1,1,0]
    >>> sort_colors(ns)
    >>> ns
    [0, 0, 1, 1, 2, 2]
    """
    index1: int = 0  # 指向已排序0的下一个
    index2: int = 0  # 处理中的指针
    index3: int = len(nums) - 1  # 指向已经排序2的上一个
    while index2 <= index3:
        # 如果为0就和前面换，换过来的肯定不是2，因为前面如果有2，则肯定已经被换到后面了
        # 所以换过来的不是1就是0，如果是1，index1和index2移动
        # 但是如果是0的话，代表目前为止还没有1出现，index1和index2移动
        if nums[index2] == 0:
            nums[index2], nums[index1] = nums[index1], nums[index2]
            index1 += 1
            index2 += 1
        elif nums[index2] == 2:
            nums[index2], nums[index3] = nums[index3], nums[index2]
            index3 -= 1
        else:
            index2 += 1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
