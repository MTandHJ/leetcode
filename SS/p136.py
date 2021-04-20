from typing import List


def singleNumber(nums: List[int]) -> int:
    # # 使用最蠢的办法：使用字典来创建对应
    # d_s = {k:0 for k in set(nums)}
    # for n in nums:
    #     d_s[n] += 1
    # print(d_s)
    # for k in d_s:
    #     if d_s[k] == 1:
    #         return k

    # 使用异或方法
    result = 0
    for num in nums:
        result ^= num
    return result


a = singleNumber([4,1,2,1,2])
print(a)