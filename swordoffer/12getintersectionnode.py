# 剑指 Offer 25. 合并两个排序的链表

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = l2
            if p2:
                p2 = p2.next
            else:
                p2 = l1
        return p1


listA = [4, 1, 8, 4, 5]
listB = [5, 0, 1, 8, 4, 5]
intersectVal = 8
skipA = 2
skipB = 3

temp = head = ListNode(listA[0])
for i in listA[1:skipA]:
    i = ListNode(i)
    temp.next = i
    temp = temp.next
temp2 = head2 = ListNode(listB[0])
for i in listB[1:skipB]:
    i = ListNode(i)
    temp2.next = i
    temp2 = temp2.next

for i in listA[skipA:]:
    i = ListNode(i)
    temp.next = i
    temp2.next = i
    temp = temp.next
    temp2 = temp2.next

head_common = Solution().mergeTwoLists(head, head2)
print("head_common:", head_common.val, end="")
while head_common.next is not None:
    head_common = head_common.next
    print("-", head_common.val, end="")
