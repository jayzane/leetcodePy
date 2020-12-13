"""
给你一个字符串 s 和一个 长度相同 的整数数组 indices 。

请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。

返回重新排列后的字符串。
输入：s = "codeleet", indices = [4,5,6,7,0,2,1,3]
输出："leetcode"
解释："codeleet" 重新排列后变为 "leetcode" 。
2020-12-11: 05:00.00;
"""


class Solution:
    def restoreString1(self, s: str, indices) -> str:
        l = len(indices)
        res = [None for _ in range(l)]
        for i in range(l):
            res[indices[i]] = s[i]
        return ''.join(res)

    def restoreString2(self, s: str, indices) -> str:
        res = list(s)
        for i in range(len(indices)):
            res[indices[i]] = s[i]
        return ''.join(res)


if __name__ == '__main__':
    s = "codeleet"
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    sol = Solution()
    res1 = sol.restoreString2(s, indices)
    print(res1)
