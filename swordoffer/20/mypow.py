# 剑指 Offer 16. 数值的整数次方

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n == 0:
            return res
        elif n == 1:
            return x
        elif n == -1:
            return 1 / x
        a, b = divmod(n, 2)
        a = self.myPow(x, a)
        res = a * a * (x if b == 1 else 1)
        return res


x = 2.00000
n = -2
print(Solution().myPow(x, n))
