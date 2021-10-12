from typing import List

class Solution:
    def lengthOfLIS(self, nums:List[int]) -> int:
        def myf(nums:List[int], i:int, dp:List[int]):
            if dp[i] != -1:
                return dp[i]

            a = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    a = max(myf(nums, j)+1, a)
            dp[i] = a
            return dp[i]

        res = 0
        dp = [-1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            res = max(res, myf(nums, i, dp))

        return res
    
    def lengthOfLIS2(self, nums: List[int]):
        if not nums:
            return 0
        
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        maxans = 1
        for i in range(1, n):
            dp[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxans = max(maxans, dp[i])
        return maxans