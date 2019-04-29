class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.heap = MinBHeap(k)
        for i in nums:
            self.heap.insert(i)

    def add(self, val: int) -> int:
        self.heap.insert(val)
        return self.heap.values[1]


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

    def delete_min(self):
        max_num = self.values[1]
        last_num = self.values[self.size - 1] if self.size - 1 > 1 else None
        index = 1
        while index * 2 < self.size:
            child = index * 2
            if child != self.size - 1 and self.values[child + 1] > self.values[child]:
                child += 1
            if last_num < self.values[child]:
                self.values[index] = self.values[child]
            else:
                break
            index = child
        self.size -= 1
        self.values[index] = last_num
        return max_num


if __name__ == '__main__':
    input_web = [[7, [-10, 1, 3, 1, 4, 10, 3, 9, 4, 5, 1]], [3], [2], [3], [1], [2], [4], [5], [5], [6], [7], [7], [8],
                 [2], [3], [1], [1], [1], [10], [11], [5], [6], [2], [4], [7], [8], [5], [6]]
    # k = 3
    k = input_web[0][0]
    # nums = [4, 5, 8, 2]
    nums = input_web[0][1]
    obj = KthLargest(k, nums)
    for i in input_web[1:]:
        print('%sth largest is %s' % (k, obj.add(i[0])))
    # for i in [3, 5, 10, 9, 4]:
    #     print('%sth largest is %s' % (k, obj.add(i)))
    # h = MaxBHeap()
    # for i in nums:
    #     h.insert(i)
    # print(h.values[:10])
    # print(h.delete_max())
    # print(h.values[:10])
