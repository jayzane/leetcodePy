from typing import *


class Solution:
    """
    给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。
    示例 1:
    输入: [1,1,2,3,3,4,4,8,8]
    输出: 2
    示例 2:
    输入: [3,3,7,7,10,11,11]
    输出: 10
    注意: 您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。
    """

    def singleNonDuplicate(self, nums: List[int]) -> int:
        pass


def single_non_duplicate_back(nums: List[int]) -> int:
    """
    :param nums:
    :return:
    >>> single_non_duplicate_back([1,1,2,3,3,4,4,8,8])
    2
    >>> single_non_duplicate_back([3,3,7,7,10,11,11])
    10
    >>> single_non_duplicate_back([1,1,2])
    2
    """
    if not nums:
        return 0
    len_n: int = len(nums)
    left: int = 0
    right: int = len_n - 1
    while left <= right:
        mid: int = (left + right) // 2
        is_odd: bool = mid % 2 != 0
        if nums[mid] != nums[mid - 1]:
            if mid == len_n - 1 or nums[mid] != nums[mid + 1]:
                return nums[mid]
        elif nums[mid] != nums[mid + 1]:
            if mid == 0 or nums[mid] != nums[mid - 1]:
                return nums[mid]
        if left < len_n - 1 and nums[mid] == nums[mid + 1]:
            if not is_odd:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if not is_odd:
                right = mid - 1
            else:
                left = mid + 1
    return 0


def single_non_duplicate(nums: List[int]) -> int:
    """
    设目标位置为i，i肯定为偶数，中间数为m并且m为偶数，
    如果m<index，肯定有nums[m] == nums[m+1]
    如果m>=index，肯定有nums[m] != nums[m+1]
    为保证m+1去得到，所以最左索引得小于最右索引
    结束循环时，最左索引可能等于最右索引，也可能比最右大1，两种情况都可以直接取最左索引
    :param nums:
    :return:
    >>> single_non_duplicate([1,1,2,3,3,4,4,8,8])
    2
    >>> single_non_duplicate([3,3,7,7,10,11,11])
    10
    >>> single_non_duplicate([1,1,2])
    2
    """
    if not nums:
        return 0
    len_n: int = len(nums)
    left: int = 0
    right: int = len_n - 1
    while left < right:
        mid: int = (left + right) // 2
        if mid % 2 == 1:
            mid -= 1  # 保证是偶数
        if nums[mid] == nums[mid + 1]:
            left = mid + 2
        else:
            right = mid
    return nums[left]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
