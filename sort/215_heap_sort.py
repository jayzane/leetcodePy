from typing import *


class Solution:
    """
    在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
    示例 1:
    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5
    示例 2:
    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass


def find_kth_largest(nums: List[int], k: int) -> int:
    """
    :param nums:
    :param k:
    :return:
    >>> find_kth_largest([3,2,1,5,6,4], 2)
    5
    >>> find_kth_largest([3,2,3,1,2,4,5,5,6], 4)
    4
    >>> find_kth_largest([2,1], 2)
    1
    """
    heap: MinBHeap = MinBHeap(k)
    for i in nums:
        heap.insert(i)
    return heap.values[0]


class MinBHeap(object):
    """
    构建指定大小的小顶堆，顶部就是第k个最大元素
    """

    def __init__(self, max_items: int):
        self.max_items: int = max_items
        self.size: int = 0
        self.values: List[Optional(int)] = [None] * self.max_items

    def insert(self, val):
        index: int = self.size
        # 堆未满就插入最后位置
        if self.size < self.max_items:
            self.values[index] = val
            parent_i: int = (index - 1) // 2
            while index > 0 and val < self.values[parent_i]:
                self.values[index], self.values[parent_i] = self.values[parent_i], self.values[index]
                index = parent_i
                parent_i = (index - 1) // 2
            self.size += 1
        # 堆已满并且插入值大于小顶堆顶
        elif val > self.values[0]:
            index = 0
            self.values[index] = val
            child: int = index * 2 + 1
            while child <= self.size - 1:
                if child != self.size - 1 and self.values[child + 1] < self.values[child]:
                    child += 1
                if self.values[index] > self.values[child]:
                    self.values[index], self.values[child] = self.values[child], self.values[index]
                else:
                    break
                index = child
                child = index * 2 + 1


# TODO: inspect
# heap = nums[:k]
# heapq.heapify(heap)
# for num in nums[k:]:
#     if num > heap[0]:
#         heapq.heappushpop(heap, num)
# return heap[0]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
