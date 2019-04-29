from typing import *
import collections


class Solution:
    """
    字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。
    示例 1:
    输入: S = "ababcbacadefegdehijhklij"
    输出: [9,7,8]
    解释:
    划分结果为 "ababcbaca", "defegde", "hijhklij"。
    每个字母最多出现在一个片段中。
    像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
    注意:
    S的长度在[1, 500]之间。
    S只包含小写字母'a'到'z'。
    """

    def partitionLabels(self, S: str) -> List[int]:
        pass


def partition_labels_back(S: str) -> List[int]:
    """
    consumed: 60ms 60ms
    :param S:
    :return:
    >>> partition_labels_back('ababcbacadefegdehijhklij')
    [9, 7, 8]
    >>> partition_labels_back('eccbbbbdec')
    [10]
    """
    if not S:
        return []
    last_index_map: Dict[str, int] = collections.defaultdict(int)
    len_text: int = len(S)
    for i in range(len_text):
        last_index_map[S[i]] = i  # 每个字符在S中所处的最后位置
    res: List[int] = []
    first_index: int = 0  # 一轮比较的首字符位置
    while first_index < len_text:
        # 动态的调整末尾字符位置，比如'a'在[0,2,3]位置'b'在[1,4,5]位置
        # 则末尾字符为b，且位置为5
        last_index: int = last_index_map[S[first_index]]
        index_i: int = first_index
        while index_i <= last_index:
            index = last_index_map[S[index_i]]
            if index > last_index:
                last_index = index
            index_i += 1
        res.append(last_index - first_index + 1)
        first_index = last_index + 1
    return res


def partition_labels(S: str) -> List[int]:
    """
    consumed: 68ms 64ms
    :param S:
    :return:
    >>> partition_labels('ababcbacadefegdehijhklij')
    [9, 7, 8]
    >>> partition_labels('eccbbbbdec')
    [10]
    """
    first_index: int = 0
    res = []
    while first_index < len(S):
        last_index: int = S.rfind(S[first_index])
        index = first_index + 1
        while index <= last_index:
            last_index = max(last_index, S.rfind(S[index]))
            index += 1
        res.append(last_index - first_index + 1)
        first_index = last_index + 1
    return res


if __name__ == '__main__':
    import doctest

    doctest.testmod()
