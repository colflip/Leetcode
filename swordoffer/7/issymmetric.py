# 剑指 Offer 28. 对称的二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val == b.val:
            return self.check(a.left, b.right) and self.check(a.right, b.left)
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            return self.check(root.left, root.right)
        return True