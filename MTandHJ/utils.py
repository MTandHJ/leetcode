



from typing import List


def binarySearch(nums, key) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == key:
            return m
        elif nums[m] > key:
            r = m - 1
        else:
            l = m + 1
    return -1


def binarySearch(nums, key) -> int:
    if len(nums) == 1:
        return 0
    m = (len(nums) - 1) // 2
    if nums[m] == key:
        return m
    elif nums[m] > key:
        return binarySearch(nums[:m], key)
    else:
        return m + 1 + binarySearch(nums[m+1:], key)
