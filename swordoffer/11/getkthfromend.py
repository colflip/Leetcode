# 剑指 Offer 22. 链表中倒数第k个节点

# Definitionfor singly - linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast, slow = head, head
        for i in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow


list = [1, 2, 3, 4, 5]
temp = ListNode(list[0])
head = temp
print(" head:", temp.val, end="")
for i in list[1:]:
    i = ListNode(i)
    temp.next = i
    temp = temp.next
    print("-", temp.val, end="")
k = 2
head_k = Solution().getKthFromEnd(head, k)
print("\n", "head_k:", head_k.val, end="")
while head_k.next is not None:
    head_k = head_k.next
    print("-", head_k.val, end="")
