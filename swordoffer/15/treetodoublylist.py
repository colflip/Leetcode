# 剑指 Offer 36. 二叉搜索树与双向链表

# Definition for a Node.
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        l = self.treeToDoublyList(root.left)
        r = self.treeToDoublyList(root.right)
        root.left, root.right = root, root

        if l: root = self.concat(l, root)
        if r: root = self.concat(root, r)
        return root

    def concat(self, l, r):
        ll, lr, rl, rr = l, l.left, r, r.left
        ll.left, lr.right, rl.left, rr.right = rr, rl, lr, ll
        return l
