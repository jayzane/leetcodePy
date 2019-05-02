import math


class Prime(object):
    def __init__(self, max_n=0, n=0):
        """
        :param max_n: 最大自然数
        :param n: 按序前面n个素数
        """
        self.max_n = max_n
        self.n = n
        self.guess_max_n()

    def guess_max_n(self, left=100, right=1000000, ratio=10):
        if not self.max_n:
            self.max_n = right
            count = (right // left) // ratio
            candidate_list = []
            for i in range(count):
                candidate_list.append(left * (i + 1))
            for x in candidate_list:
                if x / math.log(x) >= self.n:
                    self.max_n = x
                    break

    def find_prime_less_than_n(self):
        pass

    def find_prime_n_in_order(self):
        pass

    def get_prime_by_trial_division(self):
        num = 3
        last_prime = [2, ]
        while num <= self.max_n:
            for prime in last_prime:
                if num % prime == 0:
                    break
            else:
                last_prime.append(num)
            num += 1
        return last_prime

    def get_prime_by_sieve(self):
        array_flag = [True] * (self.max_n - 1)
        for num in range(2, int(math.sqrt(self.max_n)) + 1):
            if array_flag[num - 2]:
                for i in range(num ** 2, self.max_n + 1, num):
                    array_flag[i - 2] = False
        return [num for num in range(2, self.max_n + 1) if array_flag[num - 2]]


if __name__ == '__main__':
    p = Prime(max_n=100)
    # print(p.get_prime_by_trial_division())
    print(p.get_prime_by_sieve())
