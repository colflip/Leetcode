# 25. 合并两个排序的链表

# Definitionfor singly - linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        pre = None
        if l1.val < l2.val:
            pre = l1
            pre.next = self.mergeTwoLists(l1.next, l2)
        else:
            pre = l2
            pre.next = self.mergeTwoLists(l1, l2.next)
        return pre


listA = [1, 2, 4]
listB = [1, 3, 4]

temp = head = ListNode(listA[0])
print(" head:", temp.val, end="")
for i in listA[1:]:
    i = ListNode(i)
    temp.next = i
    temp = temp.next
    print("-", temp.val, end="")

temp2 = head2 = ListNode(listB[0])
print(" head2:", temp2.val, end="")
for i in listB[1:]:
    i = ListNode(i)
    temp2.next = i
    temp2 = temp2.next
    print("-", temp2.val, end="")

new_head = Solution().mergeTwoLists(head, head2)
print("\n", "new_head:", new_head.val, end="")
while new_head.next is not None:
    new_head = new_head.next
    print("-", new_head.val, end="")
