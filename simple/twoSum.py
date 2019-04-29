class Solution:
    def twoSum(self, nums, target):
        size = max(nums) - min(nums)
        hashMapObj = HashMapSearch(size)
        for i in nums:
            hashMapObj.insert(i)
        for n, one in enumerate(nums):
            other = target - one
            if hashMapObj.search(other):
                if n != nums.index(other):
                    return [n, nums.index(other)]


class HashMapSearch(object):
    def __init__(self, size=100000):
        self.size = size
        self.value = [None] * size

    def hashFunc(self, data):
        return data % self.size

    def insert(self, data):
        i = self.hashFunc(data)
        step = 2
        while self.value[i] and (step / 2 < 6):
            i = i + step
            step += 2
        self.value[i] = data

    def search(self, data):
        i = self.hashFunc(data)
        return self.value[i] is not None


class SolutionB:
    def twoSum(self, nums, target):
        hashMap = {}
        for n, i in enumerate(nums):
            if i in hashMap:
                hashMap[i].append(n)
            else:
                hashMap[i] = [n]
        for n, one in enumerate(nums):
            other = target - one
            if other in hashMap:
                indexs = hashMap[other]
                for i in indexs:
                    if n == 'a':
                        pass


class SolutionC:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


if __name__ == '__main__':
    nums = [0, 4, 3, 0]
    target = 0
    sol = SolutionC()
    print(sol.twoSum(nums, target))
