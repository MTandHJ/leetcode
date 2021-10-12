class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        isLeafNode = lambda root: not root.left and not root.right

        def dfs(root: TreeNode) -> int:
            res = 0
            if root.left:
                if isLeafNode(root.left):
                    res += root.left.val
                else:
                    res += dfs(root.left)
            if root.right and not isLeafNode(root.right):
                res += dfs(root.right)
            return res
        
        return dfs(root) if root else 0

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def isLeaf(root):
            if not root:
                return False
            if not root.left and not root.right:
                return True
            return False
        
        if not root:
            return 0
        if isLeaf(root.left):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)



class Solution:
    def sumOfLeftLeaves(self, root):
        isLeafNode = lambda root: not root.left and not root.right and root

        def dfs(root):
            res = 0
            if root.left:
                if isLeafNode(root.left):
                    res += root.left.val
                else:
                    res += dfs(root.left)
            # 不仅要找左子树的左叶子节点，还需要找右子树的左叶子节点
            if root.right and not isLeafNode(root.right):
                res += dfs(root.right)
            return res
        
        return dfs(root) if root else 0
    
    def sumOfLeftLeaves(self, root):
        isLeafNode = lambda root: root and not root.left and not root.right

        if not root:
            return 0
        # 对每一个遍历的根。
        # 都需要先对这个根的左节点遍历
        # 再加上对右节点的和
        if isLeafNode(root.left):
            return root.left.val \
                + self.sumOfLeftLeaves(root.right)
        
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
    
    # 迭代的做法
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        res = 0
        while root:
            print(root.val)
            if self.isLeaf(root):
                # res += root.val
                return res
            if self.isLeaf(root.left):
                res += root.left.val
                root = root.right
            else:
                root = root.left
            # print(res)
        return res
        
    def isLeaf(self, root):
        return root and not root.left and not root.right
