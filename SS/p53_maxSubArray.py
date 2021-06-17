from typing import List, get_origin

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, maxAns = 0, nums[0]
        for x in nums:
            pre = max(pre + x, x)
            maxAns = max(maxAns, pre)

        return maxAns


class Solution:
    class Status:
        def __init__(self, lSum:int, rSum:int, mSum:int, iSum:int) -> None:
            self.lSum = lSum
            self.rSum = rSum
            self.mSum = mSum
            self.iSum = iSum
        
    def push_up(self, l:Status, r:Status):
        # print('l: {}, r: {}'.format(l, r))
        iSum = l.iSum + r.iSum
        lSum = max(l.lSum, l.iSum+r.lSum)
        rSum = max(r.rSum, r.iSum+l.rSum)
        mSum = max(max(l.mSum, r.mSum), l.rSum+r.lSum)
        return self.Status(lSum, rSum, mSum, iSum)

    def get_info(self, a: List[int], l:int, r:int) -> int:
        print('l: {}, r: {}'.format(l, r))
    
        if l == r:
            return self.Status(a[l], a[l], a[l], a[l])
        m = (l + r) // 2
        lSub = self.get_info(a, l, m)
        print('lSub.mSum ', lSub.mSum)
        rSub = self.get_info(a, m+1, r)
        print('rSub.mSum {}'.format(rSub.mSum))
        return self.push_up(lSub, rSub)

    def maxSubArray(self, nums: List[int]) -> int:
        return self.get_info(nums, 0, len(nums)-1).mSum
    
        # iSum = sum(a[l:r+1])
        # lSum = max(sum[l:m+1], iSum)
        # rSum = max(sum[m+1, r], iSum)
        # mSum = max(lSum, rSum, iSum)
        # return self.push_up(lSub, rSub)

if __name__ == '__main__':
    ins = Solution()
    ans = ins.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    # ans = ins.maxSubArray([-2,1,-3,4])
    # ans = ins.maxSubArray([-2,1])
    # ans = ins.maxSubArray([-2, 1, 2])
    print(ans)
    
    