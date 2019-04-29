class Solution:
    """
    实现 int sqrt(int x) 函数。
    计算并返回 x 的平方根，其中 x 是非负整数。
    由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
    示例 1:
    输入: 4
    输出: 2
    示例 2:
    输入: 8
    输出: 2
    说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
    """

    def mySqrt(self, x: int) -> int:
        pass


def my_sqrt(x: int) -> int:
    """
    :param x:
    :return:
    >>> my_sqrt(4)
    2
    >>> my_sqrt(8)
    2
    >>> my_sqrt(0)
    0
    """
    left: int = 0
    right: int = x
    while left <= right:
        mid: int = (left + right) // 2
        mid_double: int = mid * mid
        if mid_double == x:
            return mid
        elif mid_double > x:
            right = mid - 1
        else:
            left = mid + 1
    # 结束循环，left-right=1，结束循环的时如果是mid*mid>x，那应该mid-1，也就是right;
    # 如果是mid*mid<x，那应该就是mid，也同样是right
    return right


if __name__ == '__main__':
    import doctest

    doctest.testmod()
