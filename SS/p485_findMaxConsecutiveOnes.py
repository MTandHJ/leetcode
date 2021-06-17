from typing import List


### 第一次，
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        def find_continue(nums):
            counters = []
            # 1 首先计算出不同的数值
            diff_num = nums[0]
            count = 0
            for i, n_i in enumerate(nums):
                if n_i == 1:
                    count += 1
                elif n_i != 1:
                    # print('this is different!')
                    counters.append(count)
                    count = 0
                    diff_num = n_i

                if i == len(nums)-1:
                    counters.append(count)
            return counters

        # return counters
        if nums == []:
            return 0
        elif set(nums) == {0}:
            return 0
        else:
            return max(find_continue(nums))

### 第二次，使用双指针
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # 找前面最大的
        # slow fast代表前面第一个为1的索引，加上最后一个的索引
        # 反过来看好像是fast充当了计数器的角色
        max_cont = 0
        slow = fast = 0
        for i, v in enumerate(nums):
            if v == 1:
                fast += 1
            else:
                if fast - slow > max_cont:
                    max_cont = fast-slow
                fast = slow = i + 1
                # fast = slow = i + 1
                # 也可以这样写，最后可以输出连续起始的位置
                # 以及连续终止的位置
        # 最后一次连续的可能是最大的        
        if fast - slow > max_cont:
            return fast - slow
        return max_cont