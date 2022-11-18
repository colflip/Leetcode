# 30. 包含min函数的栈
class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2 == []:
            if self.stack1 == []:
                return -1
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
