

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        que = [root]
        while que:
            size = len(que)
            for i in range(size):
                node = que.pop(0)
                if i < size - 1:
                    node.next = que[0]
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return root