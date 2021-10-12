


from typing import List


class TreeNode():
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val 
        self.left = left 
        self.right = right


class Solution:
    def flatten(self, root: TreeNode):
        preorderList = list()
        def preorder(root):
            if root:
                preorderList.append(root.val)
                preorder(root.left)
                preorder(root.right)
        
        preorder(root)
        size = len(preorderList)
        for i in range(1, size):
            pre, cur = preorderList[i-1], preorderList[i]
            pre.left = None
            pre.right = TreeNode(cur)
    
    def flatten2(self, root):
        res = []
        stack = list()
        node = root
        
        while node or stack:
            while node:
                res.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
    
        size = len(res)
        for i in range(1, size):
            pre, cur = res[i-1], res[i]
            pre.left = None
            pre.right = TreeNode(cur)


    