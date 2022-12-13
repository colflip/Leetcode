# 剑指 Offer 37. 序列化二叉树
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        r = []
        if root:
            stack = [root]
            count = 1
            stack = collections.deque(stack)
            while count != 0:
                parent = stack.popleft()
                if parent != None:
                    count -= 1
                    r.append(parent.val)
                    if parent.left != None:
                        count += 1
                    if parent.right != None:
                        count += 1
                    stack.append(parent.left)
                    stack.append(parent.right)
                else:
                    r.append(None)
        return r

    def deserialize(self, data):
        if data:
            data = collections.deque(data)
            root = TreeNode(data[0])
            data.popleft()
            waitlist = [root]
            waitlist = collections.deque(waitlist)
            while data:
                parent = waitlist.popleft()
                if data:
                    leftchild = data.popleft()
                else:
                    leftchild = None
                if data:
                    rightchild = data.popleft()
                else:
                    rightchild = None
                if leftchild != None:
                    leftnode = TreeNode(leftchild)
                    parent.left = leftnode
                    waitlist.append(leftnode)
                if rightchild != None:
                    rightnode = TreeNode(rightchild)
                    parent.right = rightnode
                    waitlist.append(rightnode)
            return root
        else:
            return None
