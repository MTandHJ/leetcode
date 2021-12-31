

from typing import List

from base import version

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    @version("28ms, 15mb")
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def search(node):
            if node is None:
                return []
            ans = []
            head = str(node.val)
            for left in search(node.left):
                ans.append('->'.join((head, str(left))))
            for right in search(node.right):
                ans.append('->'.join((head, str(right))))
            if ans:
                return ans
            else:
                return [head]
        return search(root)