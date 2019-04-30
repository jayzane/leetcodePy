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


def restore_ip_addresses(s: str) -> List[str]:
    """
    :param s:
    :return:
    # >>> restore_ip_addresses("25525511135")
    # ['255.255.11.135', '255.255.111.35']
    >>> restore_ip_addresses("0000")

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
                if int(left_s[:start+1]) > 255 or not left_s[start+1:]:
                    # tmp = []
                    break
                print(left_s[start+1:], deep+1)
                for l in left_addresses(left_s[start+1:], deep + 1):
                    tmp.append('%s.%s' % (left_s[:start+1], l))
            return tmp

    return left_addresses(s, 0)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
