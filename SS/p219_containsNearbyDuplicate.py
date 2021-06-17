from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 为空的情形
        if not nums:
            return False
        n = len(nums)
        
        # 从0, 1, n-k-1
        for i in range(n-k):
            cur = nums[i: i+k]
            print(cur)
            if len(cur) != 1 and self.find_idx(cur):
                return True
            else:
                return False

    # 二分法找到这个Index
    def find_idx(self, li, num):
        if not li or not isinstance(num, int):
            return False
        
        low , high = 0, len(li)-1
        while low <= high:
            mid = (low+high) // 2
            if li[mid] == num:
                return mid
            elif li[mid] > num:
                high = mid - 1
            else:
                low = mid + 1

        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
            if len(hashset) > k:
                hashset.remove(nums[i-k])
        return False

