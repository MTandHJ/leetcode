

class Soution:
    def merge(self, nums1:List[int], m, int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1
        N = m + n - 1
        while i >= 0 and j >= 0:
            N -= 1
            if nums1[i] > nums2[j]:
                nums1[N] = nums1[i]
            else:
                nums1[N] = nums2[j]