#### 杨辉三角 Ⅱ #####

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        C = [[] for _ in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            if i == 0:
                C[i] = [1]
            else:
                C[i] = [1] + [0 for _ in range(i)]
            for j in range(1, i+1):
                if j == i:
                    C[i][j] = 1
                else:
                    C[i][j] = C[i-1][j-1] + C[i-1][j]
            
        return C[rowIndex]


### 比较好的初始化数组的方法
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        C = [[] for _ in range(rowIndex + 1)]

        for i in range(rowIndex + 1):
            C[i] = [0 for _ in range(i+1)]
            # New： 优秀点在这里
            C[i][0] = C[i][i] = 1
            print(C[i])
            for j in range(1, i):
                C[i][j] = C[i-1][j-1] + C[i-1][j]
            
        return C[rowIndex]

### 优化： ####
# 思想：记录前一个和需要更新的数组
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = []
        for i in range(rowIndex + 1):
            cur = [0 for _ in range(i+1)]
            cur[0] = cur[i] = 1
            for j in range(1, i+1):
                cur[j] = pre[j-1] + pre[j]
            pre = cur
        
        return pre

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = []
        for i in range(rowIndex + 1):
            cur = []
            for j in range(i+1):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    cur.append(pre[j-1] + pre[j])
            pre = cur
            
        return pre
if __name__ == "__main__":
    ins = Solution()
    rowIndex = 3
    print(ins.getRow(rowIndex))