

nums = [4, 2, 2, 3, 3, 1]
nums.sort()

# 存放nums中不重复的元素
temp = set()
res = [] # 存放出现两次的元素

for x in nums:
    if x not in temp:
        temp.add(x)
    else:
        # 如果不存在res中，则x只出现了一次
        # 如果之前已经添加过x到res中去了，就需要
        if x not in res:
            res.append(x)

res = [str(x) for x in res]
print(' '.join(res))

#%%
