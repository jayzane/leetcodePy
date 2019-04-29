from typing import *
import operator


class Solution:
    """
    给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。
    示例 1:
    输入: "2-1-1"
    输出: [0, 2]
    解释:
    ((2-1)-1) = 0
    (2-(1-1)) = 2
    示例 2:
    输入: "2*3-4*5"
    输出: [-34, -14, -10, -10, 10]
    解释:
    (2*(3-(4*5))) = -34
    ((2*3)-(4*5)) = -14
    ((2*(3-4))*5) = -10
    (2*((3-4)*5)) = -10
    (((2*3)-4)*5) = 10
    """

    def diffWaysToCompute(self, input: str) -> List[int]:
        pass


# def diff_ways_to_compute_back(input: str) -> List[int]:
#     """
#     :param input:
#     :return:
#     >>> diff_ways_to_compute_back('2-1-1')
#     [2, 0]
#     >>> diff_ways_to_compute_back('2*3-4*5')
#     [-34, -10, -14, 10]
#     >>> diff_ways_to_compute_back('')
#     []
#     >>> diff_ways_to_compute_back('2')
#     []
#     """
#     op_i: int = get_input_op(input)
#     if op_i > 0:
#         return str_compute(input[:op_i], input[op_i + 1:], input[op_i])
#     else:
#         return []
#
#
# def get_input_op(s: str) -> int:
#     """
#     获取第一个operator的位置
#     :param s:
#     :return:
#     >>> get_input_op('1+3')
#     1
#     >>> get_input_op('')
#     -1
#     """
#     add_i: int = s.find('+')
#     sub_i: int = s.find('-')
#     mul_i: int = s.find('*')
#     op_i: int = max(add_i, sub_i, mul_i)
#     if op_i < 0:
#         return op_i
#     else:
#         return min(filter(lambda x: x > 0, [add_i, sub_i, mul_i]))
#
#
# def str_compute(a: str, b: str, c: str, op1: str, op2: str) -> List[int]:
#     symbol_map: dict = {
#         '+': operator.add,
#         '-': operator.sub,
#         '*': operator.mul,
#     }
#     if not op2:
#         if not op1:
#             pass
#     op_i: int = get_input_op(b)
#     op_i_2: int = get_input_op(b[op_i + 1:])
#     if op_i_2 > 0:
#         res_1: List[int] = [symbol_map[op](int(a), x) for x in str_compute(b[:op_i], b[op_i + 1:], b[op_i])]
#
#         tmp1: int = symbol_map[op](int(a), int(b[:op_i]))
#         res_2: List[int] = str_compute(str(tmp1), b[op_i + 1:], b[op_i])
#         res_1.extend(res_2)
#         return res_1
#     else:
#         return [symbol_map[op](int(a), int(b))]


def diff_ways_to_compute(input: str) -> List[int]:
    """
    :param input:
    :return:
    >>> diff_ways_to_compute('2-1-1')
    [2, 0]
    >>> diff_ways_to_compute('2*3-4*5')
    [-34, -10, -14, -10, 10]
    >>> diff_ways_to_compute('')
    []
    >>> diff_ways_to_compute('11')
    [11]
    """
    if not input:
        return []
    symbol_map: dict = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    index: int = 0
    result = []
    len_input: int = len(input)
    while index < len_input:
        s: str = input[index]
        if s in ['+', '-', '*']:
            left: List[int] = diff_ways_to_compute(input[:index])
            right: List[int] = diff_ways_to_compute(input[index+1:])
            for l in left:
                for r in right:
                    result.append(symbol_map[s](int(l), int(r)))
        index += 1
    return result if result else [int(input)]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
