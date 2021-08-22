## Easy ###

# record: June 22, 2021. 10:43

from typing import Collection, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root:TreeNode) -> List[int]:
        # 返回的结果
        res = list()
        # 如果当前结点非空
        if not root:
            return res
        
        # [1, 2, null, 4, 3, 5, 6]

        stack = list()
        node = root
        while stack and root:
            # while stack保证栈里面有元素
            # root 保证是某个取值不为空的结点
            
            while node:
                # 此时Node应当是根节点
                res.append(node.val)
                stack.append(node)
                # 体现出先序遍历的特点
                node = node.left
            
            node = stack.pop()
            node = node.right

        return res

class Solution:
    def preorderTraversal(self, root) -> List[int]:
        res = []
        if not root:
            return res
        
        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            node = node.right
        
        return res


class Solution:
    def preorderTraversal(self, root:TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        
        p1 = root
        while p1:
            p2 = p1.left
            if p2:
                while p2.right and p2.right != p1:
                    p2 = p2.right
                if not p2.right:
                    res.append(p1.val)
                    p2.right = p1
                    p1 = p1.left
                    continue
                else:
                    p2.right = None
            else:
                res.append(p1.val)
            p1 = p1.right

        return res


class Solution:
    def preorderTraversal(self, root:TreeNode) -> List[int]:
        def preorder(root: TreeNode) -> List[int]:
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        res = list()
        preorder(root)
        return res


# from collections import deque
class Solution:
    def preorderTraversal(self, root:TreeNode) -> List[int]:
        if not root:
            return
        
        res = []
        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

        return res


if __name__ == "__main__":
    ins = Solution()
    
