from typing import *


class Solution:
    """
    给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
    函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
    说明:
    返回的下标值（index1 和 index2）不是从零开始的。
    你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
    示例:
    输入: numbers = [2, 7, 11, 15], target = 9
    输出: [1,2]
    解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pass


def two_sum_in_sorted_nums_back(numbers: List[int], target: int) -> List[int]:
    if not numbers or (numbers and len(numbers) < 2):
        raise Exception('numbers is None or less than 2')
    index1 = 0
    index2 = len(numbers) - 1
    while index1 < index2 and (numbers[index1] + numbers[index2] != target):
        if numbers[index1] + numbers[index2] > target:
            index2 -= 1
        else:
            index1 += 1
    result: List[int] = []
    if index1 != index2:
        result = [index1 + 1, index2 + 1]
    return result


def two_sum_in_sorted_nums(numbers: List[int], target: int) -> List[int]:
    if not numbers or (numbers and len(numbers) < 2):
        raise Exception('numbers is None or less than 2')
    index1: int = 0  # to annotate params
    index2: int = len(numbers) - 1  # to annotate params
    while index1 < index2:
        tmp_sum: int = numbers[index1] + numbers[index2]  # saving tmp sum
        if tmp_sum > target:
            index2 -= 1
        elif tmp_sum < target:
            index1 += 1
        else:
            break
    return [index1 + 1, index2 + 1] if index1 != index2 else []  # one line


if __name__ == '__main__':
    # print(two_sum_in_sorted_nums([], 9))
    # print(two_sum_in_sorted_nums([1], 9))
    print(two_sum_in_sorted_nums([2, 5, 7, 9, 11], 13))
    print(two_sum_in_sorted_nums([2, 5, 7, 9, 11], 12))
    print(two_sum_in_sorted_nums([2, 5, 7, 9, 11], 88))

