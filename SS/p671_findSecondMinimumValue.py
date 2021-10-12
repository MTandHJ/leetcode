
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # 根节点都为空，说明没有
        if not root:
            return -1
        # 左节点和右节点都为空，说明没有
        if not root.left and not root.right:
            return -1
        # 要是其中两者都不为空
        leftVal = root.left.val
        rightVal = root.right.val
        # 说明最小的是left，继续从其自己欸子节点
        if leftVal == root.val:
            leftVal = self.findSecondMinimumValue(root.left)
        if rightVal == root.val:
            rightVal = self.findSecondMinimumValue(root.right)
        if leftVal != -1 and rightVal != -1:
            return min(leftVal, rightVal)
        if leftVal != -1:
            return leftVal
        return rightVal