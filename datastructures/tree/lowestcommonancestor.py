# 235. 二叉搜索树的最近公共祖先

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        while root:
            if root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
            else:
                return root


if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    print(Solution().lowestCommonAncestor(root, root.left, root.left.right.right).val)
