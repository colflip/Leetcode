# 剑指 Offer 31. 栈的压入、弹出序列
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        def find1(x):
            return popped.index(pushed[x])

        def find2(x):
            return pushed.index(popped[x])

        if not pushed or not popped: return True
        if popped == pushed[::-1]: return True
        big1 = find1(-1)
        for i in range(big1, len(popped) - 1):
            if find2(i) < find2(i + 1):
                return False
        if find2(0) - find2(1) >= 2:
            return False
        sett = [find2(i) for i in range(len(popped))]
        ori = [i for i in range(len(pushed))]
        sett = sett[big1:]
        for q in range(len(sett)):
            ori.remove(sett[q])
        for j in range(0, big1 - 1):
            if find2(j) > find2(j + 1):
                if find2(j + 1) == ori[0:ori.index(find2(j))][-1]:
                    pass
                else:
                    return False
            ori.remove(find2(j))
        return True


if __name__ == "__main__":
    pushed, popped = [1, 2, 3, 4, 5], [4, 5, 3, 2, 1]
    print(Solution().validateStackSequences(pushed, popped))
