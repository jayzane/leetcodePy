from typing import *
import collections


class Solution:
    """
    给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
    示例 1:
    输入: nums = [1,1,1,2,2,3], k = 2
    输出: [1,2]
    示例 2:
    输入: nums = [1], k = 1
    输出: [1]
    说明：
    你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
    你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    :param nums:
    :param k:
    :return:
    >>> top_k_frequent([1,1,1,2,2,3], 2)
    [1, 2]
    >>> top_k_frequent([1], 1)
    [1]
    """
    hash_map: dict = collections.defaultdict(int)
    for n in nums:
        hash_map[n] += 1
    hash_map_items: List[int, int] = list(hash_map.items())
    hash_map_items.sort(key=lambda x: x[1], reverse=True)
    return [i for i, j in hash_map_items[:k]]


# TODO: inspect
# c = collections.Counter(nums).most_common(k)
# return [v for v, _ in c]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
