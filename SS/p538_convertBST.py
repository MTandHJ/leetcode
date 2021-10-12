

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # 累计和
        self.cusum = 0
        # 二叉搜索树，右 -> 根 -> 左
        def bst(root: TreeNode) -> TreeNode:
            if not root:
                return
            # 先右
            bst(root.right)
            # 对根节点作处理
            root.val += self.cusum
            self.cusum = root.val
            # 最后左
            bst(root.left)
        
        bst(root)
        return root

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        preSum = 0

        stack = []
        stack.append(root)
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            node.val += preSum
            preSum = node.val
            if node.left:
                node = node.left
            else:
                node = None
        return root


