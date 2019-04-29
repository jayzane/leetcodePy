def insert_sort(nums):
    if len(nums) == 0:
        return
    elif len(nums) == 1:
        return nums
    for i in range(1, len(nums)):
        tmp = nums[i]
        for j in range(i, 0, -1):
            if nums[j - 1] > tmp:
                nums[j] = nums[j - 1]
                nums[j - 1] = tmp
    return nums


def merge_sort(nums, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(nums, start, mid)
    merge_sort(nums, mid + 1, end)
    copy_nums = nums[:]
    left_index = mid
    right_index = end
    copy_index = end
    while left_index >= start and right_index >= mid + 1:
        if nums[left_index] < nums[right_index]:
            copy_nums[copy_index] = nums[right_index]
            right_index -= 1
            copy_index -= 1
        else:
            copy_nums[copy_index] = nums[left_index]
            copy_index -= 1
            left_index -= 1
    for i in range(start, left_index + 1):
        copy_nums[copy_index] = nums[i]
        copy_index -= 1
    for j in range(mid + 1, right_index + 1):
        copy_nums[copy_index] = nums[j]
        copy_index -= 1
    for k in range(start, end + 1):
        nums[k] = copy_nums[k]

if __name__ == '__main__':
    # print(insert_sort([1, 8, 9, 7, 5]))
    nums = [1, 8, 9, 7, 5]
    merge_sort(nums, 0, len(nums) - 1)
    print(nums)
