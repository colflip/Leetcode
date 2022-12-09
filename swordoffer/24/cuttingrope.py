# 剑指 Offer 14- I. 剪绳子
# https://leetcode-cn.com/problems/jian-sheng-zi-lcof/

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2

        if n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            return 3 ** (n // 3 - 1) * (n % 3 + 3)
        else:
            return 3 ** (n // 3) * (n % 3)


n = 10
print(Solution().cuttingRope(n))
