import math


class Solution:
    """
    给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
    示例1:
    输入: 5
    输出: True
    解释: 1 * 1 + 2 * 2 = 5
    示例2:
    输入: 3
    输出: False
    """

    def judgeSquareSum(self, c: int) -> bool:
        pass


def judge_square_sum_back(c: int) -> bool:
    if c is None or c < 0:
        return False
    index1: int = 0
    index2: int = c
    while index1 <= index2:
        tmp_sum: int = index1 ** 2 + index2 ** 2
        if tmp_sum > c:
            index2 -= 1
        elif tmp_sum < c:
            index1 += 1
        else:
            break
    return True if index1 <= index2 else False


def judge_square_sum(c: int) -> bool:
    """
    a and b at least one more than or equal sqrt(c / 2), all less than or equal sqrt(c)
    TODO: 定理：某个正整数是两平方数之和，当且仅当该正整数的所有 4k+3 型素因数的幂次均为偶数。
    任何一个正整数都可以因数分解为 c = (2^r)*(p1^n1)*(p2^n2)*...*(pk^nk)，其中p1...pk为素因数，n1...nk为因数的幂次。
    也就是说有一个形如4k+3的素因数pi，如果ni为奇数，那它就不可能被写为两个整数的平方数之和了。
    :param c:
    :return:
    """
    if c is None or c < 0:
        return False
    index1: int = int(math.sqrt(c / 2))
    index2: int = int(math.sqrt(c))
    for i in range(index2, index1 - 1, -1):
        other: int = math.sqrt(c - i * i)
        if int(other) == other:
            return True
    return False


if __name__ == '__main__':
    print(judge_square_sum(3))
    print(judge_square_sum(4))
    print(judge_square_sum(5))
    print(judge_square_sum(10000000))
    print(judge_square_sum(0))
    print(judge_square_sum(-100))
    print(judge_square_sum(None))
    print(judge_square_sum(26))
