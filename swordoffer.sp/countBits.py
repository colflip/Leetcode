"""
counting-bits
https://leetcode-cn.com/problems/counting-bits/
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1 if i % 2 != 0 else dp[i >> 1]
        return dp


if __name__ == "__main__":
    n = 5
    s = Solution()
    print(s.countBits(n))
