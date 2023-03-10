# 94. 二叉树的中序遍历
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().inorderTraversal(root))
