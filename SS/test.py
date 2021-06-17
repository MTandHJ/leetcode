## --- 可获得的最大的金币价值
while 1:
    N = int(input())
    coins = list(map(int, input().split()))
    # A, B, C, D, N = 4 *n
    # 要找出n轮中金币的
    # (a) 首先B小朋友从金币池子中找到4枚金币
    # (b) 再A, B, C, D依次抽取一枚硬币，A找到最大的金币
    # 最后每个小朋友都有n枚硬币，请问小朋友能拥有的最高金币价值是多少。

    n = int(N / 4)
    tmp = sorted(coins, reverse=True)
    print(sum(tmp[1:2*n:2]))

## ---- 数组和最大
# 给定一个正整数数组，从数组中选择一批非相邻的数字，求这些数字和最大的值
while 1:
    nums = list(map(int, input().split(",")))
    n1 = nums[::2]
    n2 = nums[1::2]
    print(sum(n1) if sum(n1) > sum(n2) else sum(n2))
    
