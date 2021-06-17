
from typing import List
import bisect
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # params:
        # s: 我们的目标最小值，要求的最小长度要大于这个最小值s
        # nums：我们的数字列表集合
        # 如果是空集
        if not nums:
            return 0
        
        # 求出长度
        n = len(nums)
        # 初始化最后的插入的地方，是n+1
        # 插到末尾
        ans = n + 1
        # 累计和
        # New： 相当于是求的累计和
        # 即便是sums[-1] 它代表的是前面的累计和，再新加上一个数，相当于是到后面的累计和
        # sums = [0]
        # for i in range(n):
        #     sums.append(sums[-1] + nums[i])
        sums = [0] * (n+1)
        for i in range(n):
            sums[i] = sums[i-1] + nums[i]
        
        # 后面n个累计和
        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))
        
        return 0 if ans == n + 1 else ans

if __name__ == "__main__":
    ins = Solution()
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    print(ins.minSubArrayLen(target, nums))


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        ans = n + 1
        sums = [0] * (n+1)
        
        for i in range(1, n+1):
            sums[i] = sums[i-1] + nums[i-1]

        for i in range(1, n):
            new_target = target + nums[i-1]
            bound = bisect.bisect_left(sums, new_target)
            if bound != len(sums):
                ans = min(ans, bound - (i-1))
        
        return 0 if ans == n+1 else ans


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s:
            return 0
        
        n = len(nums)
        ans = n + 1
        sums = [0] * (n+1)
        
        for i in range(1, n+1):
            sums[i] = sums[i-1] + nums[i-1]

        for i in range(1, n+1):
            target = s + sums[i-1]
            # bound = self.lowerBound(sums, target)
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - (i-1))
        
        return 0 if ans == n+1 else ans

    def lowerBound(self, a, l, r, target):
        # mid, L, R = -1, l, r
        mid = -1
        while l < r:
            mid = (l +r) // 2
            if a[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l if a[l] >= target else -1


if __name__ == "__main__":
    ins = Solution()
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    print(ins.minSubArrayLen(target, nums))

