import collections
from typing import Collection, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        
        return self.hasPathSum(root.left, targetSum-root.val) \
            or self.hasPathSum(root.right, targetSum-root.val)
        
class Solution:
    def hasPathSum0(self, root, targetSum) -> bool:
        if not root:
            return False
        # 到最后叶子节点，sum值应该跟targetSum一致
        if not root.left and not root.right:
            return targetSum == root.val
        
        return self.hasPathSum0(root.left, targetSum - root.val) \
            or self.hasPathSum0(root.right, targetSum - root.val)
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        que_node = collections.deque()
        que_val = collections.deque()

        while que_node:
            node = que_node.popleft()
            val = que_val.popleft()
            if not node.left and not node.right:
                if val == targetSum:
                    return True
                continue
            # 注意下面一定要加上一个当前层的val
            if node.left:
                que_node.append(node.left)
                que_val.append(node.left.val + val)
            if node.right:
                que_node.append(node.right)
                que_val.append(node.right.val + val)
        return False

    # dfs(递归)
    def hasPathSum2(self, root: TreeNode, targetSum: int) -> bool:
        
        def dfs(root: TreeNode, target: int, path) -> bool:
            if not root:
                return False
            if sum(path) == target and not root.left and not root.right:
                return True 
            left_flag, right_flag = False, False
            if root.left:
                left_flag = dfs(root.left, target, path + [root.left.val])
            if root.right:
                right_flag = dfs(root.right, target, path + [root.right.val])
            return left_flag or right_flag
        
        if not root:
            return False
        dfs(root, targetSum, [root.val])
    
    # BFS
    def hasPathSum3(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        que = collections.deque()
        que.append((root, [root.val]))
        while que:
            cur_node, cur_path = que.popleft()
            if not cur_node.left and cur_node.right and sum(cur_path) == targetSum:
                return True
            if cur_node.left:
                que.append((cur_node.left, cur_path + [cur_node.left.val]))
            if cur_node.right:
                que.append((cur_node.right, cur_path + [cur_node.right.val]))
        return False
    
    # stack
    def hasPathSum4(self, root, targetSum) -> bool:
        if not root:
            return False
        
        stack = []
        stack.append((root, root.val))
        while stack:
            node, pathSum = stack.pop()
            if not node.left and not node.right and pathSum == targetSum:
                return True 
            if node.left:
                stack.append((node.left, pathSum + node.left.val))
            if node.right:
                stack.append((node.right, pathSum + node.right.val))
        return False
            
            