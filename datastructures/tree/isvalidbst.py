# 98. 验证二叉搜索树
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, lower, upper):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)

        return helper(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(Solution().isValidBST(root))
