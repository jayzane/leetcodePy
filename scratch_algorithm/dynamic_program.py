from typing import *


class GatherChangeMoney(object):
    """
    换零钱，只有1块，5块，11块
    """
    change_money_list: List[int] = [1, 5, 11]

    def __init__(self, change_money_list: List[int]):
        if change_money_list:
            self.change_money_list: List[int] = change_money_list

    def get_least_change_recursively(self, n: int) -> int:
        """
        最小换零钱数量(递归)
        :param n:
        :return:
        >>> gc = GatherChangeMoney([])
        >>> gc.get_least_change_recursively(15)
        3
        """
        if n <= 0:
            return 0
        return min([self.get_least_change_recursively(n - i) for i in self.change_money_list if n - i >= 0]) + 1

    def get_least_change(self, n: int, n_max: int = 100) -> int:
        """
        最小换零钱数量
        :param n:
        :param n_max: 数组长度
        :return:
        >>> gc = GatherChangeMoney([])
        >>> gc.get_least_change(15)
        3
        """
        if n <= 0:
            return 0
        array: List[int] = [0] * n_max
        for i in range(1, n + 1):
            min_num: int = float('inf')
            for j in self.change_money_list:
                if i - j < 0:
                    break
                min_num = min(min_num, array[i - j])
            array[i] = min_num + 1
        return array[n]

    def get_least_change_with_detail(self, n: int) -> List[int]:
        """
        最小数量的换零钱方案
        :param n:
        :return:
        >>> gc = GatherChangeMoney([])
        >>> gc.get_least_change_with_detail(15)
        [5, 5, 5]
        >>> gc.get_least_change_with_detail(100)
        [1, 11, 11, 11, 11, 11, 11, 11, 11, 11]
        """
        if n <= 0:
            return []
        detail: Dict[int, list] = {0: []}
        for i in range(1, n + 1):
            min_num: int = float('inf')
            tmp_map: Dict[int, int] = {}  # 在一回合比较中，记录-1，-5，-11需要的钞票张数
            for j in self.change_money_list:
                if i - j < 0:
                    break
                # 从i-1或是i-5或是i-11选择最少钞票数
                min_num = min(min_num, len(detail[i - j]))
                tmp_map[len(detail[i - j])] = i - j
            chosen: int = tmp_map[min_num]  # 选择的是i-1或是i-5或是i-11
            detail[i] = detail[chosen] + [i - chosen]
        return detail[n]

    def get_least_change_to(self, n: int) -> int:
        """
        最小换零钱数量
        TODO: 采用"我到哪里去"方式
        :param n:
        :return:
        >>> gc = GatherChangeMoney([])
        >>> gc.get_least_change_to(15)
        3
        """
        if n <= 0:
            return 0
        array: List[int] = [0] * (n + 1)
        array[1] = 1
        for i in range(1, n + 1):
            for j in self.change_money_list:
                next_n: int = i + j
                if next_n > n:
                    break
                array[next_n] = array[i] + 1
        return array[n]


class LongestIncreaseSeq(object):
    def find_lis_len(self, nums: List[int]) -> List[int]:
        """
        :param nums:
        :return:
        >>> lis = LongestIncreaseSeq()
        >>> lis.find_lis_len([1,5,3,4,6,9,7,8])
        6
        """
        tmp_data: dict = {}
        self.find_lis_core(nums, len(nums) - 1, tmp_data)
        tmp_data_l: List(Tuple(int, int)) = list(tmp_data.items())
        tmp_data_l.sort(key=lambda x: x[1], reverse=True)
        return tmp_data_l[0][1]

    def find_lis_core(self, nums: List[int], index_x: int, tmp_data: dict) -> int:
        """
        :param nums:
        :param index_x: 以第x位的数字结尾的最长序列
        :param tmp_data: 用来储存已经计算的
        :return:
        """
        if index_x < 0:
            return 0
        elif index_x == 0:
            return 1
        if index_x in tmp_data:
            return tmp_data[index_x]
        index_p: int = index_x - 1
        if nums[index_p] > nums[index_x]:
            tmp_data[index_x] = self.find_lis_core(nums, index_p, tmp_data)
        else:
            tmp_data[index_x] = self.find_lis_core(nums, index_p, tmp_data) + 1
        return tmp_data[index_x]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
