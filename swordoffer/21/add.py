# 剑指 Offer 65. 不用加减乘除做加法

MASK1 = 4294967296  # 2^32
MASK2 = 2147483648  # 2^31
MASK3 = 2147483647  # 2^31-1


class Solution:
    def add(self, a: int, b: int) -> int:
        a %= MASK1
        b %= MASK1
        while b != 0:
            carry = ((a & b) << 1) % MASK1
            a = (a ^ b) % MASK1
            b = carry
        if a & MASK2:
            return ~((a ^ MASK2) ^ MASK3)
        else:
            return a


a = 1
b = 1
print(Solution().add(a, b))
