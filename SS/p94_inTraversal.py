
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val 
        self.left = left
        self.right = right
    
class Solution:
    def inTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        stack = [(WHITE, root)]
        res = []
        while stack:
            color, node = stack.pop()
            if not node: continue
            if color == WHITE:
                stack.append((WHITE, root.left))
                stack.append((GRAY, node))
                stack.append((WHITE, root.right))
            else:
                res.append(node.val)
        
        return res

class Solution:
    def inTraversal(self, root: TreeNode) -> List[int]:
        res = []
        cur = root
        stack = [root]
        while cur and stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right

        return res

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> st;
        TreeNode* cur = root;
        while (cur != NULL || !st.empty()) {
            if (cur != NULL) { // 指针来访问节点，访问到最底层
                st.push(cur); // 将访问的节点放进栈
                cur = cur->left;                // 左
            } else {
                cur = st.top(); // 从栈里弹出的数据，就是要处理的数据（放进result数组里的数据）
                st.pop();
                result.push_back(cur->val);     // 中
                cur = cur->right;               // 右
            }
        }
        return result;
    }
};

作者：carlsun-2
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/dai-ma-sui-xiang-lu-che-di-chi-tou-qian-xjof1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。