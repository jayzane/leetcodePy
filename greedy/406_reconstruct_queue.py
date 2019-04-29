from typing import *


class Solution:
    """
    假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。
    注意：
    总人数少于1100人。
    示例
    输入:
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    输出:
    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
    """

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        pass


def reconstruct_queue(people: List[List[int]]) -> List[List[int]]:
    """
    h为身高，k为排在这个人前面且身高大于或等于h的人数
    身高矮的插入身高高的前面，不影响身高高的k值
    :param people:
    :return:
    >>> reconstruct_queue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
    [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    >>> reconstruct_queue([])
    [[]]
    >>> reconstruct_queue([[9, -1]])
    [[]]
    """
    if len(people) <= 0 or not people[0] or people[0][0] < 0 or people[0][1] < 0:
        return [[]]
    people_copy: List[List[int]] = people[:]  # 为了不改变输入参数
    res: List[List[int]] = []
    people_copy.sort(key=lambda x: (-x[0], x[1]))
    for pp in people_copy:
        res.insert(pp[1], pp)
    return res


if __name__ == '__main__':
    import doctest

    doctest.testmod()
