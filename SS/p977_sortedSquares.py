from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        neg = -1
        for i in range(n):
            if nums[i] < 0:
                neg = i
            else:
                break
        
        ans = []
        i, j = neg, neg + 1
        while i >= 0 or j < n:
            if i < 0:
                ans.append(nums[j] * nums[j])
                j += 1
            elif j == n:
                ans.append(nums[i] * nums[i])
                i -= 1
            elif nums[i] * nums[i] < nums[j]*nums[j]:
                ans.append(nums[i] * nums[i])
                i -= 1
            else:
                ans.append(nums[j]* nums[j])
                j += 1
            
        return ans

if __name__ == '__main__':
    ins = Solution()
    nums = [-4,-1,0,3,10]
    print(ins.sortedSquares(nums))
