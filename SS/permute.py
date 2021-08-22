
from typing import List
class Solution:
    def permute(self, nums: List[int]):
        # 记录路径
        track = []
        self.res = []
        self.backtrack(nums, track)
        return self.res
    
    # 路径：记录在track中
    # 选择列表： nums中不存在track中的那些元素
    # 结束条件：nums中的元素都在track中出现
    def backtrack(self, nums: List[int], track: List[int]):
        # print(len(track), len(nums))
        # # 触发当前层递归的结束条件
        if len(track) == len(nums):
            # 这里需要加上track[:]
            # 因为python中列表是会变化的
            # 在不同的backtrack中，使用的是一个track
            # 后一步的backtrack，会影响到之前添加的track
            # 这里使用浅拷贝来避免这种“会被影响的”情况
            self.res.append(track[:])
            return 

        for i in range(len(nums)):
            # 当它已经选择过了
            if nums[i] in track:
                continue
            # 做选择
            track.append(nums[i])
            # 进入下一层选择树
            self.backtrack(nums, track)
            # 撤销选择，去找新的可以做选择的点
            track.pop()

if __name__ == '__main__':
    ins = Solution()
    nums = [1, 2, 3]
    print(ins.permute(nums))
