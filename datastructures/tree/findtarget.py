# 653. 两数之和 IV - 输入二叉搜索树
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def helper(root, k, visited):
            if not root:
                return False
            if k - root.val in visited:
                return True
            visited.add(root.val)
            return helper(root.left, k, visited) or helper(root.right, k, visited)

        return helper(root, k, set())


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    print(Solution().findTarget(root, 9))
    print(Solution().findTarget(root, 28))
