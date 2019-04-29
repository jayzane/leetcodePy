from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for day in range(len(prices) - 1):
            differ = prices[day + 1] - prices[day]
            if differ > 0:
                profit += differ
        return profit


def max_profit(prices: List[int]) -> int:
    pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()
