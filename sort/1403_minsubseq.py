"""
输入：nums = [4,3,10,9,8]
输出：[10,9]
解释：子序列 [10,9] 和 [10,8] 是最小的、满足元素之和大于其他各元素之和的子序列。但是 [10,9] 的元素之和最大。 
"""


class Solution:
    def minSubsequence(self, nums):
        def find(arr, res):
            sv = sum(arr)
            la = (len(arr))
            for i in range(la):
                if sv - arr[i] > m:
                    tmp = [arr[j] for j in range(la) if j != i]
                    if tmp not in res:
                        res.append(tmp)
                        find(tmp, res)

        sumv = sum(nums)
        m = sumv // 2
        res_tmp = [nums]
        find(nums, res_tmp)
        res_tmp.sort(key=lambda x: (len(x), -sum(x)))
        return sorted(res_tmp[0], reverse=True)

    def minSubsequence1(self, nums):
        nums.sort(reverse=True)
        s = sum(nums)
        ans = []
        count = 0
        for i in range(len(nums)):
            ans.append(nums[i])
            count += ans[-1]
            if count > s // 2:
                return ans
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 4, 7, 6, 7]
    nums = [8, 8]
    res1 = sol.minSubsequence(nums)
    print(res1)
