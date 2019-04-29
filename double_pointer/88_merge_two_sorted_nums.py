from typing import *


class Solution:
    """
    给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
    说明:
    初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
    示例:
    输入:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3
    输出: [1,2,2,3,5,6]
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pass


def merge_two_sorted_nums(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    if nums1 is None or nums2 is None or m < 0 or n < 0:
        return
    index1: int = m - 1
    index2: int = n - 1
    index3: int = len(nums1) - 1
    if m == 0:
        nums1[:] = nums2[:]
    while index1 >= 0 and index2 >= 0:
        if nums1[index1] >= nums2[index2]:
            nums1[index3] = nums1[index1]
            index1 -= 1
        else:
            nums1[index3] = nums2[index2]
            index2 -= 1
        index3 -= 1
    for i in range(index2, -1, -1):
        nums1[index3] = nums2[i]
        index3 -= 1


if __name__ == '__main__':
    num1: List[int] = [1, 2, 3, 0, 0, 0]
    m: int = 3
    num2: List[int] = [2, 5, 6]
    n: int = 3
    merge_two_sorted_nums(num1, m, num2, n)
    print(num1)

    num1: List[int] = [0, 0, 0]
    m: int = 0
    num2: List[int] = [2, 5, 6]
    n: int = 3
    merge_two_sorted_nums(num1, m, num2, n)
    print(num1)

    num1: List[int] = [2, 0]
    m: int = 1
    num2: List[int] = [1]
    n: int = 1
    merge_two_sorted_nums(num1, m, num2, n)
    print(num1)

    num1: List[int] = [-11, -10, -9, 0, 0, 0]
    m: int = 3
    num2: List[int] = [2, 5, 6]
    n: int = 3
    merge_two_sorted_nums(num1, m, num2, n)
    print(num1)

    num1: List[int] = [1, 2, 3]
    m: int = 3
    num2: List[int] = []
    n: int = 0
    merge_two_sorted_nums(num1, m, num2, n)
    print(num1)

    num1: List[int] = [1, 2, 3, 0, 0, 0]
    m: int = 3
    num2 = None
    n: int = 0
    merge_two_sorted_nums(num1, m, num2, n)
    print(num1)

    num1: List[int] = [1, 2, 3, 0, 0, 0]
    m: int = 3
    num2: List[int] = [2, 5, 6]
    n: int = -3
    merge_two_sorted_nums(num1, m, num2, n)
    print(num1)
