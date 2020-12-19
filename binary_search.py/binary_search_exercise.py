"""
二分查找
查找第一个等于给定值的位置
查找最后一个等于给定值的位置
查找第一个大于等于给定值的位置
查找最后一个小于等于给定值的位置
2020-12-15: 12.00.99;
2020-12-16: 11.16.06;
2020-12-18: 14:44.56;10:07.83;
"""


def find_first_a(nums, n):
    l = len(nums)
    low = 0
    high = l - 1
    while low <= high:
        m = (low + high) // 2
        if nums[m] > n:
            high = m - 1
        elif nums[m] < n:
            low = low + 1
        else:
            if m == 0 or nums[m - 1] < n:
                return m
            high = m - 1
    return -1


def find_first_greater_equal_a(nums, n):
    l = len(nums)
    low = 0
    high = l - 1
    while low <= high:
        m = (low + high) // 2
        if nums[m] >= n:
            if m == 0 or nums[m - 1] < n:
                return m
            high = m - 1
        else:
            low = low + 1
    return -1


def find_last_a(nums, n):
    l = len(nums)
    low = 0
    high = l - 1
    while low <= high:
        m = (low + high) // 2
        if nums[m] > n:
            high = m - 1
        elif nums[m] < n:
            low = low + 1
        else:
            if m == l - 1 or nums[m + 1] > n:
                return m
            low = low + 1
    return -1


def find_last_less_equal_a(nums, n):
    l = len(nums)
    low = 0
    high = l - 1
    while low <= high:
        m = (low + high) // 2
        if nums[m] > n:
            high = m - 1
        else:
            if m == l - 1 or nums[m + 1] > n:
                return m
            low = low + 1
    return -1


def find_first_b(nums, n):
    l = len(nums)
    low = 0
    high = l - 1
    while low <= high:
        m = (low + high) // 2
        if nums[m] >= n:
            high = m - 1
        else:
            low = low + 1
    if low < l and nums[low] == n:
        return low
    return -1


def find_first_greater_equal_b(nums, n):
    l = len(nums)
    low = 0
    high = l - 1
    while low <= high:
        m = (low + high) // 2
        if nums[m] >= n:
            high = m - 1
        else:
            low = low + 1
    if low < l:
        return low
    return -1


def find_last_b(nums, n):
    l = len(nums)
    low = 0
    high = l - 1
    while low <= high:
        m = (low + high) // 2
        if nums[m] > n:
            high = m - 1
        else:
            low = low + 1
    if high >= 0 and nums[high] == n:
        return high
    return -1


def find_last_less_equal_b(nums, n):
    l = len(nums)
    low = 0
    high = l - 1
    while low <= high:
        m = (low + high) // 2
        if nums[m] > n:
            high = m - 1
        else:
            low = low + 1
    if high >= 0:
        return high
    return -1


if __name__ == '__main__':
    nums = [3, 5, 5, 5, 5, 7, 9, 10]
    sol_val = find_first_a(nums, 5)
    assert sol_val == 1, 'find_first failed'
    print('find_first success')
    sol_val = find_last_a(nums, 5)
    assert sol_val == 4, 'find_last failed'
    print('find_last success')
    sol_val = find_first_greater_equal_a(nums, 6)
    assert sol_val == 5, 'find_first_greater_equal failed'
    print('find_first_greater_equal success')
    sol_val = find_last_less_equal_a(nums, 6)
    assert sol_val == 4, 'find_last_less_equal failed'
    print('find_last_less_equal success')

    sol_val = find_first_b(nums, 5)
    assert sol_val == 1, 'find_first_b failed'
    print('find_first_b success')
    sol_val = find_last_b(nums, 5)
    assert sol_val == 4, 'find_last_b failed'
    print('find_last_b success')
    sol_val = find_first_greater_equal_b(nums, 6)
    assert sol_val == 5, 'find_first_greater_equal_b failed'
    print('find_first_greater_equal_b success')
    sol_val = find_last_less_equal_b(nums, 6)
    assert sol_val == 4, 'find_last_less_equal_b failed'
    print('find_last_less_equal_b success')
