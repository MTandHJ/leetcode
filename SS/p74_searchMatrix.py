from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            if matrix[i][0] <= target and target <= matrix[i][m-1]:
                print(i)
                if self.binary_search(matrix[i], target):
                    return True
        return False
    
    def binary_search(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            print(l, r)
            mid = (l + r) // 2
            print('mid: ', mid)
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                # [left, right)
                r = mid
        return False

    def searchMatrix_off1(self, matrix: List[List[int]], target: int) -> bool:
        row_idx = self.binary_search_first_column(matrix, target)
        if row_idx < 0:
            return False
        return self.binary_search_row(matrix[row_idx], target)

    # 选择是哪一行
    def binary_search_first_column(self, matrix: List[List[int]], target: int) -> bool:
        # l, r = 0, len(matrix) - 1
        low, high = -1, len(matrix) - 1
        while low < high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target:
                low = mid
            else:
                high = mid - 1
        return low
    
    # 选择哪一行中，具体的某个列
    def binary_search_row(self, row: List[int], target: int):
        low, high = 0, len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                high = mid - 1
            elif row[mid] < target:
                low = mid
        return False

    def searchMatrix_off2(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m*n - 1
        while low < high:
            mid = (low + high) // 2
            x = matrix[mid//n][mid%n]
            if x < target:
                low = mid
            elif x > target:
                high = mid - 1
            elif x == target:
                return True
        
        return False
            
            

