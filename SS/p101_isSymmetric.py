# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 边界条件
        if not root:
            return True
        # 一定要是两个结点，以判断对称点是否相等
        return self.check(root.left, root.right)

    def check(self, left:TreeNode, right:TreeNode) -> bool:
        # 当都是空的时候，说明当前两个结点没有子节点
        # 空的对称性也满足
        # （a）判断空的条件
        if not left and not right:
            return True
        # 除去上面一种情况，就是一个有但是另外一个没有
        if not left or not right:
            return False
        # （b）最后非空的时候，再进行判断
        return left.val == right.val \
            and self.check(left.left, left.right) \
                and self.check(left.right, right.left)

# 迭代
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 边界条件
        if not root:
            return True
        return self.check(root.left, root.right)
    
    def check(self, left:TreeNode, right:TreeNode) -> bool:
        # (a) 初始化队列
        queue = []
        queue.append(left)
        queue.append(right)

        # (b) 对队列中所有元素一一判断
        while queue:
            # (b1) 出队列
            left = queue.pop(0)
            right = queue.pop(0)
            # 对上一步出队列的元素进行判断
            
            # (b2)
            # 不判断为错误，但是可能下面还有要检查的元素
            # 所以continue
            if not left and not right:
                continue
            # 以下两个条件均是可以得出判断结果的条件
            if not left or not right:
                return False
            if left.val != left.val:
                return False
            # (b3)
            # 开始往下一层迁移，判断
            # 注意这里的顺序：
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True