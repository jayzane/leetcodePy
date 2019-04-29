from typing import *


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    """
    给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
    注意:
    可以认为区间的终点总是大于它的起点。
    区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
    示例 1:
    输入: [ [1,2], [2,3], [3,4], [1,3] ]
    输出: 1
    解释: 移除 [1,3] 后，剩下的区间没有重叠。
    示例 2:
    输入: [ [1,2], [1,2], [1,2] ]
    输出: 2
    解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
    示例 3:
    输入: [ [1,2], [2,3] ]
    输出: 0
    解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
    """

    def eraseOverlapIntervals(self, intervals: List[Interval]) -> int:
        pass


def erase_overlap_intervals(intervals: List[Interval]) -> int:
    """
    :param intervals:
    :return:
    >>> i1 = Interval(1, 2)
    >>> i2 = Interval(2, 3)
    >>> i3 = Interval(3, 4)
    >>> i4 = Interval(1, 3)
    >>> erase_overlap_intervals([i1, i2, i3, i4])
    1
    >>> erase_overlap_intervals([i1, i1, i1])
    2
    >>> erase_overlap_intervals([i1, i2])
    0
    """
    max_point: int = float('-inf')
    rm_count: int = 0
    intervals.sort(key=lambda x: x.end)
    for interval in intervals:
        if interval.start >= max_point:
            max_point = interval.end
        else:
            rm_count += 1
    return rm_count


if __name__ == '__main__':
    import doctest

    doctest.testmod()
