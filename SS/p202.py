"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true ；不是，则返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        # 先求出一个数的个十百千
        LIMIT = 1000
        nums = list(map(int, list(str(n))))

        cnt = 0
        # res = n
        res = self.square_sum(nums)
        while cnt < LIMIT:
            if res == 1:
                return True
            else:
                nums = list(map(int, list(str(res))))
                res = self.square_sum(nums)
            cnt += 1
        return False

    def square_sum(self, nums:List[int]) -> int:
        def my_pow(x):
            return x ** 2
        return sum(list(map(my_pow, nums)))


# hash表方法
class Solution:
    def isHappy(self, n: int) -> bool:
        # 创建一个初始hash映射来存储k-v映射
        res_sum = set()
        # 定义一个函数来获取一轮平方和之后的数据
        def getNext(n: int) -> int:
            res_sum = 0
            # 当至少二位数时
            while n > 0:
                n, digit = divmod(n, 10)
                res_sum += digit ** 2
            return res_sum

        # 更新数据，进行判断
        # 当这个书在res_sum中出现过，且不是1，则说明已经进入循环
        # 且循环是跳不出来的
        while n != 1:
            n = getNext(n)
            if n in res_sum:
                return False
            res_sum.add(n)
        return True


# for test
if __name__ == "__main__":
    ins = Solution()
    n = 19
    print(ins.isHappy(n))
