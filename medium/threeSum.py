class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i, _ in enumerate(nums):
            if i == 0 or nums[i-1] < nums[i]:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    s = nums[i] + nums[j] + nums[k]
                    if s == 0:
                        tmpL = [nums[i], nums[j], nums[k]]
                        res.append(tmpL)
                        k -= 1
                        j += 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
                    elif s < 0:
                        j += 1
                    else:
                        k -= 1
        return res


class SolutionB:
    def threeSum(self, nums):
        nums.sort()
        res =[]
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i]>nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] +nums[r]
                    if s ==0:
                        res.append([nums[i],nums[l],nums[r]])
                        l +=1
                        r -=1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s>0:
                        r -=1
                    else :
                        l +=1
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))