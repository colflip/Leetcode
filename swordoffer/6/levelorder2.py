# 剑指 Offer 32 - II. 从上到下打印二叉树 II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, q, this_row = [[root.val]], [root], []
        while q:
            while q:
                cur = q.pop(0)
                if cur.left:
                    this_row.append(cur.left)
                if cur.right:
                    this_row.append(cur.right)
            if not this_row:
                return res
            q += this_row
            res.append([e.val for e in this_row])
            this_row = []
        return res