class Solution:
    def findKthLargest(self, nums, k):
        heap = MinBHeap(k)
        for i in nums:
            heap.insert(i)
        return heap.values[1]


class MinBHeap(object):
    def __init__(self, max_items=100000, minint=-9999999):
        self.max_items = max_items + 1
        self.size = 1
        self.values = [None] * self.max_items
        self.values[0] = minint

    def insert(self, val):
        index = self.size
        if self.size > 1:
            if self.size < self.max_items:
                self.values[index] = val
                while index > 0 and val < self.values[index // 2]:
                    self.values[index] = self.values[index // 2]
                    index //= 2
                self.values[index] = val
                self.size += 1
            elif val > self.values[1]:
                index = 1
                while index * 2 < self.size:
                    child = index * 2
                    if child != self.size - 1 and self.values[child + 1] < self.values[child]:
                        child += 1
                    if val > self.values[child]:
                        self.values[index] = self.values[child]
                    else:
                        break
                    index = child
                self.values[index] = val
        else:
            self.values[1] = val
            self.size += 1


if __name__ == '__main__':
    k = 4
    nums = [3,2,3,1,2,4,5,5,6]
    sol = Solution()
    res = sol.findKthLargest(nums, k)
    print('%sth largest is %s' % (k, res))
