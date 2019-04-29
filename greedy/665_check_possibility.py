from typing import *


class Solution:
    """
    给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
    我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。
    示例 1:
    输入: [4,2,3]
    输出: True
    解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
    示例 2:
    输入: [4,2,1]
    输出: False
    解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
    说明:  n 的范围为 [1, 10,000]。
    """

    def checkPossibility(self, nums: List[int]) -> bool:
        pass


def check_possibility(nums: List[int]) -> bool:
    """
    :param nums:
    :return:
    >>> check_possibility([3, 4, 2, 3])
    False
    >>> check_possibility([4, 2, 3])
    True
    >>> check_possibility([4, 3, 2])
    False
    >>> check_possibility([2])
    True
    >>> check_possibility([2, 3, 4, 7, 9, 10, 5, 12, 15])
    True
    """
    if not nums:
        return False
    decr_cnt: int = 0  # 逆序计数
    for index in range(1, len(nums)):
        if nums[index] >= nums[index - 1]:
            continue
        decr_cnt += 1
        if decr_cnt > 1:
            return False
        if index > 1 and nums[index] < nums[index - 2]:  # [4, 5, 3]
            nums[index] = nums[index - 1]
        else:  # [2, 5, 3]
            nums[index - 1] = nums[index]
    return True


if __name__ == '__main__':
    import doctest

    doctest.testmod()
