import sys
# 1. 开锁
def func(n, m, mat):
    if n == 1:
        return sum(mat[0])
    # 最优策略下，打开所有锁的期望时间
    # 对第j把锁
    expect = 0
    for j in range(m):
        temp = [mat[i][j] for i in range(n)]
        temp.sort()
        temp_sum = [sum(temp[:i+1])  for i in range(n)]
        expect += sum(temp_sum) / n
    return expect

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    n, m = [int(item) for item in line.split()]
    mat = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        mat.append(list(map(int, line.split())))
    print(func(n, m, mat))


# 2. 勇闯币圈
def func(n, speed):
    if n == 1:
        return n
    speed.sort()
    # 代表以这个车队开头的，车队人数
    
    dp = [[0] * n for _ in range(n)]
    max_len = 1
    for i in range(n):
        for j in range(i+1, n):
            if speed[j] - speed[i] <= 10:
                speed[i][j] = j - i + 1
            else:
                dp[i][j] = max(dp[i][i:j+1])
            max_len = max_len if max_len > dp[i][j] else dp[i][j]
    return max_len
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    print(func(n, values))

def func(t, pi, mat):
    if pi[2] > 0.5:
        return 1
    
    for _ in range(t):
        p1 = sum([mat[0][j] * pi[j] for j in range(3)])
        p2 = sum([mat[1][j] * pi[j] for j in range(3)])
        p3 = sum([mat[2][j] * pi[j] for j in range(3)])
        if pi_new[2] > 0.5:
            return 1
        pi_new = [p1, p2, p3]
        pi = pi_new
    
    return 0
    
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        t = int(sys.stdin.readline().strip())
        pi = sys.stdin.readline().strip()
        #print(pi)
        pi = [float(i) for i in pi.split()]

        mat = []
        for j in range(3):
            line = sys.stdin.readline().strip()
            line = [float(i) for i in line.split()]
            mat.append(line)
        print(func(t, pi, mat))

# 3. 迎宾车队
# 最长车队人数
def func(n, speed):
    if n == 1:
        return n
    speed.sort()
    # 代表以这个车队开头的，车队人数
    
    dp = [1] * n
    for i in range(n):
        if speed[-1] - speed[i] <= 10:
            dp[i] = n - i
            continue
        
        for j in range(i+1, n):
            if speed[j] - speed[i] <= 10:
                dp[i] += 1
    return max(dp)
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    print(func(n, values))

# 水站的水流量
# 水站网络有n层，第i层有i个水站节点，水流单向流动
# 2 2
# 1
import sys
def func(n, t):
    if t == 0:
        return 0

import sys
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    n, t = [int(item) for item in line.split()]
    print(n, t)


# 5. 定点轰炸
# 在不经过1的前提下到达区域外的0点，则
'''
3
0 0 0
0 0 1
0 1 1

'''