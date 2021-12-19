

import sys



class TreeNode():
    def __int__(self, val):
        self.val = val
        self.child = []
def func():
    res = 0
    mat.sort(key=lambda x:(x[0], x[1]))
    start = roomA
    
    temp = []
    
    d = {}
    for i in range(len(mat)):
        n0, n1 = mat[i]
        if n0 in d:
            temp[d[n0]][1].append(n1)
        else:
            temp.append([n0, [n1]])
            d[i] = mat[0]
    #print(temp)
    print(2)


if __name__ == '__main__':
    cnt = 0
    mat = []
    for val in sys.stdin.readlines():
        if cnt == 0:
            roomA = int(val)
        elif cnt == 1:
            roomB = int(val)
        elif cnt == 2:
            N = int(val)
        else:
            mat.append(list(map(int, val.strip().split())))
        cnt += 1
    

def func(sizes, starts, ends, N, lakes):
    dp = [[[0] * 2] * sizes[1] for _ in range(sizes[0])]
    mat = [[0] * sizes[1] for _ in range(sizes[0])]

    for i, j in lakes:
        mat[i][j] = 1
        dp[i][j] = float('inf')

    s_i, s_j = starts
    e_i, e_j = ends
    dp[s_i][s_j] = 0
    for i in range(s_i+1, e_i+1):
        for j in range(s_j+1, e_j+1):
            if mat[i][j] == 0:
                dp[i][j][0] = min(dp[i-1][j], dp[i][j-1]) + 1
                dp[i][j][1] += 1
    return dp[ends[0]][ends[1]]

if __name__ == '__main__':
    # i = 0
    lakes = []
    for i, val in sys.stdin.readlines():
        if i == 0:
            sizes = list(map(int, val.strip().split()))
        elif i == 1:
            starts = list(map(int, val.strip().split()))
        elif i == 2:
            ends = list(map(int, val.strip().split()))
        elif i == 3:
            N = int(val)
        elif i >= 4:
            lakes.append(list(map(int, val.strip().split())))
    
