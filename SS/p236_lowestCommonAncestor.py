class TreeNode:
    def __init__(self, left=None, right=None, val=0) -> None:
        self.left = left
        self.right = right
        self.val = val


class Solution:
    def dfs(self, root, p, q):
        if not root:
            return False
        lson = self.dfs(root.left, p, q)
        rson = self.dfs(root.right, p, q)
        if lson and rson \
            or (root.val == p.val or root.val == q.val) \
                and lson or rson:
                self.ans = root
        return lson or rson or root.val == p.val or root.val == q.val
    
    def lowestCommonAncestor(self, root, p, q):
        self.ans = None
        self.dfs(root, p, q)
        return self.ans
        