class Solution:
    def threeSumClosest(self, nums, target):
        pass

    def findClosest(self, nums, start, end, target):
        midI = (end + start) // 2
        length = len(nums)
        if start == end:
            if target == nums[start]:
                return target
            if start == 0:
                return nums[start + 1] if abs(target - nums[start]) > abs(target - nums[start + 1]) else nums[start]
            if end == length - 1:
                return nums[end - 1] if abs(target - nums[end]) > abs(target - nums[end - 1]) else nums[end]
            if abs(target - nums[start]) > abs(target - nums[start + 1]):
                if abs(target - nums[end]) > abs(target - nums[end - 1]):
                    return nums[end - 1]
                else:
                    return nums[start]
            else:
                return nums[start]
        if target == nums[midI]:
            return nums[midI]
        elif target > nums[midI]:
            return self.findClosest(nums, midI + 1, end, target)
        else:
            return self.findClosest(nums, start, midI, target)


class SolutionB:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closetNum = nums[0] + nums[1] + nums[2]
        res = [0, 1, 2]
        for i, _ in enumerate(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]
                if abs(threeSum - target) < abs(closetNum - target):
                    closetNum = threeSum
                if threeSum < target:
                    j += 1
                elif threeSum > target:
                    k -= 1
                else:
                    print('closeNum:%s indexs:%s', closetNum, ','.join(map(str, res)))
                    return target
        print('closeNum:%s indexs:%s', closetNum, ','.join(map(str, res)))
        return closetNum


if __name__ == '__main__':
    nums = [2, 3, 6, 9]
    nums = [-1, 2, 1, -4]
    target = 1
    sol = SolutionB()
    # length = len(nums)
    # print(sol.findClosest(nums, 0, length - 1, 4))
    sol.threeSumClosest(nums, target)
