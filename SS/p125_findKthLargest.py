
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k:int) -> None:
        self.buildMaxHeap(nums)
        n = len(nums)
        # 调整 k - 1次
        for i in range(n-1, n-k, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)
        # 此时，堆顶的元素就是第k大的数据
        return nums[0]

    def buildMaxHeap(self, a: List[int]) -> None:
        # 从卒子后一个非叶子节点开始调增大顶堆
        # 最后一个非叶子节点的下表就是len(nums)
        n = len(a)
        for i in range(n // 2 - 1, -1, 0):
            self.heapify(a, n, i)

    # 调整大顶堆，第三个参数表示剩余未排序的数字的数量，也是剩余堆的大小
    def heapify(self, a, n, i):
        largest = i 
        l = 2 * i + 1
        r = 2 * i + 2
        # 与左子树、右子树比较
        if l < n and a[i] < a[l]:
            largest = l
        if r < n and a[largest] < a[r]:
            largest = r 
        # 将最大值交换未根节点
        if i != largest:
            a[i], a[largest] = a[largest], a[i]
            # 再次调整交数字后的大顶堆
            self.heapify(a, n, i)
        