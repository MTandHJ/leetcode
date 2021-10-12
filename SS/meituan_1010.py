def numOfSmallAction(stand, real, n, m, k):
    # 先找到最大的长度
    mmax = -1
    for i in range(n):
        mmax = max(mmax, stand[i][1])
    for j in range(m):
        mmax = max(mmax, real[j][1])

    temp0 = [-1] * (mmax + 1)
    temp1 = [-1] * (mmax + 1)
    for i in range(n):
        for i0 in range(stand[i][0], stand[i][1]):
            temp0[i0] = stand[i][2]
    for j in range(m):
        for j0 in range(real[j][0], real[j][1]):
            temp1[j0] = real[j][2]
    # dp = [-1] * (mmax + 1)

    res = 0
    # 再去找是否有连续值
    for i in range(mmax + 1):
        cur_score = addScore(i, temp0, temp1)
        if cur_score == 0:
            pass
        else:
            if i + 1 < mmax + 1 and addScore(i, temp0, temp1) == 1:
                continue
            else:
                res += 1
    return res
    

def addScore(i, temp0, temp1):
    cnt = 0
    if temp0[i] != -1:
        if temp1[i] == -1:
            cnt = 0
        else:
            if temp0[i] != temp1[i]:
                cnt += 1
    else:
        if temp1[i] != -1:
            cnt += 1
    return cnt
            

while 1:
    #print(len(list(map(int, input().split(' ')))))
    #break
    ss = list(map(int, input().strip().split()))
    cnt = 0
    for val in ss:
        if cnt == 0:
            n = val
        elif cnt == 1:
            m = val
        else: k = val
        cnt += 1
    standard = []
    real = []
    for i in range(n):
        standard.append(list(map(int, input().split(' '))))
    for j in range(m):
        real.append(list(map(int, input().split(' '))))
    print(numOfSmallAction(standard, real, n, m, k))