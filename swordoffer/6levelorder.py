# 32 - I. 从上到下打印二叉树
# 层序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#

class Solution:
    def levelOrder(self, root):
        temp = [root]
        ans = []
        while len(temp) > 0:
            if temp[0] is not None:
                ans.append(temp[0].val)
                temp.append(temp[0].left)
                temp.append(temp[0].right)

            temp.pop(0)
        return ans


