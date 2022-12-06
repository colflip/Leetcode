# 剑指 Offer 15. 二进制中1的个数

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


n = 3
print(Solution().hammingWeight(n))
