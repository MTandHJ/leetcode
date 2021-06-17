from typing import List
import copy

# 官方 一遍
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 交换数组中两个元素，因为nums[i]已经填写过了
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res

# 自己 一遍
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
            
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res
    
    # labuladong 一遍    
    def permute(self, nums):
        # 结果集合
        res = []
        def backtrack(nums, track):
            # nums：路径
            # track：选择列表

            # 如果满足结束条件，即里面的元素都添加进去
            # 从第一个元素到最后一个元素都添加进去了
            if len(track) == len(nums):
                # 一定要这样, 否则会产生最终所有元素都为空的情况
                # new_track = copy.deepcopy(track)
                # res.append(new_track)
                res.append(track[:])
                return

            # 选择列表是在nums[i]中
            for i in range(n):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                backtrack(nums, track)
                track.pop()
            return res

        n = len(nums)
        track = []
        backtrack(nums, track)
        return res

if __name__ =="__main__":
    ins = Solution()
    nums = [1, 2, 3]
    print(ins.permute(nums))
