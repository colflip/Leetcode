# 27. 二叉树的镜像

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root):
        if not root:
            return None
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root
