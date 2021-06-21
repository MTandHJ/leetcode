### Easy ####
# 找到旋转数组排序数组中最小值

# record : June 19, 2021. 1
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 双指针
        # 两个准则：
        # 1. pivot 小于high时，则需要扔掉右边的
        #   但是在更新时，需要保留下pivot的索引，因为它可能是最小值所在位置
        # 2. 当pivot 大于high, 则需要扔掉左边的
        #   更新时, 扔掉包括pivot的左边
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high = pivot
        return nums[low]

if __name__ == '__main__':
    ins = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(ins.findMin(nums))