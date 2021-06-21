### Easy ####

# record: June 20, 2021. 15:06

from typing import List

class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        i, j = 0, 0
        # 最后输出i， j之间的差距试0的个数
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

class Solution:
    def moveZeros(self, nums:List[int]) -> None:
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        
if __name__ == '__main__':
    ins = Solution()
    nums = [0, 1, 0, 3, 12]
    ins.moveZeros(nums)
    print(nums)