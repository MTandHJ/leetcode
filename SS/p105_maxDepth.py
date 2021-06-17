
class TreeNode:
    def __init__(self, left=None, right=None, val=0) -> None:
        self.left = left
        self.right = right
        self.val = val

class Solution:
    def maxDepth(self, root:TreeNode) -> bool:
        # 边界条件
        if not root:
            return 0
        # 计算左边节点的高度，第一层递归
        left_depth = self.maxDepth(root.left)
        # 计算右边结点的高度，第二层递归
        right_depth = self.maxDepth(root.right)
        # 上面外层的递归完成之后才会计算这一步
        return max(left_depth, right_depth) + 1