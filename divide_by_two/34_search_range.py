from typing import *


class Solution:
    """
    给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
    你的算法时间复杂度必须是 O(log n) 级别。
    如果数组中不存在目标值，返回 [-1, -1]。
    示例 1:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: [3,4]
    示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: [-1,-1]
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pass


def search_range_back(nums: List[int], target: int) -> List[int]:
    """
    :param nums:
    :param target:
    :return:
    >>> search_range_back([5,7,7,8,8,10], 8)
    [3, 4]
    >>> search_range_back([5,7,7,8,8,10], 6)
    [-1, -1]
    >>> search_range_back([5,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,10], 8)
    [24, 25]
    """
    if not nums:
        return [-1, -1]
    left: int = 0
    len_nums: int = len(nums)
    right: int = len_nums - 1
    while left <= right:
        mid: int = (left + right) // 2
        if nums[mid] > target:
            while mid > left and nums[mid - 1] == nums[mid]:
                mid -= 1
            right = mid - 1
        elif nums[mid] < target:
            while mid < right and nums[mid + 1] == nums[mid]:
                mid += 1
            left = mid + 1
        else:
            mid_left: int = mid
            while mid_left > left:
                if nums[mid_left - 1] == nums[mid_left]:
                    mid_left -= 1
                else:
                    break
            mid_right: int = mid
            while mid_right < right:
                if nums[mid_right + 1] == nums[mid_right]:
                    mid_right += 1
                else:
                    break
            return [mid_left, mid_right]
    return [-1, -1]


def search_range(nums: List[int], target: int) -> List[int]:
    """
    :param nums:
    :param target:
    :return:
    >>> search_range([2, 2], 2)
    [0, 1]
    >>> search_range([], 8)
    [-1, -1]
    >>> search_range([1], 1)
    [0, 0]
    >>> search_range([5,7,7,8,8,10], 8)
    [3, 4]
    >>> search_range([5,7,7,8,8,10], 6)
    [-1, -1]
    >>> search_range([5,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,10], 8)
    [24, 25]
    """
    len_n: int = len(nums)
    left_i: int = bi_search(nums, 0, len_n - 1, target)
    right_i: int = bi_search(nums, 0, len_n - 1, target + 1)
    if len_n < 1 or nums[left_i] != target:
        return [-1, -1]
    if right_i > 0 and nums[right_i] != target:
        right_i -= 1
    return [left_i, right_i]


def bi_search(nums: List[int], left: int, right: int, target: int) -> int:
    """
    找到目标数的最左位置，如果在nums中不存在目标数，输出的是比其大的第一个位置
    :param nums:
    :param left:
    :param right:
    :param target:
    :return:
    """
    while left < right:
        mid: int = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    import doctest

    doctest.testmod()
