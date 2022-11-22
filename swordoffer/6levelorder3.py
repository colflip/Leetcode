# 32 - III. 从上到下打印二叉树 III
import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, deque = [], collections.deque([root])
        while deque:
            temp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2:
                    temp.appendleft(node.val)
                else:
                    temp.append(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(temp))
        return res
