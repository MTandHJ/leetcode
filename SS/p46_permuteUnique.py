
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]):
        res = []
        perm = []
        self.vis = [0 for _ in range(len(nums))]

        nums.sort()
        self.backtrack(nums, res, 0, perm)
        return res
    
    def backtrack(self, nums, res, idx, perm):
        # 到这一步说明已经遍历完一个数组了
        if idx == len(nums):
            res.append(perm[:])
            # return 
        for i in range(len(nums)):
            # 当访问过
            # 或者访问的一层，跟之前的是一样的
            if self.vis[i] or (i > 0 and nums[i] == nums[i-1] and not self.vis[i-1]):
                continue
            # 经典的回溯框架
            perm.append(nums[i])
            self.vis[i] = 1
            self.backtrack(nums, res, idx+1, perm)
            self.vis[i] = 0
            perm.pop()
    
    def permute2(self, nums):
        def backtrack(first=0):
            print(first)
            if first == n:
                res.append(nums[:])
                return 
            for i in range(n-1):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[first], nums[i]
        n = len(nums)
        res = []
        backtrack()
        return res

ins = Solution()
print(ins.permute2([1, 2, 3]))
        
        
        