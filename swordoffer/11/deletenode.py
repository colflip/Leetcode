# 剑指 Offer 18. 删除链表的节点


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        temp = head
        if temp.val == val:
            return temp.next
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head


headlist = [4, 5, 1, 9]
temp = ListNode(headlist[0])
head = temp
print(" head:", head.val, end="")
for i in headlist[1:]:
    i = ListNode(i)
    temp.next = i
    temp = temp.next
    print("-", temp.val, end="")
val = 5
new_head = Solution().deleteNode(head, val)
print("\n", "new_head:", new_head.val, end="")
while new_head.next is not None:
    new_head = new_head.next
    print("-", new_head.val, end="")
