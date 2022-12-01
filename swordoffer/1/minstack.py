# 剑指 Offer 30. 包含min函数的栈
import math


class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minstack.append(self.minstack[-1] if self.minstack[-1] < x else x)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
