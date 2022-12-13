# 382. 链表随机节点
from random import choice
from typing import Optional

from Cython.Compiler.ExprNodes import ListNode


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return choice(self.arr)
