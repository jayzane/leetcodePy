class SolutionA:
    def nthUglyNumber(self, n: int) -> int:
        res = 1
        count = 0
        num = 1
        while count < n:
            i = num
            while i % 2 == 0:
                i /= 2
            while i % 3 == 0:
                i /= 3
            while i % 5 == 0:
                i /= 5
            if i == 1:
                res = num
                count += 1
            num += 1
        return res


class SolutionB:
    def nthUglyNumber(self, n: int) -> int:
        next_index = -1
        ugly_nums = [1, ]
        two_index = 0
        three_index = 0
        five_index = 0

        while len(ugly_nums) < n:
            min_num = min([ugly_nums[two_index] * 2, ugly_nums[three_index] * 3, ugly_nums[five_index] * 5])
            ugly_nums.append(min_num)
            while ugly_nums[two_index] * 2 <= ugly_nums[next_index]:
                two_index += 1
            while ugly_nums[three_index] * 3 <= ugly_nums[next_index]:
                three_index += 1
            while ugly_nums[five_index] * 5 <= ugly_nums[next_index]:
                five_index += 1
        return ugly_nums[-1]


if __name__ == '__main__':
    n = 10
    sol = SolutionB()
    print(sol.nthUglyNumber(n))
