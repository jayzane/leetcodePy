from typing import *


class Solution:
    """
    给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

    示例:

    输入: "25525511135"
    输出: ["255.255.11.135", "255.255.111.35"]
    """

    def restoreIpAddresses(self, s: str) -> List[str]:
        pass


def restore_ip_addresses_back(s: str) -> List[str]:
    """
    :param s:
    :return:
    """

    def left_addresses(left_s: str, deep: int) -> List[str]:
        len_left: int = len(left_s)
        # print(left_s, deep)
        if deep > 3:  # 255.255.255.255.255
            return []
        elif deep == 3:
            if int(left_s) < 256:
                return [left_s]
            else:
                return []  # # 255.255.255.2552
        elif len_left <= 1:
            return []
        elif len_left == 2:
            if deep == 2:
                return [left_s[0], left_s[1]]
            else:
                return []
        else:
            tmp: List[str] = []
            for start in range(3):
                if int(left_s[:start + 1]) > 255 or not left_s[start + 1:]:
                    break
                for l in left_addresses(left_s[start + 1:], deep + 1):
                    tmp.append('%s.%s' % (left_s[:start + 1], l))
            return tmp

    return left_addresses(s, 0)


def restore_ip_addresses(s: str) -> List[str]:
    """
    :param s:
    :return:
    >>> restore_ip_addresses("25525511135")
    ['255.255.11.135', '255.255.111.35']
    >>> restore_ip_addresses("0000")
    ['0.0.0.0']
    """

    def left_addresses(left_s: str, deep: int, tmp_str: str, restored: List[str]) -> None:
        len_left: int = len(left_s)
        if len_left == 0:
            if deep == 4:
                restored.append(tmp_str)
            return
        elif deep > 4 or (len_left > 0 and deep == 4):
            return
        for i in range(3):
            # eg1. i=1 and left_s='025' eg2. i=1 or 2 when left_s='25' is same
            if i > 0 and left_s[0] == '0' or i + 1 > len_left:
                break
            t: str = tmp_str
            ip_s: str = left_s[:i + 1]
            if ip_s and int(ip_s) < 256:
                if not tmp_str:
                    tmp_str = left_s[:i + 1]
                else:
                    tmp_str += '.%s' % left_s[:i + 1]
                left_addresses(left_s[i + 1:], deep + 1, tmp_str, restored)
                tmp_str = t

    res: List[str] = []
    left_addresses(s, 0, '', res)
    return res


if __name__ == '__main__':
    import doctest

    doctest.testmod()
