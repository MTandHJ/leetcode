

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        _sum = 0
        for num in nums:
            _sum += num
        
        if _sum & 1 == 1:
            return False
        
        target = sum // 2
        dp = [[False] * (target + 1) for _ in range(n)]
        if nums[0] <= target:
            dp[0][nums[0]] = True
        
        for i in range(n):
            for j in range(target + 1):
                dp[i][j] = dp[i-1][j]
                if nums[i] == j:
                    dp[i][j] = True
                    continue
                if nums[i] < j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i]]
        return dp[-1][-1]

    def canPartition1(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False
        
        target = total // 2
        if maxNum > target:
            return False
        
        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        
        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-num]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]