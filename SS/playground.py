from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 使用循环数组，取余的运算
        n = len(nums)
        new_li = [nums[(i + k) % n] for i in range(n)]
        for i in range(n):
            nums[i] = new_li[i]
        print(nums)


if __name__ == "__main__":
    ins = Solution()
    a = ins.rotate([-1, -100, 3, 99], 2)
    print(a)


