

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 说明root在p, q的右边
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # 说明root在p, q的左边，需要去遍历root的右边去寻找他们两的公共祖先
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right)
        return root