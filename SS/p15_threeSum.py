
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        # 枚举a
        for first in range(n):
            # 需要在上次的右边
            # 且与上次的值不相等
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c从右边开始减少
            third = n - 1
            # 目标值, 希望我们的能够
            target = -nums[first]
            # 枚举b
            for second in range(first + 1, n):
                # NOTE: 下面要是second > first + 1，这说明前面已经有遍历过一次secondl
                # 我们需要与前一次遍历过的second相对比
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 保证second, third顺序
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合,b会继续增加
                # 但是这时就没有满足a + b + c=0的b, c, 退出循环
                if second == third:
                    break

                if nums[second] + nums[third] == target:
                    res.append([nums[first], nums[second], nums[third]])
            
        return res