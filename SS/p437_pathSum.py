

class TreeNode:
    def __init__(self, left=None, right=None, val=0) -> None:
        self.left = left
        self.right = right
        self.val = val
    
class Solution:
    def pathSum(self, root: TreeNode, _sum):
        if not root:
            return 0
        res = self.pathSumStartWithRoot(root, _sum) \
            + self.pathSum(root.left, _sum - root.val) \
                + self.pathSum(root.right, _sum - root.val)
        return res
    
    def pathSumStartWithRoot(self, root: TreeNode, _sum: int) -> int:
        if not root:
            return 0
        res = 0
        if root.val == _sum:
            res += 1
        res += self.pathSumStartWithRoot(root.left, _sum - root.val) \
            + self.pathSumStartWithRoot(root.right, _sum - root.val)
        return res