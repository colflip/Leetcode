# 剑指 Offer 55 - II. 平衡二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.treeHeight(root) >= 0

    def treeHeight(self, root):
        if not root:
            return 0
        leftHeight = self.treeHeight(root.left)
        rightHeight = self.treeHeight(root.right)
        if leftHeight >= 0 and rightHeight >= 0 and abs(leftHeight - rightHeight) <= 1:
            return max(leftHeight, rightHeight) + 1
        else:
            return -1
