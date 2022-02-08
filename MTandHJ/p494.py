

from typing import List

from base import version


class Solution:

    @version("dfs: 692ms, 43.8mb")
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memory = dict()
        def search(nums, target):
            if len(nums) == 0:
                if target == 0:
                    return 1
                else:
                    return 0
            key = str(len(nums)) + ';' + str(target)
            try:
                return memory[key]
            except KeyError:
                ans = []
                ans.append(search(nums[1:], target + nums[0]))
                ans.append(search(nums[1:], target - nums[0]))
                memory[key] = sum(ans)
                return memory[key]
        return search(nums, target)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = abs(target)
        new_nums = []
        for num in nums:
            if num != 0:
                new_nums.append(num)
        factor = len(nums) - len(new_nums)
        nums = new_nums
        target = (sum(nums) + target)
        if target % 2 != 0:
            return 0
        target = target // 2
        m = len(nums)
        vdp = [[0] * (target + 1) for _ in range(m + 1)]
        ndp = [[0] * (target + 1) for _ in range(m + 1)]
        ndp[0][0] = 1
        for i in range(1, m + 1):
            for j in range(1, target + 1):
                v = nums[i - 1]
                nxt = vdp[i - 1][max(0, j - v)] + v
                nxt = -1 if nxt > j else nxt
                if vdp[i - 1][j] <= nxt:
                    vdp[i][j] = nxt 
                    if vdp[i][j] == j:
                        ndp[i][j] = sum([ndp[k][max(0, j - v)] for k in range(i)])
                else:
                    vdp[i][j] = vdp[i - 1][j]
        return sum([row[-1] for row in ndp]) * 2 ** factor

    @version("dp: 104ms, 14.9mb")
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = sum(nums) + target
        if target % 2 != 0 or target < 0:
            return 0
        target = target // 2
        m = len(nums)
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, m + 1):
            for j in range(target, -1, -1): # -1 not 0 !!!!!!!
                v = 0 if j < nums[i - 1] else dp[j - nums[i - 1]]
                dp[j] += v
        return dp[-1]

