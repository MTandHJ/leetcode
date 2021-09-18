

from typing import List

class Solution:
    def printNumbers(self, n:int) -> List[int]:
        def dfs(x:int):
            if x == n:
                res.append(''.join(num))
                return 
            for i in range(10):
                num[x] = str(i)
                dfs(x+1)
        
        num = ['0'] * n
        res = []
        dfs(0)
        return ''.join(res)

class Solution:
    def printNumbers(self, n:int) -> List[int]:
        def dfs(index, num, digit):
            if index == digit:
                # 当前第几位 VS 真实的位数
                # 比如当前index： 1， 真实digit： 2
                res.append(int(''.join(num)))
                return
            for i in range(10):
                # 从第二位数开始，依次往下递增
                num.append(str(i))
                dfs(index+1, num, digit)
                # 一次递归完成之后，返回
                # 将上一次最后一位给删除，比如91
                # 继续进行下一次，比如92, 直到当前for i in range(10)循环结束
                num.pop()
        
        res = []
        # digit代表是当前的第几位
        for digit in range(1, n+1):
            for first in range(1, 10):
                # 第一位数
                num = [str(first)]
                dfs(1, num, digit)

        return res
    

if __name__ == '__main__':
    ins = Solution()
    n = 2

    print(ins.printNumbers(2))