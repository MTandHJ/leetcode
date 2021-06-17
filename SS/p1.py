from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val_i in enumerate(nums[:-1]):
            for j, val_j in enumerate(nums[i+1:]):
                if val_i + val_j == target:
                    return i, j+i+1

# 使用hash表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 初始化空数组
        res = dict()
        for i, num in enumerate(nums):
            # 当原数组中存在有这个差值时，返回，已经找到
            if target - num in res:
                return res[target - num], i
            # 没找到就继续往res里面添加元素
            # 这里面存放可能是两者之差的数据
            res[num] = i
        return -1, -1

if __name__ == "__main__":
    ins = Solution()
    nums = [2,7,11,15]
    target = 9
    ins.twoSum(nums, target)