class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val
    
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.path = 0
        
        def dfs(root: TreeNode) -> int:
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            if root.left and root.left.val == root.val:
                leftPath = left + 1
            else:
                leftPath = 0
            if root.right and root.right.val == root.val:
                rightPath = right + 1
            else:
                rightPath = 0
            path = max(self.path, leftPath + rightPath)
            return max(leftPath, rightPath)

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.path = 0

        def dfs(root: TreeNode) -> int:
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            # NOTE: 可以不包含根节点
            # 当左节点的值,等于根节点的值
            # 左边不存在就说明leftPath=0
            # 右边同理
            if root.left and root.left.val == root.val:
                leftPath = left + 1
            else:
                leftPath = 0
            if root.right and root.right.val == root.val:
                rightPath = right + 1
            else:
                rightPath = 0
            # 这里是边的长度,所以最长路径等于左边可能相同值边的长度之和
            self.path = max(self.path, leftPath + rightPath)
            # 找到左边或者右边, 边的长度
            return max(leftPath, rightPath)
        dfs(root)
        return self.path