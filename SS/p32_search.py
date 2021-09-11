import sys
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return nums[0] == target
        
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] < nums[mid]:
                # 升序
                if nums[0] < target < nums[mid]:
                    r = mid - 1
                # 非升序
                else:
                    l = mid + 1
                print('ascend: {}, {}'.format(l, r))
                # sys.exit()
            elif nums[0] > nums[mid]:
                if nums[mid] < target < nums[n-1]:
                    l = mid + 1
                else:
                    r = mid - 1
                print('descend {}, {}'.format(l, r))
                # sys.exit()
        return -1

ins = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(ins.search(nums, target))                  

                