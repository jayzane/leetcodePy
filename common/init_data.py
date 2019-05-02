"""
some random init data to test
"""
import random
from typing import *

MAX_NUM = 99999999


def random_nums(length: int = 100, sorted_flag: int = 0,
                has_negative: bool = False, has_dup: bool = False,
                max_num: int = 0) -> List[int]:
    """
     Get init nums in list
    :param length:
    :param sorted_flag: 0 is not sorted, -1 is reverse sorted, 1 is sorted
    :param has_negative:
    :param has_dup:
    :param max_num:
    :return:
    """
    max_num = MAX_NUM if max_num == 0 else max_num
    start = -max_num if has_negative else 0
    result = []
    for _ in range(length):
        rand_int = random.randrange(start, max_num)
        while not has_dup and rand_int in result:
            rand_int = random.randrange(start, max_num)
        result.append(rand_int)
    if sorted_flag > 0:
        result.sort()
    elif sorted_flag < 0:
        result.sort(reverse=True)
    return result


if __name__ == '__main__':
    print(random_nums(10, max_num=100))
