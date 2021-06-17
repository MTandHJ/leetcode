from typing import List

## 第一次最蠢的方法：
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 找到中心的下标
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i

        return -1

# 查看别人解答：
# 思路：两边的和相等，
# 那就说明total_sum - nums[i] = 2 * left_sum = 2 * right_sum
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # (1) 首先计算总和 与总长度
        total_sum = sum(nums)
        n = len(nums)
        # 判断第一个是
        if total_sum == nums[0]:
            return 0

        # (2) 开始从第二个元素判断
        left_sum = 0
        for i in range(1, n):
            left_sum += nums[i-1]
            if total_sum - nums[i] == 2 * left_sum:
                return i
        
        return -1