class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val_i in enumerate(nums[:-1]):
            for j, val_j in enumerate(nums[i+1:]):
                if val_i + val_j == target:
                    return i, j+i+1