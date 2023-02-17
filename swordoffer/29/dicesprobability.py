# 剑指 Offer 60. n个骰子的点数
from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        res = [0] * (n * 5 + 1)
        res[0] = 1
        base = 0
        for j in range(n):
            base = j * 5
            for i in range(base, -1, -1):
                for k in range(5, 0, -1):
                    res[i + k] += res[i] / 6
                res[i] /= 6
        return res
