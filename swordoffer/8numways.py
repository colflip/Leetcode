# 10- II. 青蛙跳台阶问题
from functools import lru_cache


class Solution:
    @lru_cache()
    def numWays(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b % 1000000007
        # ------------------------------
        # if n == 0:
        #     return 1
        # elif n == 1:
        #     return 1
        # else:
        #     return (self.numWays(n - 1) + self.numWays(n - 2)) % 1000000007
