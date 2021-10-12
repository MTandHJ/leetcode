

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # 返回，说明就是空的，修剪之后也是空的
        if not root:
            return
        # root.left.val < root.val < root.right.val
        # root.val > high
        # 说明最后留下来的是root.left, 
        if root.val > high:
            return self.trimBST(root.left, low, high)
        if root.val < low:
            return self.trimBST(root.right, low, high)
        # 对于root.left, 其值一定小于root.val
        # 将root.val作为最大值，继续修剪
        root.left = self.trimBST(root.left, low, root.val)
        root.right = self.trimBST(root.right, root.val, high)
        return root