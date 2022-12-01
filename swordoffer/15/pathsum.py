# 剑指 Offer 34. 二叉树中和为某一值的路径

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int):
        if not root: return []
        stack = [(root, [root.val])]
        res = []
        while stack:
            node, val = stack.pop()
            if node and not node.left and not node.right and sum(val) == target:
                res.append(val)
            if node.left:
                stack.append((node.left, val + [node.left.val]))
            if node.right:
                stack.append((node.right, val + [node.right.val]))
        return res


root = [5, 4, 8, 11, -1, 13, 4, 7, 2, -1, -1, 5, 1]
targetSum = 22

temp_node = head_node = left_node = TreeNode(root[0])
temp_node.left = None
for i in root[1:]:
    node = left_node = TreeNode(i)
    temp_node.left = left_node
    temp_node.right = node
    temp_node = temp_node.right
print(Solution().pathSum(head_node, targetSum))
