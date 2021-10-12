class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        # 先判断两个房子是否相邻（不是同一个父节点）
        # 找不相邻房子的最大和
        cache = dict()
        if not root:
            return 0
        if root in cache:
            return cache[root]
        
        val1 = root.val
        # 相当于是１，３层
        if root.left:
            val1 += self.rob(root.left.left) \
                + self.rob(root.left.right)
        if root.right:
            val1 += self.rob(root.right.left) \
                + self.rob(root.right.right)
        # 相当于是1，2，3层中的2层
        val2 = self.rob(root.left) + self.rob(root.right)
        res = max(val1, val2)
        # 将这个添加进去
        cache[root] = res
        return res