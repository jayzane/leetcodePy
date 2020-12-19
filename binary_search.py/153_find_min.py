from typing import *


class Solution:
    """
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    请找出其中最小的元素。
    你可以假设数组中不存在重复元素。
    示例 1:
    输入: [3,4,5,1,2]
    输出: 1
    示例 2:
    输入: [4,5,6,7,0,1,2]
    输出: 0
    """

    def findMin(self, nums: List[int]) -> int:
        pass


def find_min(nums: List[int]) -> int:
    """
    旋转后，最小数字以右的位置都应该比左边的小，同时最左边最小的是首位，所以只需要判断mid是否小于第一个数字
    :param nums:
    :return:
    >>> find_min([3,4,5,1,2])
    1
    >>> find_min([2, 1])
    1
    >>> find_min([1])
    1
    >>> find_min([1,2,3,4,5])
    1
    >>> find_min([])
    Traceback (most recent call last):
    ...
    Exception: nums is empty!
    """
    if not nums:
        raise Exception('nums is empty!')
    if nums[0] < nums[-1]:
        return nums[0]
    if len(nums) == 1:
        return nums[0]
    first: int = nums[0]
    left: int = 1
    right: int = len(nums) - 1
    while left <= right:
        mid: int = (left + right) // 2
        if nums[mid] > first:
            left = mid + 1
        else:
            right = mid - 1
    return nums[left]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
