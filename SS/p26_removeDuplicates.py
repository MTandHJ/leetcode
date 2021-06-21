### Easy ####
# in: nums
# out: index of no duplicate elements

#  record: June 20, 2021. 10:31

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        slow, fast = 1, 1
        # 当数组长度为1时，不执行这一步
        while fast < len(nums):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow

if __name__ == '__main__':
    ins = Solution()
    nums = [1, 1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    for i in range(ins.removeDuplicates(nums)):
        print(nums[i], end=' ')