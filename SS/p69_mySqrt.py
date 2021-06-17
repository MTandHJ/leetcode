class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left, right = 0, x
        while left < right:
            print(left, right)
            mid = (left + right) // 2
            print(mid)
            if mid ** 2 == x:
                return mid
            elif left ** 2 <= x and mid ** 2 > x:
                if mid - left == 1: return left
                right = mid
            elif mid ** 2 < x and x <= right ** 2:
                if right - mid == 1: return mid
                left = mid
        
        # return left

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        C, x0 = float(x), float(x)
        while 1:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)
if __name__ == "__main__":
    ins = Solution()
    nums = 3
    # target = 7
    print('final: ', ins.mySqrt(nums))