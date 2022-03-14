

from typing import Optional, List

import collections

from base import version

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def findMode(self, root: TreeNode) -> List[int]:
        memory = collections.defaultdict(int)
        def dfs(root):
            if root is None: return
            memory[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        counts = 0
        label = set()
        for key, val in memory.items():
            if val > counts:
                counts = val
                label = {key}
            if val == counts:
                label.add(key)
        return list(label)
