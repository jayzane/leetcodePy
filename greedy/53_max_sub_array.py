from typing import *


class Solution:
    """
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    示例:
    输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
    进阶:
    如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
    """

    def maxSubArray(self, nums: List[int]) -> int:
        pass


def max_sub_array_back(nums: List[int]) -> int:
    """
    :param nums:
    :return:
    >>> max_sub_array_back([-2,1,-3,4,-1,2,1,-5,4])
    6
    >>> max_sub_array_back([-2,1])
    1
    """
    if not nums:
        return 0
    pre_sum: int = nums[0]
    max_sum = nums[0]
    for i in range(1, len(nums)):
        if pre_sum > 0:
            pre_sum += nums[i]
        else:
            pre_sum = nums[i]
        max_sum = max(max_sum, pre_sum)
    return max_sum


def max_sub_array(nums: List[int]) -> int:
    """
    :param nums:
    :return:
    >>> max_sub_array([-2,1,-3,4,-1,2,1,-5,4])
    6
    >>> max_sub_array([-2,1])
    1
    """
    for i in range(1, len(nums)):
        nums[i] = nums[i] + max(nums[i - 1], 0)
    return max(nums)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
