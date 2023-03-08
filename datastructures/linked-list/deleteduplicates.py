# 83. 删除排序链表中的重复元素
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None
        head1 = head
        pos, pos1 = head, head1
        while pos:
            if pos.val > pos1.val:
                pos1.next = pos
                pos1 = pos1.next
            pos = pos.next
        pos1.next = None
        return head1
