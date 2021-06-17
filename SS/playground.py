# 2021.5.10美团笔试
# -------------网格
# 递归，找最小的
def get_next(nums, cur):
    pos_next = []
    for i in range(len(nums)):
        if nums[i][0] == cur[0] and nums[i][1] == cur[1]:
            pos_next.append((nums[i][2:4], nums[i][-1]))
    return pos_next

# 想用递归来计算得分
def get_cost(nums, cur, cur_cost, target):
    if cur == target:
        return cur_cost
    if not get_next(nums, cur):
        return -1
    else:
        pass
    
    

while 1:
    n, m, k = list(map(int, input().split()))
    num5 = []
    for _ in range(k):
        # xi, yi, ui, vi, wi = 
        num5.append(list(map(int, input().split())))
    
    cost = 0
    first_next = get_next(num5, [1, 1])
    
    for pos, c in first_next:
        cur_next = get_next(num5, pos)


# -----------------围栏----------------------------
# 数组
def is_lt(li, h):
    for i in li:
        if i > h:
            return False
    return True

def is_continue(li, m, h):
    if len(li) < m:
        return False
    for i in range(len(li)-m):
        if is_lt(li[i:i+m], h):
            return i + 1
    return -1


while 1:
    n, m, h = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    print(is_continue(heights, m, h))


# -------------------小美练吉他--------------------------
def rest(revenue, x, b):
    return revenue, x + b
def work(revenue, x, a):
    if x < a:
        x -= x
    else:
        x -= a
    return revenue + x, x

# 不太懂最大路径和最小路径，先暂时写下一个思路，回去再继续学习
# （1） 首先创建根节点，其值为初始状态值和初始收益值
# (2) 左节点：休息，右节点：练习
# (3) 生成树之后，使用中序遍历
# （4） 中序遍历的时候，到达另外的叶子结点，直到所有的叶子结点都遍历完。
# 分别记录所有叶子结点的收益值，返回最大的。
def max_reve(t, x, a, b, n):
    # 最大路径
    # 暴力穷举法
    # 好像也是二叉树
    reves = []
    for i in range(t):
        revenue, x = rest(0, x, b)

while 1:
    t = int(input().strip())
    x, a, b, n = list(map(int, input().split()))


# -----------------4、机器人
while 1:
    n, m = list(map(int, input().split()))
    wg = []
    for _ in range(n):
        line = list(input().strip())
        wg.append(line)
    

def aggregateByKey_hashmap(keys):
    hashmap = {}
    for key in keys:
        if key in hashmap:
            if hashmap.get(key) satisfy the requirement:
                return need_infomation
        hashmap[key] = value
    return need_information