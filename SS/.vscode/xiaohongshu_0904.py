import sys
import numpy as np

def findMax(N, mat):
    max_ = max(mat)
    for i in range(N*N):
        max_ = max(max_, subMax(mat, i, N))
    return max_

def subMax(mat, k, N):
    arr = np.array(mat).reshape(N, N)
    i = k // N
    j = k % N
    cur = arr[k]
    left_up = cur
    right_up = cur
    left_down = cur
    right_down = cur
    
    left_up = max(arr[:i+1][:j+1])
    right_up = max(arr[:i+1][j:])
    left_down = max(arr[i:][:j])
    right_down = max(arr[i:][j:])
    return max(cur, left_up, left_down, right_up, right_down)

N = 3
mat = "1 2 -3 3 4 -5 -5 -6 -7"
mat = [int(i) for i in mat.split(' ')]
print(findMax(N, mat))

    
# while 1:
#     N = int(input().strip())
#     mat = [int(line) for line in sys.stdin.readline().split(' ')]
#     print(findMax(N, mat))

import sys
import numpy as np 


while 1:
	N, K = [int(i) for i in input().split(' ')]
	mat = [int(i) for i in input().split(' ')]
    arr = np.array(mat).reshape(N-1, 3)
    for i in range(N-1):
    	for j in range(2):
        	if arr[i, j] + arr[i+1, j] < K:
                cnt += 1
            if arr[i, j] + arr[i, j+1] < K:
                cnt += 1
    print(cnt)