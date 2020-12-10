"""
给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。


示例 1：

输入：nums = [10,2]
输出："210"
示例 2：

输入：nums = [3,30,34,5,9]
输出："9534330"
示例 3：

输入：nums = [1]
输出："1"
示例 4：

输入：nums = [10]
输出："10"

"""


class Solution:
    # 2020-12-08: 还未正确
    def largestNumber(self, nums) -> str:
        def f(arr, en):
            l = len(arr)
            if l > 1:
                res = ''
                i = len(str(max(arr))) - 1
                # i = 0
                while i >= 0:
                    bs1 = [[] for _ in range(10)]
                    for n in arr:
                        if len(str(n)) < i + 1:
                            bs1[en].append(n)
                            continue
                        s = 9 - (n // (10 ** i) % 10)
                        bs1[s].append(n)
                    arr.clear()
                    for b1 in bs1:
                        arr.extend(b1)
                    i -= 1
                res += ''.join(map(lambda x: str(x), arr))
            else:
                res = ''.join(map(lambda x: str(x), arr))
            return res

        bs = [[] for _ in range(10)]
        for n in nums:
            i = len(str(n)) - 1
            s = 9 - (n // (10 ** i) % 10)
            bs[s].append(n)
        result = ''
        for n,b in enumerate(bs):
            result += f(b, n)
        return result


if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    nums = [432,43243]
    sol = Solution()
    res1 = sol.largestNumber(nums)
    print(res1)
