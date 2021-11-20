


from typing import List
from base import version

class Solution:
   
    @version("1 hour to solve it")
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        node1, node2 = 0, 0
        nums1[m:] = [10 ** 9] * n
        while node2 < n:
            if nums1[node1] > nums2[node2]:
                nums1[node1+1:] = nums1[node1:-1]
                nums1[node1] = nums2[node2]
                node2 += 1
            node1 += 1
  
    @version("insert")
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        node1, node2 = 0, 0
        nums1[m:] = [10 ** 9] * n
        while node2 < n:
            if nums1[node1] > nums2[node2]:
                nums1.insert(node1, nums2[node2])
                node2 += 1
            node1 += 1
        nums1[:] = nums1[:m + n]

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        node1, node2 = m - 1, n - 1
        while node1 >= 0 and node2 >= 0:
            if nums1[node1] > nums2[node2]:
                nums1[node1 + node2 + 1] = nums1[node1]
                node1 -= 1
            else:
                nums1[node1 + node2 + 1] = nums2[node2]
                node2 -= 1



x = [1, 2, 3]
x.insert(1, 5)
print(x)

